"""l = str(input("unos: "))

l = list(l)

l1 = []

l2 = []

l3 = []

brj = ""

for i in range (0,len(l)-1):
    for j in range (len(l)-1,0,-1):
        if j > i:
            if (l[i] == l[j] and l[i+1] == l[j-1]) and i != j:
                if l1[::-1] == l1:
                    brj = brj + l[i]
                    break

        elif j < i:
            if (l[i] == l[j] and l[i - 1] == l[j + 1]) and i != j:
                if l2[::-1] == l2:
                    brj = brj + l[i]
                    break

        else:
            if l[i+1] == l[i-1]:
                brj = brj + l[i]
                break
print(brj)
"""
