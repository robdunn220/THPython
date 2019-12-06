class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        output = []
        iter_object = self.__iter__()
        for blip in iter_object:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    def __iter__(self):
        yield from self.pattern


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '_', '.']
        super().__init__(pattern)


s = S()
print(s.__str__())


