a = list(input('Шифруемая фраза: '))
b = list(input('Ключ шифрования: '))
c = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
c0 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

eng0 = 'abcdefghijklmnopqrstuvwxyz'
eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(b)):
    if b[i] in c0:
        b[i] = c[c0.index(b[i])]

    if b[i] in eng0:
        b[i] = eng[eng0.index(b[i])]

    for j in range(i, len(a), len(b)):
        print(a[j])
        if a[j] in c:
            f = c.index(b[i]) + c.index(a[j])
            if f > 32:
                a[j] = c[f - 32]
            else:
                a[j] = c[f]

        elif a[j] in c0:
            f = c.index(b[i]) + c0.index(a[j])
            if f > 32:
                a[j] = c0[f - 32]
            else:
                a[j] = c0[f]

        elif a[j] in eng:
            f = eng.index(b[i]) + eng.index(a[j])
            if f > 25:
                a[j] = eng[f - 25]
            else:
                a[j] = eng[f]

        elif a[j] in eng0:
            f = eng.index(b[i]) + eng0.index(a[j])
            if f > 25:
                a[j] = eng0[f - 25]
            else:
                a[j] = eng0[f]
print()
for i in range(len(a)):
    print(a[i], end = '')