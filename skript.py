r = int(input ("Введите количество билетов"))
itog = 0
for i in range(r):
    age = int(input ("Введите возраст"))
    if age < 18:
        itog= itog+0
    elif 18<=age<25:
        itog=itog+990
    else:
        itog= + 1390
    if r>=3:
        itog=int(itog*0.9)
print (itog)
