# 2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
import timeit


# использование решето Эратосфена
def funk_eratosfen(n):
    n = n - 1
    size = 10 * n
    a = [0] * size
    for i in range(size):
        a[i] = i

    a[1] = 0

    m = 2
    while m < size:
        if a[m] != 0:
            j = m * 2
            while j < size:
                a[j] = 0
                j = j + m
        m += 1

    b = []

    for i in a:
        if a[i] != 0:
            b.append(a[i])

    for i, item in enumerate(b):
        if i == n:
            return item


print(timeit.timeit('funk_eratosfen(10)', number=100, globals=globals()))  # 0.003001300000000002
print(timeit.timeit('funk_eratosfen(100)', number=100, globals=globals()))  # 0.031821199999999994
print(timeit.timeit('funk_eratosfen(1000)', number=100, globals=globals()))  # 0.37195
print(timeit.timeit('funk_eratosfen(1000)', number=100, globals=globals()))  # 0.3886974
print(timeit.timeit('funk_eratosfen(10000)', number=100, globals=globals()))  # 4.4945505

print('-' * 50)


# не используя решето

def isprime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def funk_not_eratosfen(n):
    n = n + 1
    size = 10 * n
    a = [0] * size
    for i in range(size):
        a[i] = i

    a[1] = 0

    b = []
    for i, item in enumerate(a):
        if isprime(i) == True:
            b.append(item)

    for i, item in enumerate(b):
        if i == n:
            return item


print(timeit.timeit('funk_not_eratosfen(10)', number=100, globals=globals()))  # 0.004571300000000056
print(timeit.timeit('funk_not_eratosfen(100)', number=100, globals=globals()))  # 0.06911260000000008
print(timeit.timeit('funk_not_eratosfen(1000)', number=100, globals=globals()))  # 1.3530045

# нахождение просто числа быстрее через использование решето Эратосфена
