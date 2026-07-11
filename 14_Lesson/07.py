dictionary = {
    'hello': 'salam',
    'apple': 'alma',
    'lemon': 'limon',
    'cat': 'pisik',
    'dog': 'it',
    'Flag': 'baydak',
    'student': 'okuwcy',
    'family': 'masgala',
    'pen': 'ruçka',
    'water': 'suw',
    'bread': 'görek'
}

b = {}
for i, j in dictionary.items():
    b.setdefault(j, i)
for x, y in b.items():
    print(f"{x} - {y}")