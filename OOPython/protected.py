class Protected:
    __name = 'Security'

    def __method(self):
        return self.__name


a = Protected()
print(a._Protected__method())
