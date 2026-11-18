

votes = input().split()

d = {}

for name in votes:
    if name in d:
        d[name] += 1
    else:
        d[name] = 1

for name in d:
    print(name + ":", d[name])

winner = list(d.keys())[0]
max_votes = d[winner]

for name in d:
    if d[name] > max_votes:
        max_votes = d[name]
        winner = name

print("Winner:", winner)