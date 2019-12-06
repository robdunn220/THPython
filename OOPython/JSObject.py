class JSObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)


js_dict = JSObject({'smoob': 'smebly'})
print(js_dict.smoob)
