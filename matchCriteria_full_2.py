import operator

OPS = {
    "=": operator.eq,
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    # Custom operator
    "contains": lambda a, b: b in a,
    "icontains": lambda a, b: str(b).lower() in str(a).lower(),
    "startswith": lambda a, b: str(a).startswith(str(b)),
    "istartswith": lambda a, b: str(a).lower().startswith(str(b).lower()),
    "endswith": lambda a, b: str(a).endswith(str(b)),
    "iendswith": lambda a, b: str(a).lower().endswith(str(b).lower()),
    "in": lambda a, b: a in b,
    "not_in": lambda a, b: a not in b,
    "regex": lambda a, b: re.search(b, str(a)) is not None,
    "isnull": lambda a, b: a is None,
    "notnull": lambda a, b: a is not None,
    }

def evaluate(data, rule):
    if "and" in rule:
        return all(evaluate(data, r) for r in rule["and"])

    if "or" in rule:
        return any(evaluate(data, r) for r in rule["or"])

    field = rule["field"]
    op = rule["operator"]
    value = rule["value"]
    actual = data.get(field)
    if actual is None:
        return False
    if op not in OPS:
        raise ValueError(f"Unsupported operator: {op}")
    return OPS[op](actual,value)

if __name__ == "__main__":
    #data = {
    #        "hostname": 'abc.core.comcast.net',
    #    }
    
    #rule = {
    #    "field": "hostname",
    #    "operator": "contains",
    #    "value": "CORE"
    #}
    #print(evaluate(data, rule))

    #data = {
    #    "Temperature": 70,
    #    "Humidity": 50,
    #    "Pressure": 980
    #}

    data = [
            {"Temperature": 70,
             "Humidity": 50,
             "Pressure": 980},
            {"Temperature": 60,
              "Humidity": 50,
              "Pressure": 980},
            {"Temperature": 80,
             "Humidity": 50,
            "Pressure": 980}
         ]

    rule = {
        "and": [
            {"field": "Temperature", "operator": ">=", "value": 65},
              {
                "or": [
                        {"field": "Humidity", "operator": "<", "value": 60},
                        {"field": "Pressure", "operator": ">", "value": 1000},
                      ]

              }
        ]
    }
    
    matches = [item for item in data if evaluate(item, rule)]
    print(matches)
    for item in data: 
        print(evaluate(item, rule))