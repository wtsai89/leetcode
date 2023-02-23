from collections import defaultdict

a = [1,2,3,4,5]

for i in a[:2] + a[3:]:
    print(i)