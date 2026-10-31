class C1:
    def __init__(self):
        self.name = 'john'


class C2(C1):
    def __init__(self):
        super().__init__()
        print('inited')

        print(self.name)

C2()