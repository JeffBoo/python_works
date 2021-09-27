a = int(input("a :"))
k = 0
p = 1 # on veille à avoir constamment p = 2**k
while p < a:
    p = p * 2
    k = k + 1
print("k: ", k, "2^k: ", p)