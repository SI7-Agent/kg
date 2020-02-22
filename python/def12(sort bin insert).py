print('Введите массив данных через пробел: ')
n = 1
while n == 1:
    try:
        mas = list(map(float, input().split()))
        def binar_vstavka(mas):
            n = len(mas)
            for i in range(1, n):
                if mas[i - 1] > mas[i]:
                    x = mas[i]
                    left = 0
                    right = i - 1
                    while True:
                        sr = (left + right) // 2
                        if mas[sr] < x:
                            left = sr + 1
                        else:
                            right = sr - 1
                        if left > right:
                            break
                    j = i - 1
                    while j >= left:
                        mas[j + 1] = mas[j]
                        j -= 1
                    mas[left] = x
            return mas

        mas_res = ' '.join(map(str, binar_vstavka(mas)))
        print('\nОтсортированный массив: ')
        print(mas_res)
        n = 0
    except:
        print('Ошибка! Повторите попытку')
        n = 1