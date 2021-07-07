def max_num(list):
    if len(list) == 1:
        return list[0]
    else:
        m = max_num(list[1:])
        return m if m > list[0] else list[0]


lista = [2,3,6,89,3,1]

resp = max_num(lista)

print(resp)