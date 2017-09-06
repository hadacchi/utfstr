class utfstr(str):
    def __len__(self):
        return super().__len__() + (super().__str__().encode('utf-8').__len__() - super().__str__().__len__())//2

