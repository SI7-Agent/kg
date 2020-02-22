import pickle
with open('qwe.bin', 'rb') as f:
    d = pickle.load(f)
search = 'g'
search1 = 'G'
count = 0
d0 = {}
d1 = d[0]
for i in range(len(d1)):
    print(d1[i], end=' ' * 10)
print()
nums = []

for i in range(1, len(d)):
    for key, item in d[i].items():
        if search in item or search1 in item:
            nums.append(i)

for i in range(1, len(d)):
    if i not in nums:
        d0 = dict(d[i])
        for j in d0.keys():
            if len(j) > len(d0.get(j)):
                print(d0.get(j), end=' ' * (abs((len(j) - len(d0.get(j)))) + 10))
            else:
                print(d0.get(j), end=' ' * (12 - len(d0.get(j))))
        print()