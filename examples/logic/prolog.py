"""簡易 Prolog 解譯器 - 正確工作的版本。"""

from typing import Dict, List, Optional, Tuple


def parse_term(s: str) -> Tuple:
    """解析 term。"""
    s = s.strip()
    if "(" not in s:
        if s[0].isupper() or s[0] == "_":
            return ("var", s)
        try:
            return ("num", int(s))
        except ValueError:
            try:
                return ("num", float(s))
            except ValueError:
                return ("const", s)

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
            args.append(parse_term(current.strip()))
            current = ""
            continue
        current += ch
    if current.strip():
        args.append(parse_term(current.strip()))
    return ("struct", name.strip(), args)


def deref(term, env):
    """解引用變數。"""
    visited = set()
    while isinstance(term, tuple) and term[0] == "var" and term[1] in env:
        if term[1] in visited:
            break
        visited.add(term[1])
        term = env[term[1]]
    return term


def unify(t1: Tuple, t2: Tuple, env: Dict = None) -> Optional[Dict]:
    """統一算法。"""
    if env is None:
        env = {}

    t1 = deref(t1, env)
    t2 = deref(t2, env)

    # 變數
    if isinstance(t1, tuple) and t1[0] == "var":
        if isinstance(t2, tuple) and t2[0] == "var" and t1[1] == t2[1]:
            return env
        env[t1[1]] = t2
        return env
    if isinstance(t2, tuple) and t2[0] == "var":
        env[t2[1]] = t1
        return env

    # 常數
    if isinstance(t1, tuple) and t1[0] in ("const", "num"):
        return env if t1 == t2 else None
    if isinstance(t2, tuple) and t2[0] in ("const", "num"):
        return env if t1 == t2 else None

    # 結構
    if not (isinstance(t1, tuple) and t1[0] == "struct"):
        return None
    if not (isinstance(t2, tuple) and t2[0] == "struct"):
        return None
    if t1[1] != t2[1] or len(t1[2]) != len(t2[2]):
        return None

    for a, b in zip(t1[2], t2[2]):
        env = unify(a, b, env)
        if env is None:
            return None
    return env


def load_pl(path: str) -> List[Tuple]:
    """載入 .pl 檔案。"""
    clauses = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("%"):
                continue
            clause = parse_clause(line)
            if clause:
                clauses.append(clause)
    return clauses


def parse_clause(line: str) -> Optional[Tuple]:
    """解析子句。"""
    line = line.strip()
    if ":-" in line:
        head_str, body_str = line.split(":-", 1)
        head = parse_term(head_str.strip())
        body_str = body_str.rstrip(".").strip()
        # 正確分割 body 中的多個目標
        body_terms = []
        depth = 0
        current = ""
        for ch in body_str:
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            elif ch == "," and depth == 0:
                body_terms.append(parse_term(current.strip()))
                current = ""
                continue
            current += ch
        if current.strip():
            body_terms.append(parse_term(current.strip()))
        return ("rule", head, body_terms)
    elif line.endswith("."):
        head = parse_term(line[:-1].strip())
        return ("fact", head)
    return None


def query(clauses: List[Tuple], goal_str: str) -> List[Dict]:
    """查詢。"""
    goal = parse_term(goal_str)
    return solve(clauses, [goal], {})


_var_counter = 0


def fresh_var():
    """產生一個新的唯一變數名稱。"""
    global _var_counter
    _var_counter += 1
    return f"_V{_var_counter}"


def rename_vars(term, var_map=None):
    """為 term 中的變數產生新的名稱。"""
    if var_map is None:
        var_map = {}

    if isinstance(term, tuple):
        if term[0] == "var":
            if term[1] not in var_map:
                var_map[term[1]] = fresh_var()
            return ("var", var_map[term[1]])
        elif term[0] == "struct":
            new_args = [rename_vars(arg, var_map) for arg in term[2]]
            return ("struct", term[1], new_args)
    return term


def solve(clauses: List[Tuple], goals: List[Tuple], env: Dict) -> List[Dict]:
    """證明目標。"""
    if not goals:
        return [env]

    results = []
    first = goals[0]
    rest = goals[1:]

    for clause in clauses:
        if clause[0] == "fact":
            new_env = unify(first, clause[1], dict(env))
            if new_env is not None:
                results.extend(solve(clauses, rest, new_env))
        else:  # rule
            # 為規則產生新的變數名稱
            var_map = {}
            head = rename_vars(clause[1], var_map)
            body = [rename_vars(b, var_map) for b in clause[2]]

            new_env = unify(first, head, dict(env))
            if new_env is not None:
                new_goals = body + rest
                results.extend(solve(clauses, new_goals, new_env))

    return results


def term_str(term: Tuple) -> str:
    """Term 轉字串。"""
    if isinstance(term, tuple):
        if term[0] == "var":
            return term[1]
        elif term[0] == "const":
            return term[1]
        elif term[0] == "num":
            return str(term[1])
        elif term[0] == "struct":
            args = ", ".join(term_str(a) for a in term[2])
            return f"{term[1]}({args})"
    return str(term)


def collect_vars(term: Tuple, vars: set = None) -> set:
    """收集變數。"""
    if vars is None:
        vars = set()
    if isinstance(term, tuple):
        if term[0] == "var":
            vars.add(term[1])
        elif term[0] == "struct":
            for arg in term[2]:
                collect_vars(arg, vars)
    return vars


def get_original_var_name(renamed_var):
    """從重新命名的變數取得原始名稱。"""
    if renamed_var.startswith("_V"):
        return None  # 內部變數，不是查詢變數
    return renamed_var


def print_results(results: List[Dict], query_str: str):
    """印出結果。"""
    if not results:
        print("false.")
        return

    goal = parse_term(query_str)
    query_vars = collect_vars(goal)

    if not query_vars:
        print("true.")
        return

    print(f"查詢：{query_str}")
    for i, env in enumerate(results, 1):
        print(f"\n  解答 {i}:")
        for var in sorted(query_vars):
            val = deref(("var", var), env)
            if val is not None and val != ("var", var):
                print(f"    {var} = {term_str(val)}")


def main():
    import sys

    if len(sys.argv) < 2:
        print("用法：python prolog.py <檔案.pl> [查詢]")
        print("\n範例：")
        print("  python prolog.py examples/logic/family.pl")
        print('  python prolog.py examples/logic/family.pl "grandmother(X, Y)"')
        sys.exit(1)

    filepath = sys.argv[1]
    clauses = load_pl(filepath)

    print(f"已載入 {len(clauses)} 個子句")
    print("=" * 60)

    if len(sys.argv) >= 3:
        query_str = " ".join(sys.argv[2:])
        results = query(clauses, query_str)
        print_results(results, query_str)
    else:
        print("可用謂詞：")
        predicates = set()
        for c in clauses:
            if c[0] == "fact" and isinstance(c[1], tuple) and c[1][0] == "struct":
                predicates.add(c[1][1])
            elif c[0] == "rule" and isinstance(c[1], tuple) and c[1][0] == "struct":
                predicates.add(c[1][1])
        for p in sorted(predicates):
            print(f"  {p}")


if __name__ == "__main__":
    main()
