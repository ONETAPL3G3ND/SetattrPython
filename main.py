class Base:
    _fields = []
    def __init__(self, *args):
        for name, value in zip(self._fields, args):
                setattr(self, name, value)


class Stock(Base):
    _fields = ["name", "shares", "price"]


if __name__ == "__main__":
    a = Stock(1, 2 ,3)
    print(a.name)
