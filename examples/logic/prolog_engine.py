"""簡易 Prolog 解譯器 - 核心實作。

支援事實、規則、查詢，語法接近 Prolog。
"""

from typing import Dict, List, Optional, Set, Tuple


class Variable:
    """Prolog 變數。"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Variable) and self.name == other.name

    def __hash__(self):
        return hash(("var", self.name))


class Structure:
    """Prolog 結構（functor + arguments）。"""

    def __init__(self, functor: str, args: List):
        self.functor = functor
        self.args = args

    def __repr__(self):
        if not self.args:
            return self.functor
        args_str = ", ".join(repr(a) for a in self.args)
        return f"{self.functor}({args_str})"

    def __eq__(self, other):
        if not isinstance(other, Structure):
            return False
        return self.functor == other.functor and self.args == other.args

    def __hash__(self):
        return hash((self.functor, tuple(self.args)))


def parse_term(text: str):
    """解析 Prolog 項。"""
    text = text.strip()
    if "(" not in text:
        # 常數或變數
        if text[0].isupper() or text == "_":
            return Variable(text)
        try:
            return int(text)
        except ValueError:
            try:
                return float(text)
            except ValueError:
                return text

    # 結構
    functor, rest = text.split("(", 1)
    rest = rest.rstrip(")")
    args = []
    depth = 0
    current = ""
    for char in rest:
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        elif char == "," and depth == 0:
            if current.strip():
                args.append(parse_term(current.strip()))
            current = ""
            continue
        current += char
    if current.strip():
        args.append(parse_term(current.strip()))
    return Structure(functor.strip(), args)


def unify(term1, term2, bindings: Dict = None) -> Optional[Dict]:
    """統一算法。"""
    if bindings is None:
        bindings = {}

    if isinstance(term1, Variable):
        if term1.name in bindings:
            return unify(bindings[term1.name], term2, bindings)
        bindings[term1.name] = term2
        return bindings

    if isinstance(term2, Variable):
        if term2.name in bindings:
            return unify(term1, bindings[term2.name], bindings)
        bindings[term2.name] = term1
        return bindings

    if not isinstance(term1, Structure) or not isinstance(term2, Structure):
        return bindings if term1 == term2 else None

    if term1.functor != term2.functor or len(term1.args) != len(term2.args):
        return None

    for a1, a2 in zip(term1.args, term2.args):
        bindings = unify(a1, a2, bindings)
        if bindings is None:
            return None
    return bindings


class Clause:
    """Prolog 子句。"""

    def __init__(self, head, body=None):
        self.head = head
        self.body = body or []

    def is_fact(self):
        return len(self.body) == 0

    def __repr__(self):
        if self.is_fact():
            return f"{self.head}."
        body_str = ", ".join(repr(t) for t in self.body)
        return f"{self.head} :- {body_str}."


class PrologEngine:
    """Prolog 推理引擎。"""

    def __init__(self):
        self.clauses: List[Clause] = []

    def load_file(self, filepath: str):
        """載入 Prolog 程式檔。"""
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        lines = []
        for line in content.split("\n"):
            line = line.strip()
            if not line or line.startswith("%"):
                continue
            lines.append(line)

        for line in lines:
            clause = self._parse_clause(line)
            if clause:
                self.clauses.append(clause)

    def _parse_clause(self, text: str) -> Optional[Clause]:
        """解析子句。"""
        if ":-" in text:
            parts = text.split(":-", 1)
            head = parse_term(parts[0].strip())
            body_str = parts[1].rstrip(".").strip()
            body = [parse_term(b.strip()) for b in body_str.split(",")]
            return Clause(head, body)
        elif text.endswith("."):
            head = parse_term(text[:-1].strip())
            return Clause(head)
        return None

    def query(self, goal_str: str) -> List[Dict]:
        """執行查詢。"""
        goal = parse_term(goal_str)
        return self._prove([goal], {})

    def _prove(self, goals: List, bindings: Dict) -> List[Dict]:
        """證明目標。"""
        if not goals:
            return [bindings]

        results = []
        first = goals[0]
        rest = goals[1:]

        for clause in self.clauses:
            new_bindings = unify(first, clause.head, bindings.copy())
            if new_bindings is None:
                continue

            if clause.is_fact():
                rest_results = self._prove(rest, new_bindings)
                results.extend(rest_results)
            else:
                new_goals = [unify(g, clause.head, new_bindings.copy()) or g for g in clause.body] + rest
                new_goals = [g for g in new_goals if g is not None]
                combined_results = self._prove(new_goals, new_bindings)
                results.extend(combined_results)

        return results

    def print_results(self, results: List[Dict], query: str):
        """印出查詢結果。"""
        if not results:
            print("false.")
            return

        # 找出所有變數
        query_term = parse_term(query)
        variables = set()
        self._collect_vars(query_term, variables)

        if not variables:
            print("true.")
            return

        print(f"查詢：{query}")
        for i, bindings in enumerate(results, 1):
            print(f"\n  解答 {i}:")
            for var in sorted(variables):
                if var in bindings:
                    print(f"    {var} = {bindings[var]}")

    def _collect_vars(self, term, variables: Set):
        """收集變數名稱。"""
        if isinstance(term, Variable):
            variables.add(term.name)
        elif isinstance(term, Structure):
            for arg in term.args:
                self._collect_vars(arg, variables)


def main():
    """主程式。"""
    import sys

    if len(sys.argv) < 2:
        print("用法：python prolog_engine.py <程式檔.pl> [查詢]")
        print("\n範例：")
        print("  python prolog_engine.py examples/logic/family.pl")
        print('  python prolog_engine.py examples/logic/family.pl "grandmother(X, Y)"')
        sys.exit(1)

    filepath = sys.argv[1]

    engine = PrologEngine()
    engine.load_file(filepath)

    print(f"已載入 {len(engine.clauses)} 個子句")
    print("=" * 60)

    if len(sys.argv) >= 3:
        query_str = " ".join(sys.argv[2:])
        results = engine.query(query_str)
        engine.print_results(results, query_str)
    else:
        print("可用謂詞：")
        predicates = set(c.head.functor for c in engine.clauses if isinstance(c.head, Structure))
        for pred in sorted(predicates):
            print(f"  {pred}")


if __name__ == "__main__":
    main()
