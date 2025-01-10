#Завдання на один простий цикл while/for:
#1. Обчислити суму чисел в діапазоні від 1 до 10 циклом.
start = 0
variable = 1
while variable <= 10:
    start += variable
    variable += 1
print(start)
    
#2. Обчислити суму чисел в діапазоні від 1 до 10 циклом.
celsius = 0
fahrenheit = 32
while celsius <= 50:
    fahrenheit = (celsius * 9/5) + 32
    print(celsius ,"-", fahrenheit)
    celsius += 1

#4. Написати програму, яка обчислює факторіал введеного числа.
x = int(input("Введіть число: "))
factorial = 1
while x > 1:
    factorial *= x
    x -= 1
print("Факторіал числа: ", factorial)

#6. З клавіатури вводиться ціле число. Вивести на екран всі числа, на які введене число ділиться без залишку.
x = int(input("Введіть ціле число: "))
for y in range(1, x + 1):
    if x % y == 0:
        print(y)

#9. Визначити, чи є введене число паліндромом. Паліндром — це число, яке однаково читається як зліва направо, так і справа наліво, наприклад, 1234321. У цьому завданні (як і в інших завданнях) не можна використовувати рядки та списки.
def is_palindrome(number):
    original_number = number 
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
    return original_number == reversed_number
number = int(input("Введіть число: "))
if is_palindrome(number):
    print(f"Число {number} - паліндром.")
else:
    print(f"Число {number} не паліндром.")

#Завдання на псевдографіку:
#1. Показати на екрані рівнобедрений трикутник висотою N.
import os
os.system('cls')
N = int(input("Введіть висоту трикутника: "))
for y in range(1, N + 1):
        spaces = N - y
        stars = 2 * y - 1
        print(" " * spaces + "*" * stars)

#2. Написати програму, яка виводить на екран ромб.
import os
os.system('cls')
height = 5
for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
for i in range(height - 2, -1, -1):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

#Завдання на вкладені цикли:
#1. Написати програму, що показує таблицю множення (таблиця Піфагора).
def print_multiplication_table(n = 10):
    for x in range(1, n + 1):  
        for y in range(1, n + 1): 
            print(x * y, end=" ") 
        print()
print_multiplication_table(10)

#4. Написати програму, яка виводить на екран всі прості числа в діапазоні від 2 до 10.000.000.
def is_prime(num):
   if num < 2:
       return False
   for i in range(2, int(num ** 0.5) + 1):
       if num % i == 0:
        return False
   return True
a = 2
b = 10000000
for num in range(a, b + 1):
   if is_prime(num):
       print(num)