"""超簡單 Prolog 解譯器。

直接、簡單的實作，支援：
- 事實：pred(arg1, arg2).
- 規則：head :- body1, body2.
- 查詢
"""

from typing import Dict, List


def parse_term(s: str):
    """解析一個 term。"""
    s = s.strip()
    if "(" not in s:
        # 常數或變數
        if s[0].isupper():
            return ("var", s)
        try:
            return ("num", int(s))
        except ValueError:
            try:
                return ("num", float(s))
            except ValueError:
                return ("const", s)

    # 複合 term
    name, rest = s.split("(", 1)
    rest = rest.rstrip(")")
    args = []
    depth = 0
    current = ""
    for ch in rest:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "," and depth == 0:
            args.append(parse_term(current))
            current = ""
            continue
        current += ch
    if current:
        args.append(parse_term(current))
    return ("struct", name.strip(), args)


def parse_clause(line: str):
    """解析子句。"""
    line = line.strip()
    if not line or line.startswith("%"):
        return None

    if ":-" in line:
        head_str, body_str = line.split(":-", 1)
        head = parse_term(head_str.strip())
        body_str = body_str.rstrip(".").strip()
        body = [parse_term(b.strip()) for b in body_str.split(",")]
        return ("rule", head, body)
    elif line.endswith("."):
        head = parse_term(line[:-1].strip())
        return ("fact", head)
    return None


def unify(term1, term2, env=None):
    """統一算法。"""
    if env is None:
        env = {}

    # 變數
    if term1[0] == "var":
        name = term1[1]
        if name in env:
            return unify(env[name], term2, env)
        env[name] = term2
        return env

    if term2[0] == "var":
        name = term2[1]
        if name in env:
            return unify(term1, env[name], env)
        env[name] = term1
        return env

    # 常數
    if term1[0] == "const" and term2[0] == "const":
        return env if term1[1] == term2[1] else None
    if term1[0] == "num" and term2[0] == "num":
        return env if term1[1] == term2[1] else None

    # 結構
    if term1[0] == "struct" and term2[0] == "struct":
        if term1[1] != term2[1] or len(term1[2]) != len(term2[2]):
            return None
        for a, b in zip(term1[2], term2[2]):
            env = unify(a, b, env)
            if env is None:
                return None
        return env

    return None


def load_pl(filepath: str) -> List:
    """載入 .pl 檔案。"""
    clauses = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            clause = parse_clause(line)
            if clause:
                clauses.append(clause)
    return clauses


def query_all(clauses: List, goal, env=None) -> List[Dict]:
    """查詢所有解。"""
    if env is None:
        env = {}

    results = []

    for clause in clauses:
        if clause[0] == "fact":
            new_env = unify(goal, clause[1], env.copy())
            if new_env is not None:
                results.append(new_env)
        elif clause[0] == "rule":
            head = clause[1]
            body = clause[2]
            new_env = unify(goal, head, env.copy())
            if new_env is not None:
                # 證明 body
                body_results = prove_all(clauses, body, new_env)
                results.extend(body_results)

    return results


def prove_all(clauses: List, goals: List, env: Dict) -> List[Dict]:
    """證明多個目標。"""
    if not goals:
        return [env]

    results = []
    first = goals[0]
    rest = goals[1:]

    for clause in clauses:
        if clause[0] == "fact":
            new_env = unify(first, clause[1], env.copy())
            if new_env is not None:
                rest_results = prove_all(clauses, rest, new_env)
                results.extend(rest_results)
        elif clause[0] == "rule":
            head = clause[1]
            body = clause[2]
            new_env = unify(first, head, env.copy())
            if new_env is not None:
                new_goals = body + rest
                results.extend(prove_all(clauses, new_goals, new_env))

    return results


def ask(clauses: List, query_str: str) -> List[Dict]:
    """用字串查詢。"""
    goal = parse_term(query_str)
    return query_all(clauses, goal)


def print_results(results: List[Dict], query_str: str):
    """印出結果。"""
    if not results:
        print("false.")
        return

    # 收集變數
    variables = set()
    _collect_vars(parse_term(query_str), variables)

    if not variables:
        print("true.")
        return

    print(f"查詢：{query_str}")
    for i, env in enumerate(results, 1):
        print(f"\n  解答 {i}:")
        for var in sorted(variables):
            if var in env:
                val = env[var]
                if val[0] == "var":
                    print(f"    {var} = {val[1]}")
                elif val[0] == "const":
                    print(f"    {var} = {val[1]}")
                elif val[0] == "num":
                    print(f"    {var} = {val[1]}")
                elif val[0] == "struct":
                    args_str = ", ".join(_term_str(a) for a in val[2])
                    print(f"    {var} = {val[1]}({args_str})")


def _term_str(term):
    """轉 term 為字串。"""
    if term[0] == "var":
        return term[1]
    elif term[0] == "const":
        return term[1]
    elif term[0] == "num":
        return str(term[1])
    elif term[0] == "struct":
        args = ", ".join(_term_str(a) for a in term[2])
        return f"{term[1]}({args})"


def _collect_vars(term, variables: set):
    """收集變數。"""
    if term[0] == "var":
        variables.add(term[1])
    elif term[0] == "struct":
        for arg in term[2]:
            _collect_vars(arg, variables)


def main():
    import sys

    if len(sys.argv) < 2:
        print("用法：python prolog_simple.py <檔案.pl> [查詢]")
        print("\n範例：")
        print("  python prolog_simple.py examples/logic/family.pl")
        print('  python prolog_simple.py examples/logic/family.pl "grandmother(X, Y)"')
        sys.exit(1)

    filepath = sys.argv[1]
    clauses = load_pl(filepath)

    print(f"已載入 {len(clauses)} 個子句")
    print("=" * 60)

    if len(sys.argv) >= 3:
        query_str = " ".join(sys.argv[2:])
        results = ask(clauses, query_str)
        print_results(results, query_str)
    else:
        print("可用謂詞：")
        predicates = set()
        for c in clauses:
            if c[0] == "fact":
                if c[1][0] == "struct":
                    predicates.add(c[1][1])
            elif c[0] == "rule":
                if c[1][0] == "struct":
                    predicates.add(c[1][1])
        for p in sorted(predicates):
            print(f"  {p}")


if __name__ == "__main__":
    main()
