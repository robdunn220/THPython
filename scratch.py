class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        morse = []
        for value in self.pattern:
            if value == '.':
                morse.append('dot')
            elif value == '_':
                morse.append('dash')

        return "-".join(morse)


class S(Letter):
    def __init__(self):
        pattern = ['.', '_', '.', '_', '.', '.']
        super().__init__(pattern)


ptrn = S()
print(ptrn.__str__())
