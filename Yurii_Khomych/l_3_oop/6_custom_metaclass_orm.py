class Field:
    class Base:
        pass

    class Int(Base):
        pass

    class String(Base):
        pass


class LittleORMMeta(type):
    def __new__(cls, name, bases, cls_dict):

        fields = []
        for fname, tp in cls_dict.items():
            try:
                if issubclass(tp, Field.Base):
                    fields.append(fname)
            except TypeError:
                pass

        cls_dict["_fields"] = fields

        return super(LittleORMMeta, cls).__new__(cls, name, bases, cls_dict)

    def __lshift__(self, fields):
        self.insert(**fields)


class Table(metaclass=LittleORMMeta):
    @classmethod
    def execute(cls, request):
        print(request)

    @classmethod
    def insert(cls, **fields):
        insert_request = (
            f"insert into {cls.__name__} ({','.join(cls._fields)}) "
            f"values ({','.join(repr(fields[fname]) for fname in cls._fields)})"
        )
        cls.execute(insert_request)


class MyTable(Table):
    rec_id = Field.Int
    name = Field.String


MyTable.insert(**dict(rec_id=1, name="a"))
MyTable.insert(**dict(rec_id=2, name="b"))
MyTable.insert(**dict(rec_id=3, name="c"))
