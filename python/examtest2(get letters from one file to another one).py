import os

f1 = open('11.txt', 'r')
if os.path.exists('22.txt'):
    open('22.txt', 'w').close()

def cr_txt(stri):
    if os.path.exists('22.txt'):
        f2 = open('22.txt', 'a+')
    else:
        f2 = open('22.txt', 'w')
    for i in stri:
        if i.isalpha():
            f2.write(i)
        elif i == '\n':
            f2.write(i)

dict = {}
def sort_():
    f1 = open('11.txt', 'r')
    for i in f1:
        count = 0
        flag = 0
        flag1 = 0
        tmp = 0
        for g in range(len(i)):
            if i[g].isdigit():
                tmp += float(i[g])*float(((0.1)**flag))
                flag += 1
                flag1 += 1
            elif i[g].isdigit()==0:
                if flag1 >= 1:
                    flag -= 1
                    tmp *= 10**flag
                    count += tmp
                    flag1 = 0
                    tmp = 0
                flag = 0
        dict[i] = round(count)
    return dict

max = 0
dict2 = sort_()
for i in dict2.values():
    if i >= max:
        max = i
print(dict)
dict1 = {}

for i in range(1, max + 1):
    for key, item in dict.items():
        if item == i:
            dict1[i] = key

print(dict1)
n = 0
for i in f1:
    if i.isupper() == 1:
        cr_txt(i)
    else:
        cr_txt(list(dict1.values())[n])
        n += 1

print()
f2 = open('22.txt', 'r')
for i in f2:
    print(i, end = '')