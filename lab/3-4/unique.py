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
        if self.ignore_case:
            while True:
                self.index += 1
                if self.index >= len(self.data):
                    raise StopIteration
                current = self.data[self.index]
                if type(current) == str:
                    if not ((current.lower() in self.occured) or (current.upper() in self.occured)):
                        self.occured.add(current)
                        return current
                else:
                    if not (current in self.occured):
                        self.occured.add(current)
                        return current
        else:
            while True:
                self.index += 1
                if self.index >= len(self.data):
                    raise StopIteration
                current = self.data[self.index]
                if not (current in self.occured):
                    self.occured.add(current)
                    return current
        pass

    def __iter__(self):
        return self

# def main():
#     for i in Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'], True):
#         print(i)

# main()