n = int(input())
while len(set(str(n+1))) != 4:
    n += 1
print(n+1)