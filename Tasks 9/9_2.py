glsn = ['а', 'о', 'у', 'ы', 'я', 'ё', 'ю', 'и', 'е', 'э']
s = list(input())
slova = input().split()
res = []
res2 = []

for i in range(len(s)):
    if s[i] in glsn:
        s_index = i
        res.append(s_index)
        res = sorted(res)

for slov in slova:
    for b in range(len(slov)):
        if slov[b] in glsn:
            s2_index = b
            res2.append(s2_index)
    if res == res2:
        print(slov, end= ' ')
    res2 = []
