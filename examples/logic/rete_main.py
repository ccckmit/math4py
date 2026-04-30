"""Rete 推論引擎主程式 - Prolog 風格語法。

讀取 .kb 知識庫檔案，執行推論並印出結果。

知識庫語法（類似 Prolog）：
  - 事實：fact(屬性1=值1, 屬性2=值2).
  - 規則：rule(名稱) :- condition(模式) -> action(結果).
"""

import os
import sys
from typing import Any, Callable, Dict, List, Optional, Tuple

from math4py.logic import Fact, ReteEngine, Rule, create_fact


def parse_kb_file(filepath: str) -> Tuple[List[Fact], List[Rule]]:
    """讀取 .kb 知識庫檔案，回傳事實和規則列表。

    語法：
      fact(屬性1=值1, 屬性2=值2).
      rule(名稱) :- condition(模式) -> action(結果).
    """
    facts = []
    rules = []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("fact(") and line.endswith(")."):
            fact = _parse_fact(line)
            if fact:
                facts.append(fact)

        elif line.startswith("rule(") and ":-" in line:
            rule = _parse_rule(line)
            if rule:
                rules.append(rule)

        else:
            print(f"警告：第 {line_num} 行語法無法識別：{line}")

    return facts, rules


def _parse_fact(line: str) -> Optional[Fact]:
    """解析事實：fact(key1=val1, key2=val2)."""
    try:
        # 去掉 "fact(" 和 ")."
        inner = line[5:-2]
        kwargs = _parse_key_value_pairs(inner)
        return create_fact(**kwargs)
    except Exception as e:
        print(f"解析事實失敗：{line}, 錯誤：{e}")
        return None


def _parse_rule(line: str) -> Optional[Rule]:
    """解析規則：rule(名稱) :- condition(...) -> action(...)."""
    try:
        # 分割 rule(名稱) 和 主體
        parts = line.split(":-", 1)
        if len(parts) != 2:
            return None

        rule_part = parts[0].strip()
        body_part = parts[1].strip()

        # 解析規則名稱
        rule_name = rule_part[5:-1].strip()  # 去掉 "rule(" 和 ")"

        # 解析條件和動作
        if "->" not in body_part:
            print(f"規則缺少 -> ：{line}")
            return None

        cond_action = body_part.split("->", 1)
        conditions_str = cond_action[0].strip()
        action_str = cond_action[1].strip()

        # 解析條件（可能有多個，用逗號分隔）
        conditions = _parse_conditions(conditions_str)

        # 解析動作
        action = _parse_action(action_str)

        return Rule(rule_name, conditions, [action])

    except Exception as e:
        print(f"解析規則失敗：{line}, 錯誤：{e}")
        return None


def _parse_key_value_pairs(text: str) -> Dict[str, Any]:
    """解析 key=value 對，用逗號分隔。"""
    kwargs = {}
    pairs = text.split(",")
    for pair in pairs:
        pair = pair.strip()
        if "=" in pair:
            key, value = pair.split("=", 1)
            key = key.strip()
            value = value.strip()
            # 嘗詴轉換為適當的型態
            kwargs[key] = _convert_value(value)
    return kwargs


def _convert_value(value: str) -> Any:
    """轉換字串值為適當的 Python 型態。"""
    # 移除引號
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]

    # 布林值
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False

    # 數字
    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value


def _parse_conditions(conditions_str: str) -> List[Dict]:
    """解析條件列表。"""
    conditions = []
    # 簡化：假設每個條件都是 func(attr1=val1, attr2=val2) 格式
    depth = 0
    current = ""
    for char in conditions_str:
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        if char == "," and depth == 0:
            if current.strip():
                cond = _parse_single_condition(current.strip())
                if cond:
                    conditions.append(cond)
            current = ""
        else:
            current += char

    if current.strip():
        cond = _parse_single_condition(current.strip())
        if cond:
            conditions.append(cond)

    return conditions


def _parse_single_condition(cond_str: str) -> Optional[Dict]:
    """解析單一條件：func(attr1=val1, attr2=val2)"""
    try:
        # 找出函數名和內容
        idx = cond_str.find("(")
        if idx == -1:
            return None

        cond_str[:idx].strip()
        inner = cond_str[idx + 1 : -1].strip()

        kwargs = _parse_key_value_pairs(inner)
        return kwargs

    except Exception as e:
        print(f"解析條件失敗：{cond_str}, 錯誤：{e}")
        return None


def _parse_action(action_str: str) -> Callable:
    """解析動作並回傳可呼叫的函數。"""

    def action_wrapper(*args):
        try:
            # action_str 格式：person=f1.person, relation="grandmother", target=f2.target
            kwargs = {}
            pairs = action_str.split(",")
            for pair in pairs:
                pair = pair.strip()
                if "=" not in pair:
                    continue
                key, value = pair.split("=", 1)
                key = key.strip()
                value = value.strip()

                # 處理變數引用（f1.person, f2.target）
                if "." in value:
                    parts = value.split(".")
                    if len(parts) == 2 and parts[0].startswith("f") and parts[0][1:].isdigit():
                        fact_idx = int(parts[0][1:]) - 1
                        attr = parts[1]
                        if 0 <= fact_idx < len(args):
                            value = args[fact_idx].attributes.get(attr)
                        else:
                            value = None
                    else:
                        value = _convert_value(value)
                else:
                    value = _convert_value(value)

                kwargs[key] = value

            return create_fact(**kwargs)

        except Exception as e:
            print(f"執行動作失敗：{action_str}, 錯誤：{e}")
            return None

    return action_wrapper


def run_inference(kb_file: str, verbose: bool = True) -> ReteEngine:
    """讀取知識庫，執行推論，回傳引擎。"""
    if not os.path.exists(kb_file):
        print(f"錯誤：檔案不存在 - {kb_file}")
        return None

    print(f"讀取知識庫：{kb_file}")
    facts, rules = parse_kb_file(kb_file)

    print(f"載入 {len(facts)} 個事實和 {len(rules)} 個規則")

    engine = ReteEngine()

    # 加入事實
    for fact in facts:
        engine.add_fact(fact)

    # 加入規則
    for rule in rules:
        engine.add_rule(rule)

    # 執行推論
    if verbose:
        print("\n開始推論...")

    count = engine.run()

    if verbose:
        print(f"推論完成，共執行 {count} 次規則")
        print(f"最終事實數量：{len(engine.facts)}")

    return engine


def print_results(engine: ReteEngine):
    """印出推論結果。"""
    print("\n" + "=" * 60)
    print("推論結果")
    print("=" * 60)

    # 分類並印出事實
    inferred = set(f.id for f in engine.inferred_facts)
    original = set(f.id for f in engine.facts) - inferred

    print("\n[原始事實]")
    for fact in engine.facts:
        if fact.id in original:
            print(f"  {fact}")

    print("\n[推論事實]")
    if engine.inferred_facts:
        for fact in engine.inferred_facts:
            print(f"  {fact}")
    else:
        print("  (無)")

    # 查詢各種關係
    print("\n[查詢結果]")
    relations = set(
        f.attributes.get("relation") for f in engine.facts if "relation" in f.attributes
    )

    for rel in sorted(relations):
        matching = engine.query_facts({"relation": rel})
        if matching:
            print(f"\n  關係：{rel}")
            for f in matching:
                print(f"    {f}")


def main():
    """主程式。"""
    if len(sys.argv) < 2:
        print("用法：python rete_main.py <知識庫檔案.kb> [--verbose]")
        print("\n範例：")
        print("  python rete_main.py examples/logic/family.kb")
        print("  python rete_main.py examples/logic/math.kb --verbose")
        sys.exit(1)

    kb_file = sys.argv[1]
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    engine = run_inference(kb_file, verbose)

    if engine:
        print_results(engine)


if __name__ == "__main__":
    main()
