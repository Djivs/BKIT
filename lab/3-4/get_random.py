import random
# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки
def gen_random(num_count, begin, end):
    assert begin < end
    assert num_count >= 0

    for i in range(num_count):
        yield random.randint(begin, end)
    # Необходимо реализовать генератор

gen1 = gen_random(1, 2, 3)
gen2 = gen_random(3, 5, 25)

for i in gen1:
    print(i, end=' ')
print()

for i in gen2:
    print(i, end=' ')
