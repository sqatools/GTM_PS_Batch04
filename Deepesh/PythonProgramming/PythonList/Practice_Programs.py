input_list = [1, 'a', [1, "b"], ('a', 3, 8), {"a": "7"}, {1, 2, 34}]

addition = 0

for val in input_list:
    if isinstance(val, int):
        addition = addition + val
    elif isinstance(val, list):
        for v2 in val:
            if isinstance(v2, int):
                addition += v2

    elif isinstance(val, tuple):
        for v3 in val:
            if isinstance(v3, int):
                addition += v3

    elif isinstance(val, dict):
        for v4 in val:
            if isinstance(v4, int):
                addition += v4

    elif isinstance(val, set):
        for v5 in val:
            if isinstance(v5, int):
                addition += v5

print("addition of int values :", addition)
