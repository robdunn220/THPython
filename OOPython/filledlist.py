import copy


class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))

    def __len__(self):
        return super(FilledList, self).__len__() + 2


fl = FilledList(3, 2)
print(len(fl))
