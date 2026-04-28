"""Rete 推論引擎。

基於 Rete 算法的邏輯推論引擎，用於高效模式匹配和規則推論。
簡化實作，專注於正確的多條件匹配。
"""

from typing import Any, Callable, Dict, List, Set, Tuple


class Fact:
    """事實（Working Memory Element）。"""

    _next_id = 0

    def __init__(self, **attributes):
        self.attributes = attributes
        self.id = Fact._next_id
        Fact._next_id += 1

    def matches(self, pattern: Dict[str, Any]) -> bool:
        """檢查事實是否匹配模式。"""
        for key, value in pattern.items():
            if key not in self.attributes:
                return False
            if callable(value):
                if not value(self.attributes[key]):
                    return False
            elif self.attributes[key] != value:
                return False
        return True

    def __repr__(self):
        return f"Fact({self.attributes})"

    def __eq__(self, other):
        return isinstance(other, Fact) and self.id == other.id

    def __hash__(self):
        return hash(self.id)


class Rule:
    """生產規則：IF conditions THEN actions。"""

    def __init__(
        self, name: str, conditions: List[Dict], actions: List[Callable], priority: int = 0
    ):
        self.name = name
        self.conditions = conditions  # List of pattern dicts
        self.actions = actions
        self.priority = priority

    def __repr__(self):
        return f"Rule({self.name})"


class ReteEngine:
    """Rete 推論引擎（簡化版）。

    支援多條件規則的正確匹配。
    """

    def __init__(self):
        self.facts: List[Fact] = []
        self.rules: List[Rule] = []
        self.agenda: List[Tuple[Rule, Tuple[Fact, ...]]] = []
        self.inferred_facts: List[Fact] = []
        # 記錄已激活的規則+事實組合，避免重複
        self.activated_combinations: Set[str] = set()

    def add_fact(self, fact: Fact):
        """加入事實到工作記憶體。"""
        # 避免加入重複的事實（屬性完全相同）
        if not any(f.attributes == fact.attributes for f in self.facts):
            self.facts.append(fact)
            # 檢查所有規則是否可以激活
            for rule in self.rules:
                self._evaluate_rule(rule, fact)

    def add_rule(self, rule: Rule):
        """加入規則。"""
        self.rules.append(rule)
        # 立即評估已有事實
        for fact in self.facts:
            self._evaluate_rule(rule, fact)

    def _evaluate_rule(self, rule: Rule, trigger_fact: Fact = None):
        """評估規則是否所有條件都滿足。"""
        conditions = rule.conditions

        if len(conditions) == 1:
            # 單條件規則
            if trigger_fact and trigger_fact.matches(conditions[0]):
                self._activate_rule(rule, (trigger_fact,))
        else:
            # 多條件規則：找出每個條件的匹配事實
            condition_matches = []
            for condition in conditions:
                matches = [f for f in self.facts if f.matches(condition)]
                condition_matches.append(matches)

            # 生成所有組合（每個條件選一個匹配的事實）
            self._generate_combinations(rule, condition_matches, 0, [])

    def _generate_combinations(
        self, rule: Rule, fact_lists: List[List[Fact]], index: int, current: List[Fact]
    ):
        """遞迴生成事實組合並激活規則。"""
        if index == len(fact_lists):
            # 檢查組合中沒有重複的事實（每個 fact id 都不同）
            fact_ids = [f.id for f in current]
            if len(set(fact_ids)) == len(current):
                self._activate_rule(rule, tuple(current))
            return

        for fact in fact_lists[index]:
            current.append(fact)
            self._generate_combinations(rule, fact_lists, index + 1, current)
            current.pop()

    def _activate_rule(self, rule: Rule, match: Tuple[Fact, ...]):
        """激活規則，加入議程（避免重複）。"""
        # 生成唯一鍵：規則名 + 事實 ID 排序
        fact_ids = sorted([f.id for f in match])
        key = f"{rule.name}:{fact_ids}"

        if key not in self.activated_combinations:
            self.activated_combinations.add(key)
            self.agenda.append((rule, match))
            self.agenda.sort(key=lambda x: -x[0].priority)

    def fire_all_rules(self) -> int:
        """執行議程中的所有規則，回傳執行次數。"""
        count = 0
        while self.agenda:
            rule, match = self.agenda.pop(0)
            for action in rule.actions:
                result = action(*match)
                if isinstance(result, Fact):
                    self.add_fact(result)
                    self.inferred_facts.append(result)
                    count += 1
        return count

    def fire_rule(self) -> bool:
        """執行議程中的一個規則。"""
        if not self.agenda:
            return False
        rule, match = self.agenda.pop(0)
        for action in rule.actions:
            result = action(*match)
            if isinstance(result, Fact):
                self.add_fact(result)
                self.inferred_facts.append(result)
        return True

    def run(self, max_iterations: int = 100) -> int:
        """執行推論直到沒有新事實或達到最大迭代次數。"""
        iteration = 0
        total = 0
        while iteration < max_iterations:
            count = self.fire_all_rules()
            if count == 0:
                break
            total += count
            iteration += 1
        return total

    def query_facts(self, pattern: Dict[str, Any]) -> List[Fact]:
        """查詢匹配模式的事實。"""
        return [f for f in self.facts if f.matches(pattern)]

    def clear(self):
        """清除所有事實和推論結果。"""
        self.facts.clear()
        self.agenda.clear()
        self.inferred_facts.clear()
        self.activated_combinations.clear()
        Fact._next_id = 0


def create_fact(**kwargs) -> Fact:
    """快速建立事實。"""
    return Fact(**kwargs)


__all__ = [
    "Fact",
    "Rule",
    "ReteEngine",
    "create_fact",
]
