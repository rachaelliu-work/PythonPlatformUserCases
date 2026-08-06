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

    data = {
        "Temperature": 70
    }

    rules = [
        {"field": "Temperature", "operator": "=", "value": 70},
        {"field": "Temperature", "operator": ">", "value": 65},
        {"field": "Temperature", "operator": "<", "value": 80},
    ]

    for rule in rules:
        print(engine.match(data, rule))
