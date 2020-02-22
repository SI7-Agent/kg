a = str(input('Введите строку слов/символов: '))
q = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
q1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
a10 = []
a0temp = []
temp = ''
for i in range(len(a)):
    if a[i] in q or a[i] in q1:
        temp += a[i]
    elif a[i] not in q or a[i] not in q1:
        a10.append(temp)
        temp = ''
if a[len(a) - 1] in q or a[len(a) - 1] in q1:
    a10.append(temp)
while '' in a10:
    a10.remove('')
for i in range(len(a10)):
    temp0 = 0
    temp = a10[i].lower()
    for j in range(len(temp)):
        if temp.count(temp[j]) > 1:
            temp0 += 1
    if temp0 == len(temp):
        a0temp.append(a10[i])
a0temp = sorted(a0temp)
print()
print(', '.join(a10), '\n')
print('Слова, удовлетворяющие выданному условию:', '\n')
for i in range(len(a0temp)):
    print(a0temp[i])
