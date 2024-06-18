'''number = 1 # целое число int()
number_float= 2.5 # число с плавающей точкой float()
chislo = 2
print(id(number))
number = number + 1
print(id(number))
print(id(number_float))

name_stroka = 'Привет всем курсантам' # str()
print(id(name_stroka))

name_stroka = name_stroka + ' 1' + ' потока!'
print(id(name_stroka))

print('Лабрадор','это собака!','самая добрая', sep ='',end = '*')
print(name_stroka) # над строками работают 2 математические операции + *'''

stroka = 'GhfhGGHFkYUEWDnbcjd'
print(stroka.replace(' ','g'))

spisok = [True, 1,2,'56'] #list
print('G' in stroka)
print(type(spisok))

corteg = (True, 1,2,'56')
print(type(corteg))
print(corteg)

slovar = {'Denis':1988,
          'Nikola':1988}
slovar[0] = 2001
print(type(slovar))

mnogestvo = {1,1,1,1,2,2,3,3,3,4,4,5,5,6,78,8,}
print(type(mnogestvo))





