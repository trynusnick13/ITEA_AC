import operator


class SortKey:
    def __init__(self, *attribute_names):
        self.attribute_names = attribute_names

    def __call__(self, instance):
        values = []
        for attribute_name in self.attribute_names:
            values.append(getattr(instance, attribute_name))
        return values


class Person:
    def __init__(self, first_name, second_name, email):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email


peoples = [
    Person(first_name="Julii", second_name="Cesar", email="julii@cesar.com"),
    Person(
        first_name="Bonapart",
        second_name="Napoleon",
        email="napoleon@cakes.com",
    ),
    Person(
        first_name="Alexander",
        second_name="Makedonsiy",
        email="make@donskiy.com",
    ),
]

peoples.sort(key=SortKey("first_name"))
peoples.sort(key=SortKey("first_name", "second_name"))
peoples.sort(key=SortKey("second_name", "first_name"))
peoples.sort(key=SortKey("first_name", "second_name", "email"))
peoples.sort(key=SortKey("email"))

# Alternative operator.attrgetter()
peoples.sort(key=operator.attrgetter("first_name"))
peoples.sort(key=operator.attrgetter("second_name"))
peoples.sort(key=operator.attrgetter("second_name", "first_name"))

# >
# +
# -
# operator.add
#
# def process_two_objects(first, second, oper):
#     return oper(first, second)
#
# process_two_objects(1, "2", operator.add)
