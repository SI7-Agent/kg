import os

f1 = open('1.txt', 'r')
f2 = open('2.txt', 'r')
print(os.path.exists('3.txt'))
if os.path.exists('3.txt'):
    open('3.txt', 'w').close()

def cr_txt(string):
    if os.path.exists('3.txt'):
        f3 = open('3.txt', 'a+')
    else:
        f3 = open('3.txt', 'w')
    f3.write(str(string) + ' ')

def check2(num):
    fib0 = 0
    fib1 = 1
    fibs = 0
    while fibs < num:
        fibs = fib0 + fib1
        fib0 = fib1
        fib1 = fibs
    if fibs == num:
        return 1
    else:
        return 0

dict = {}
count1 = 0
max = 0

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
        else:
            if flag1 >= 1:
                flag -= 1
                tmp *= 10**flag
                count = tmp
                if count not in dict.values():
                    dict[count1] = round(count)
                    count1 += 1
                flag1 = 0
                tmp = 0
            flag = 0
            if count >= max:
                max = count

for i in f2:
    count = 0
    flag = 0
    flag1 = 0
    tmp = 0
    for g in range(len(i)):
        if i[g].isdigit():
            tmp += float(i[g]) * float(((0.1) ** flag))
            flag += 1
            flag1 += 1
        else:
            if flag1 >= 1:
                flag -= 1
                tmp *= 10 ** flag
                count = tmp
                if count not in dict.values():
                    dict[count1] = round(count)
                    count1 += 1
                flag1 = 0
                tmp = 0
            flag = 0
            if count >= max:
                max = count

max = int(round(max))

for i in range(max+1):
    for key, item in dict.items():
        if (i == item and check2(item) == 1):
            cr_txt(item)
            continue

f3 = open('3.txt', 'r')
for i in f3:
    print(i)