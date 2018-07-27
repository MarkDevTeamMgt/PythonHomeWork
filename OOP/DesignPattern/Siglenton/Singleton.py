

class Singleton(object):
    instance = None

    def __init__(self):
        raise SyntaxError('can not instance, please use get_instance')

    @classmethod
    def get_instance(cls):
        if Singleton.instance is None:
            Singleton.instance = object.__new__(Singleton)
        return Singleton.instance

    def showMsg(self):
        print 'Hello!!'

a = Singleton.get_instance()
b = Singleton.get_instance()
print(id(a))
print(id(b))
a.showMsg()
b.showMsg()