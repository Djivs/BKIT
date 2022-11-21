# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, ignore_case = False, **kwargs):
        self.ignore_case = ignore_case
        self.data = items
        self.occured = set()
        self.index = -1

        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        pass

    def __next__(self):
        # Нужно реализовать __next__
        while True:
            self.index += 1
            if self.index >= len(self.data):
                raise StopIteration
            if self.check():
                current = self.data[self.index]
                self.occured.add(current)
                return current
        pass

    def __iter__(self):
        return self

    def check(self):
        el = self.data[self.index]
        if self.ignore_case:
            if type(el) == str:
                return not((el.lower() in self.occured) or (el.upper() in self.occured))
            else:
                return not(el in self.occured)
        else:
            return not(el in self.occured)
        pass


# def main():
#     for i in Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']):
#         print(i)

# main()