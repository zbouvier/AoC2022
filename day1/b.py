
# with open('b.txt') as f:
#     lines = f.read().splitlines()
# cur = -1
# inc = 0  
# dictionary = {}
# for n in lines:
#     n = n.split(" ")
#     val = int(n[0])
#     for thing in n[1:]:
#         if thing != "":
#             if thing in dictionary:
#                 dictionary[thing]+=val
#             else:
#                 dictionary[thing] = val
                
# cur = -1 
# inc = 0
# for thing in dictionary:
#     if cur == -1:
#         cur = dictionary[thing]
#     else:
#         if dictionary[thing] > cur:
#             inc+=1
#             cur = dictionary[thing]
#         else:
#             cur = dictionary[thing]
with open('b.txt') as f:
    lines = f.read().splitlines()
cur = -1
inc = 0  
new_inc = []
for i, n in enumerate(lines):
    n = int(n)
    if len(lines) - i > 2:
        new_inc.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))
        
for thing in new_inc:
    if cur == -1:
        cur = thing
    else:
        if thing > cur:
            inc+=1
            cur = thing
        else:
            cur = thing
print(inc)