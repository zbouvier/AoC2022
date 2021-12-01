with open('a.txt') as f:
    lines = f.read().splitlines()
cur = -1
inc = 0  
for n in lines:
    n = int(n)
    print(n)
    if cur == -1:
        print("ree")
        cur = n
    else:
        if n > cur:
            inc+=1
            cur = n
        else:
            cur = n
print(inc)
