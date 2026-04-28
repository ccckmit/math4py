"""範例：使用 Rete 推論引擎進行邏輯推理。

包含多個範例測試推論結果是否正確。
"""

from math4py.logic import Fact, ReteEngine, Rule, create_fact


def test_family_relations():
    """範例 1：家族關係推理。

    已知：Alice 是 Bob 的母親，Bob 是 Charlie 的父親。
    推論：Alice 是 Charlie 的祖母。
    """
    engine = ReteEngine()

    # 加入事實
    engine.add_fact(create_fact(person="Alice", relation="mother", target="Bob"))
    engine.add_fact(create_fact(person="Bob", relation="father", target="Charlie"))

    # 規則：如果 X 是 Y 的母親，Y 是 Z 的父親，則 X 是 Z 的祖母
    def add_grandmother(f1: Fact, f2: Fact) -> Fact:
        return create_fact(
            person=f1.attributes["person"], relation="grandmother", target=f2.attributes["target"]
        )

    rule = Rule(
        "grandmother_rule",
        [
            {"relation": "mother"},
            {"relation": "father"},
        ],
        [add_grandmother],
        priority=1,
    )
    engine.add_rule(rule)

    # 執行推論
    count = engine.run()
    print(f"家族關係推論：執行了 {count} 次規則")

    # 查詢結果
    results = engine.query_facts({"relation": "grandmother"})
    print(f"推論結果：{results}")

    # 驗證
    assert len(results) == 1
    assert results[0].attributes["person"] == "Alice"
    assert results[0].attributes["target"] == "Charlie"
    print("✓ 家族關係推論正確\n")
    return True


def test_mathematical_inference():
    """範例 2：數學推理。

    已知：數字和運算關係，推論新事實（限制推論次數）。
    """
    engine = ReteEngine()

    # 加入數字事實
    engine.add_fact(create_fact(number=2, type="even"))
    engine.add_fact(create_fact(number=3, type="odd"))
    engine.add_fact(create_fact(number=4, type="even"))

    # 規則：偶數 + 偶數 = 偶數（限制和小於 10）
    def add_even_sum(f1: Fact, f2: Fact) -> Fact:
        result = f1.attributes["number"] + f2.attributes["number"]
        if result < 10:  # 限制推論範圍
            return create_fact(number=result, type="even")
        return None

    rule_even_sum = Rule(
        "even_sum_rule",
        [
            {"type": "even"},
            {"type": "even"},
        ],
        [add_even_sum],
        priority=1,
    )
    engine.add_rule(rule_even_sum)

    # 執行推論
    count = engine.run(max_iterations=5)  # 限制迭代次數
    print(f"數學推論：執行了 {count} 次規則")

    # 查詢結果
    results = engine.query_facts({"type": "even"})
    numbers = [f.attributes["number"] for f in results]
    print(f"推論結果（偶數）：{sorted(numbers)}")

    # 驗證：2+4=6 應該被推論出來
    assert 6 in numbers, "應該推論出 2+4=6"
    print("✓ 數學推論正確\n")
    return True


def test_diagnostic_system():
    """範例 3：診斷系統。

    根據症狀推論疾病。
    """
    engine = ReteEngine()

    # 病人症狀
    engine.add_fact(create_fact(symptom="fever"))
    engine.add_fact(create_fact(symptom="cough"))
    engine.add_fact(create_fact(symptom="headache"))

    # 規則：發燒 + 咳嗽 = 流感
    def diagnose_flu(*facts) -> Fact:
        return create_fact(diagnosis="flu")

    rule_flu = Rule(
        "flu_diagnosis",
        [
            {"symptom": "fever"},
            {"symptom": "cough"},
        ],
        [diagnose_flu],
        priority=2,
    )
    engine.add_rule(rule_flu)

    # 規則：發燒 + 頭痛 = 感冒
    def diagnose_cold(*facts) -> Fact:
        return create_fact(diagnosis="cold")

    rule_cold = Rule(
        "cold_diagnosis",
        [
            {"symptom": "fever"},
            {"symptom": "headache"},
        ],
        [diagnose_cold],
        priority=1,
    )
    engine.add_rule(rule_cold)

    # 執行推論
    count = engine.run()
    print(f"診斷系統推論：執行了 {count} 次規則")

    # 查詢結果
    flu_results = engine.query_facts({"diagnosis": "flu"})
    cold_results = engine.query_facts({"diagnosis": "cold"})
    print(f"診斷結果：流感={flu_results}, 感冒={cold_results}")

    # 驗證
    assert len(flu_results) >= 1, "應該診斷出流感"
    assert len(cold_results) >= 1, "應該診斷出感冒"
    print("✓ 診斷系統推論正確\n")
    return True


def test_transitive_relation():
    """範例 4：遞移關係推理。

    已知：A < B, B < C，推論 A < C。
    """
    engine = ReteEngine()

    # 加入事實
    engine.add_fact(create_fact(x="A", relation="<", y="B"))
    engine.add_fact(create_fact(x="B", relation="<", y="C"))

    # 規則：遞移性
    def add_transitive(f1: Fact, f2: Fact) -> Fact:
        return create_fact(x=f1.attributes["x"], relation="<", y=f2.attributes["y"])

    rule_transitive = Rule(
        "transitive_rule",
        [
            {"relation": "<"},
            {"relation": "<"},
        ],
        [add_transitive],
        priority=1,
    )
    engine.add_rule(rule_transitive)

    # 執行推論
    count = engine.run()
    print(f"遞移關係推論：執行了 {count} 次規則")

    # 查詢結果
    results = engine.query_facts({"x": "A", "y": "C"})
    print(f"推論結果：{results}")

    # 驗證
    assert len(results) == 1, "應該推論出 A < C"
    print("✓ 遞移關係推論正確\n")
    return True


if __name__ == "__main__":
    print("=" * 60)
    print("Rete 推論引擎範例測試")
    print("=" * 60 + "\n")

    test_family_relations()
    test_mathematical_inference()
    test_diagnostic_system()
    test_transitive_relation()

    print("=" * 60)
    print("所有範例測試通過！")
    print("=" * 60)
