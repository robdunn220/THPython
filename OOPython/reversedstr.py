class ReversedStr(int):
    def __new__(*args, **kwargs):
        self = int.__new__(*args, **kwargs)
        return self


double_int = ReversedStr(5)
Double
print(double_int)
