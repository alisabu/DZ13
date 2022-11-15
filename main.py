

import re
s = input("Введите ставки банков")
m = int(input ("Введите сумму"))
a = 1
nums = re.findall(r'\d*\.\d+|\d+', s)
for i in range(a):
   nums = [float(i) for i in nums]
   deposit = [m // 100 * i for i in nums]
   max_number = int(max(deposit))
   print ("Максимальная заработанная сумма", max_number)
