

def valid(str):
    pass


def getVirtual(str):
    if str == 'i':
        return 1
    elif str == '-i':
        return -1
    else:
        return  int(str[:-1])

def getOpposite(num):
    return  num-2*num

def prase(str):
    if 'i' not in str:
        return  int(str), 0
    else:
        if '+' in str:
            x,y = str.split('+')
            return int(x), getVirtual(y)
        elif '-' in str:
            list = str.split('-')
            real = 0
            virtual = 0
            print list
            if len(list) == 3:
                real = getOpposite(int(list[1]))
                virtual = getOpposite(getVirtual(list[2]))
            if len(list) == 2 and '' not in list:
                real = int(list[0])
                virtual = getOpposite(getVirtual(list[1]))
            if len(list) == 2 and '' in list:
                real = 0
                virtual = getOpposite(getVirtual(list[1]))
            return  real,virtual
        else:
            return 0,getVirtual(str)

def addition(x, y):
    a,b = prase(x)
    print  a, b
    c,d = prase(y)
    print  c, d
    real = ''
    if a+c !=0:
        real = str(a+c)
    virtual = ''
    if b+d !=0:
        if b+d > 0:
            virtual = '+'+str(b+d)+'i'
            if b+d ==1:
                virtual = '+i'
        else:
            virtual = str(b+d)+'i'
            if b+d == -1:
                virtual = '-i'
    return real+virtual


def subtraction(x, y):
    pass

def multiplication(x,y):
    pass

def division(x,y):
    pass





if __name__ == '__main__':
    x = "-1-i"
    y = "-i"
    print addition(x,y)