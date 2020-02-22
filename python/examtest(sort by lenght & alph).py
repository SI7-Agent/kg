f = open('test.txt', 'r')

def sort_str(i):
    global flag
    flag = 0
    d = {}
    tmp = ''
    for g in range(len(i)):
        if i[g].isalpha() == True:
            tmp += i[g]
        if i[g].isalpha() == False:
            d[tmp] = len(tmp)
            if len(tmp) >= flag:
                flag = len(tmp)
            tmp = ''
    if tmp != str(''):
        d[tmp] = len(tmp)
    while '' in d:
        d.pop('')

    return d

for i in f:
    print(sort_str(i))
    string = ''
    dic = sort_str(i)
    for g in range(flag+1):
        for key, item in dic.items():
            if item == g:
                string += key + ' '
                continue
    print(string)
