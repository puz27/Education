# метод быстрой сортировки
def speed_sort(data: list):
    if len(data) < 2:
        return data
    else:
        start = data[0]
        little = [i for i in data[1:] if start > i]
        bigger = [i for i in data[1:] if start < i]
        return speed_sort(little) + [start] + speed_sort(bigger)


data = [4, 1, 7, 2, 10]
print(speed_sort(data))


# вычисление факториала
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))


# вычисление суммы элементов списка
def summa(data: list):
    if data == []:
        return 0
    else:
        x = data.pop(0)
        return x + summa(data)


data = [4, 1, 7, 2, 10]
print(summa(data))


# вычисление количества элементов списка
def count(data: list):
    if data == []:
        return 0
    return 1 + count(data[1:])


data = [1, 2, 3, 4, 5]
print(count(data))


# вычисление максимального элемента массива
def bigger(data):
    if data == []:
        return 0
    else:
        if data[0] > bigger(data[1:]):
            return data[0]
        else:
            return bigger(data[1:])


data = [111, 22, 99, 55, 555]
print(bigger(data))
