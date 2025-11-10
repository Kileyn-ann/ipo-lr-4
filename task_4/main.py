import math #подключаем модуль math
import random
rand = [round(random.uniform(0,10),2)  for i in range(7)] #Создаём список чисел с 1 по 19
print(rand)
pow_l = [math.floor(num)  for num in rand]
print(pow_l) #Выводим ноовый список
