text = ['Каждый человек раб. Даже',
        'Если король. Даже',
        'Если не признается в этом самому себе. Потому',
        'Что каждый почти каждый в глубине души жаждет хозяина. Вождя',
        'Ли, князя, волхва или бога, который следил бы за каждым его шагом и без воли которого волос бы не упал. И',
        'Чем всемогущее бог, тем лучше. Человек',
        'Ропщет на хозяина, но постоянно его ищет.']
tr = '1'
a = text

def glassoglas(b):
    max = 0
    maxtemp = 0
    a3 = 'аяуюэеёоиы'
    a5 = 'бвгджзйклмнпрстфхцчшщ'
    for i in range(len(b)):
        b = b.lower()
    if b[0] in a3:
        if len(b) % 2 == 1:
            if len(b) == 1:
                max = 0
            else:
                for j in range(1, len(b) - 1, 2):
                    if b[j] in a5 and b[j + 1] in a3:
                        maxtemp += 1
                if maxtemp == len(b) // 2:
                    max = 1
        else:
            for j in range(1, len(b) - 1, 2):
                if b[j] in a5 and b[j + 1] in a3:
                    maxtemp += 1
            if b[len(b) - 1] in a5:
                maxtemp += 1
            if maxtemp == len(b) // 2:
                max = 1
    elif b[0] in a5:
        if len(b) % 2 == 1:
            if len(b) == 1:
                max = 0
            else:
                for j in range(1, len(b) - 1, 2):
                    if b[j] in a3 and b[j + 1] in a5:
                        maxtemp += 1
                if maxtemp == len(b) // 2:
                    max = 1
        else:
            for j in range(1, len(b) - 1, 2):
                if b[j] in a3 and b[j + 1] in a5:
                    maxtemp += 1
            if b[len(b) - 1] in a3:
                maxtemp += 1
            if maxtemp == len(b) // 2:
                max = 1
    return max

def choice4(text):
    a0 = []
    a10 = ''
    a1 = 'аяуюэеёоиыбвгджзйклмнпрстфхцчшщьъ'
    a2 = 'АЯУЮЭЕЁОИЫБВГДЖЗЙКЛМНПРСТФХЦЧШЩЬЪ'
    for j in range(len(a)):
        temp = str(a[j])
        for i in range(len(a[j])):
            if temp[i] in a1 or temp[i] in a2:
                a10 += temp[i]
            else:
                a0.append(a10)
                a10 = ''
            if i == len(a[j]) - 1:
                a0.append(a10)
                a10 = ''
    while '' in a0:
        a0.remove('')
    q = []
    for i in range(len(a0) - 1):
        q.append(glassoglas(a0[i]) and glassoglas(a0[i + 1]))
    max = 0
    maxtemp = 0
    for i in range(len(q)):
        if q[i] == 1:
            maxtemp += q[i]
        elif q[i] == 0:
            if max < maxtemp:
                max = maxtemp
            maxtemp = 0
    return max+1

def f1():
    slc = sl.capitalize()
    reslc = resl.capitalize()
    for i in range(len(text)):
        text[i] = text[i].split()
        for j in range(len(text[i])):
            if not text[i][j].isalpha():
                q = text[i][j][-1:]
                text[i][j] = text[i][j][:-1]
            else:
                q = ''
            if text[i][j] == sl:
                text[i][j] = resl
            elif text[i][j] == slc:
                text[i][j] = reslc
            text[i][j] += q
        text[i] = ' '.join(text[i])
        f3()


def f3():
    wi = max([len(i) for i in text])
    for i, g in enumerate(text):
        g = g.split()
        g = ' '.join(g)
        text[i] = g
        if tr == '2':
            text[i] = g.rjust(wi, ' ')
        elif tr == '3':
            sr = len(g)
            g = g.split()
            coun = len(g) - 1
            tab = (wi - sr) // coun + 1
            ost = (wi - sr) % coun
            val = g[0]
            for j in range(1, coun + 1):
                val += (' ' * (tab + int(ost >= j)) + g[j])
            text[i] = val

while 1:
    print('\n'.join(text), '\nМеню:', '1. Удалить заданное слово во всем тексте.',
          '2. Произвести замену одного слова на другое во всем тексте.',
          '3. Выравнивание текста.', '4. Определить максимальное кол-во слов подряд с чередованием гласных и согласных', '5. Выйти.\n', sep='\n')
    n = input('Опция №')
    if n == '1':
        print()
        sl = input('Введите слово, которое надо удалить: \n')
        resl = ''
        f1()
        print()
    elif n == '2':
        print()
        sl = input('Введите слово, которое надо заменить: \n')
        print()
        resl = input('Введите слово, на которое надо заменить: \n')
        f1()
        print()
    elif n == '3':
        while 1:
            print()
            print('1. По левому краю', '2. По правому краю', '3. По ширине',
                  sep='\n')
            print()
            tr = input('Подопция №')
            print()
            if not len(tr) - 1 and tr in '123':
                f3()
                break
            else:
                print('Выберите правильное действие')
    elif n == '4':
        print()
        print('Максимальное кол-во слов, удовлетворяющих условию: ', choice4(text))
        print()
    elif n == '5':
        break
    else:
        print('Введено неправильное значение!\n')
