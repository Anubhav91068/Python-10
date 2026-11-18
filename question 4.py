

word = input()

d = {}

for ch in word:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)