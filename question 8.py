

n = int(input())

d = {}

for i in range(n):
    country, capital = input().split()
    d[country] = capital

search = input()

if search in d:
    print(d[search])
else:
    print("Not found")
    