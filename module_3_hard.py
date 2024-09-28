data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    sum = 0

    if isinstance(data, (int, float)):
        sum += data
    elif isinstance(data, str):
        sum += len(data)
    elif isinstance(data, dict):
        for a, b in data.items():
            sum += calculate_structure_sum(a)
            sum += calculate_structure_sum(b)  
    elif isinstance(data, (list, tuple, set)):
        for i in data:
            sum += calculate_structure_sum(i)
    return sum

result = calculate_structure_sum(data_structure)
print(result)                     