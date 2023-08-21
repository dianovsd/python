# Вводим два числа
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Вводим операцию
op = input("Введите операцию (+, -, *, /): ")

# Вычисляем и выводим результат
if op == "+":
  result = num1 + num2
elif op == "-":
  result = num1 - num2
elif op == "*":
  result = num1 * num2
elif op == "/":
  if num2 != 0:
    result = num1 / num2
  else:
    result = "Ошибка: деление на ноль"
else:
  result = "Ошибка: неверная операция"

print(f"Результат: {result}")
