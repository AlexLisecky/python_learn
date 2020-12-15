#1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
#Примечание. Идеальным решением будет:
# выбрать хорошую задачу, которую имеет смысл оценивать,
# написать 3 варианта кода (один у вас уже есть),
# проанализировать 3 варианта и выбрать оптимальный,
# результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# написать общий вывод: какой из трёх вариантов лучше и почему.

import random
import timeit
import cProfile

def funk_for(n):
    array_idx_FOR = []
    idx = 0
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]

    for i in array:
        if i % 2 == 0:
            array_idx_FOR.append(idx)
        idx += 1
    return array_idx_FOR

print(timeit.timeit('funk_for(10)',number=100,globals=globals())) # 0.0008887999999999986
print(timeit.timeit('funk_for(100)',number=100,globals=globals())) # 0.008097300000000002
print(timeit.timeit('funk_for(1000)',number=100,globals=globals())) #0.08381050000000001
print(timeit.timeit('funk_for(10000)',number=100,globals=globals())) # 0.8607707

cProfile.run('funk_for(100000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.217    0.217 <string>:1(<module>)
#    100000    0.060    0.000    0.132    0.000 random.py:200(randrange)
#    100000    0.032    0.000    0.164    0.000 random.py:244(randint)
#    100000    0.049    0.000    0.072    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.018    0.018    0.217    0.217 work_1.py:13(funk_for)
#         1    0.029    0.029    0.194    0.194 work_1.py:18(<listcomp>)
#         1    0.000    0.000    0.217    0.217 {built-in method builtins.exec}
#     50620    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
#    100000    0.009    0.000    0.009    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    126553    0.014    0.000    0.014    0.000 {method 'getrandbits' of '_random.Random' objects}

print('-' * 50)


def funk_enumerate(n):
    array_idx_ENUMERATE = []
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]

    for i, item in enumerate(array):
        if item % 2 == 0:
            array_idx_ENUMERATE.append(i)
    return array_idx_ENUMERATE

print(timeit.timeit('funk_enumerate(10)',number=100,globals=globals())) # 0.0008835999999998734
print(timeit.timeit('funk_enumerate(100)',number=100,globals=globals())) # 0.00788549999999999
print(timeit.timeit('funk_enumerate(1000)',number=100,globals=globals())) # 0.08048370000000005
print(timeit.timeit('funk_enumerate(10000)',number=100,globals=globals())) # 0.8739952

cProfile.run('funk_enumerate(100000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.203    0.203 <string>:1(<module>)
#    100000    0.056    0.000    0.124    0.000 random.py:200(randrange)
#    100000    0.032    0.000    0.156    0.000 random.py:244(randint)
#    100000    0.046    0.000    0.069    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.014    0.014    0.202    0.202 work_1.py:49(funk_enumerate)
#         1    0.028    0.028    0.184    0.184 work_1.py:53(<listcomp>)
#         1    0.000    0.000    0.203    0.203 {built-in method builtins.exec}
#     50389    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#    100000    0.009    0.000    0.009    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    126755    0.013    0.000    0.013    0.000 {method 'getrandbits' of '_random.Random' objects}

print('-' * 50)



def funk_while(n):
    array_idx_WHILE = []
    idx = 0
    i = 0
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]

    while n > 0:
        if array[i] % 2 == 0:
            array_idx_WHILE.append(idx)
        i += 1
        idx += 1
        n -= 1

    return array_idx_WHILE


print(timeit.timeit('funk_while(10)', number=100, globals=globals())) # 0.0009645000000000348
print(timeit.timeit('funk_while(100)',number=100,globals=globals())) # 0.008858699999999997
print(timeit.timeit('funk_while(1000)',number=100,globals=globals())) # 0.12709110000000012
print(timeit.timeit('funk_while(10000)',number=100,globals=globals())) # 1.0191137000000001

cProfile.run('funk_while(100000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.236    0.236 <string>:1(<module>)
#    100000    0.061    0.000    0.134    0.000 random.py:200(randrange)
#    100000    0.036    0.000    0.170    0.000 random.py:244(randint)
#    100000    0.049    0.000    0.073    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.031    0.031    0.235    0.235 work_1.py:84(funk_while)
#         1    0.030    0.030    0.200    0.200 work_1.py:90(<listcomp>)
#         1    0.000    0.000    0.236    0.236 {built-in method builtins.exec}
#     50273    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#    100000    0.010    0.000    0.010    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    126809    0.014    0.000    0.014    0.000 {method 'getrandbits' of '_random.Random' objects}


# Использование for и enumerate быстрее чем через цикл while судя по графику
