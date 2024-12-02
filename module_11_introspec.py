from pprint import pprint
def introspection_info(obj):
    info = {
        'type': type(obj),
        'attributes': dir(obj),
        'methods': [attr for attr in dir(obj) if callable(getattr(obj, attr))],
    }
    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__
    else:
        info['module'] = None

    return info

number_info = introspection_info(42)
pprint(number_info)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def new_year(self):
        self.age += 1

max = Human(max, 10)
pprint(introspection_info(max))        