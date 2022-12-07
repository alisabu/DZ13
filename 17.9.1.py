spisok = input("Введите любые числа строго через пробел ")
spisok_l = [int(a) for a in spisok.split()]

num = int(input("Введите любое число, которое хотите добавить в последовательность: "))
if num % 1 == 0:
    spisok_l.append(num)
    print("Список до сортировки: ", spisok_l)

def my_sort(spisok_l):
    for i in range(len(spisok_l)):
        idx_min = i
        for j in range(i, len(spisok_l)):
            if spisok_l[j] < spisok_l[idx_min]:
                idx_min = j
        if i != idx_min:
            spisok_l[i], spisok_l[idx_min] = spisok_l[idx_min], spisok_l[i]
    return spisok_l

print("Последовательность после сортировки:", my_sort(spisok_l))

index = spisok_l.index(num)
if index == 0:
    print ('Введеное число наименьшее, его индекс = ', index)
elif index == len(spisok_l) - 1:
    print('Введено наибольшее число, его индекс =', index)
else:
    print('Индекс введеного числа', index, ', индекс предыдущего числа', index - 1, ', индекс следующего числа', index + 1)
