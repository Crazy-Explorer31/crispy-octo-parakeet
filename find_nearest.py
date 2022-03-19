import datetime
separator = input('Введите разделитель ')
dates = [datetime.datetime(*(list(map(int, i.split(separator)))[::-1])) for i in input().split()]
alpha = datetime.datetime(1956, 4, 10)
res = dates[[abs((temp_date - alpha).days) for temp_date in \
    dates].index(min([abs((temp_date - alpha).days) for temp_date in dates]))]
def formalization(n):
    if len(str(n)) < 2:
        return '0' + str(n)
    else:
        return n
print(formalization(res.day), formalization(res.month), formalization(res.year), sep = '/')
input('Press enter to exit ')
