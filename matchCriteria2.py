import operator

class MatchingEngine:
    OPERATORS = {
        "=": operator.eq,
        "==": operator.eq,
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "!=": operator.ne,
    }
    def match(self, data, rule):
        field = rule["field"]
        op = rule["operator"]
        expected = rule["value"]

        if field not in data:
            return False

        actual = data[field]

        if op not in self.OPERATORS:
            raise ValueError(f"Unsupported operator: {op}")

        return self.OPERATORS[op](actual, expected)

if __name__ == "__main__":
    engine = MatchingEngine()

    data = [
        {"Temperature": 70},
        {"Temperature": 60},
        {"Temperature": 80}
    ]

    rule = {
        "field": "Temperature",
        "operator": ">=",
        "value": 70
        }
    engine = MatchingEngine()
    matches = [item for item in data if engine.match(item, rule)]
    print(matches)
