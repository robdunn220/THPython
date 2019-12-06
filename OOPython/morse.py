class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    @classmethod
    def from_string(cls, string):
        no_hyphen = []
        for x in string.split('-'):
            if x == 'dot':
                no_hyphen.append('.')
            else:
                no_hyphen.append('_')
        return no_hyphen


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '_']
        super().__init__(pattern)


s = S()
print(Letter.from_string(str(s)))
