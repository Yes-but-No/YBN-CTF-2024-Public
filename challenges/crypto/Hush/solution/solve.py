data = ([85, 118, 80, 163, 121, 121, 123, 123, 86, 126, 86, 89, 128, 89, 53, 132, 93, 56, 134, 58, 59, 60, 137, 135, 89, 89, 143, 105, 67, 67, 108, 69, 146, 92, 87, 113, 113, 74, 74], ['0', '_', 'N', '}', 'p', 'h', 'h', '_', 'H', 'h', '5', 'Y', '{', ':', '2', 'u', '?', '4', 'l', '3', '3', '1', 'u', 'l', '9', '7', 'w', '_', 'B', '7', '_', '5', 'u', '9', '3', 'k', '_', '5', '1'])

result = []
for i, j in zip(data[0], data[1]):
    result.append((i-ord(j), j))

result = sorted(result)
for char in result:
    print(char[1], end="")