"""Tests for logic/rete_inference.py."""

from math4py.logic import Fact, Rule, ReteEngine, create_fact


class TestFact:
    def test_create_fact(self):
        f = create_fact(person="Alice", age=30)
        assert f.attributes["person"] == "Alice"
        assert f.attributes["age"] == 30

    def test_fact_matches(self):
        f = create_fact(type="even", number=2)
        assert f.matches({"type": "even"})
        assert not f.matches({"type": "odd"})

    def test_fact_matches_with_callable(self):
        f = create_fact(number=5)
        assert f.matches({"number": lambda x: x > 0})
        assert not f.matches({"number": lambda x: x < 0})


class TestRule:
    def test_create_rule(self):
        def dummy_action(*args):
            return None

        rule = Rule("test", [{"type": "even"}], [dummy_action])
        assert rule.name == "test"
        assert len(rule.conditions) == 1


class TestReteEngine:
    def test_single_condition_rule(self):
        """測試單條件規則。"""
        engine = ReteEngine()

        results = []

        def add_result(fact):
            results.append(fact.attributes.get("value"))
            return None

        rule = Rule("test_rule", [{"type": "target"}], [add_result])
        engine.add_rule(rule)

        engine.add_fact(create_fact(type="target", value=42))
        engine.run()

        assert len(results) == 1
        assert results[0] == 42

    def test_multi_condition_rule(self):
        """測試多條件規則（家族關係）。"""
        engine = ReteEngine()

        def add_grandmother(f1, f2):
            return create_fact(
                person=f1.attributes["person"],
                relation="grandmother",
                target=f2.attributes["target"],
            )

        rule = Rule(
            "grandmother_rule",
            [{"relation": "mother"}, {"relation": "father"}],
            [add_grandmother],
        )
        engine.add_rule(rule)

        engine.add_fact(create_fact(person="Alice", relation="mother", target="Bob"))
        engine.add_fact(create_fact(person="Bob", relation="father", target="Charlie"))

        count = engine.run()
        assert count == 1

        results = engine.query_facts({"relation": "grandmother"})
        assert len(results) == 1
        assert results[0].attributes["person"] == "Alice"
        assert results[0].attributes["target"] == "Charlie"

    def test_no_duplicate_inference(self):
        """測試不重複推論相同的事實。"""
        engine = ReteEngine()

        def add_even(f1, f2):
            result = f1.attributes["number"] + f2.attributes["number"]
            if result < 20:
                return create_fact(number=result, type="even")
            return None

        rule = Rule(
            "even_sum",
            [{"type": "even"}, {"type": "even"}],
            [add_even],
        )
        engine.add_rule(rule)

        engine.add_fact(create_fact(number=2, type="even"))
        engine.add_fact(create_fact(number=4, type="even"))

        count = engine.run(max_iterations=5)
        # 應該只推論出 6，不會無限循環
        assert count >= 1

        results = engine.query_facts({"type": "even"})
        numbers = [f.attributes["number"] for f in results]
        assert 6 in numbers

    def test_query_facts(self):
        """測試查詢事實。"""
        engine = ReteEngine()
        engine.add_fact(create_fact(type="even", number=2))
        engine.add_fact(create_fact(type="odd", number=3))

        evens = engine.query_facts({"type": "even"})
        assert len(evens) == 1
        assert evens[0].attributes["number"] == 2

    def test_clear_engine(self):
        """測試清除引擎。"""
        engine = ReteEngine()
        engine.add_fact(create_fact(type="test"))
        engine.clear()
        assert len(engine.facts) == 0
        assert len(engine.agenda) == 0
