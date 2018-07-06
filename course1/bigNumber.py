
class BigNumber:

    def __init__(self):
        pass


    def convertNum(self, s):
        dict = {}

        numbers = ['0','1','2','3','4','5','6','7','8','9']
        return numbers.index(s)

    def Islarge(self, s1,s2):
        if len(s1)>len(s2):
            return True
        if len(s1)<len(s2):
            return False
        i = 0
        while i <len(s1):
            if self.convertNum(s1[i])< self.convertNum(s2[i]):
                return False
            elif self.convertNum(s1[i]) > self.convertNum(s2[i]):
                return True
            i +=1

        return True


    def BigNumber_Plus(self,s1,s2):    #'123' '456'
        result = []
        arr1 = []
        arr2 = []
        for i in range(0,len(s1)):
            arr1.append(self.convertNum(s1[i]))  # [1,2,3]
        for i in xrange(0,len(s2)):
            arr2.append(self.convertNum(s2[i]))  #[4,5,6,7,8,9]
        i, j = len(arr1)-1, len(arr2)-1    # len s1 and len s2
        move = 0       # 0,1
        while i>= 0 and j >= 0:
            digit = (arr1[i]+arr2[j]+move)%10    # 11%10 == 1 12%10 ==2 10%10 == 0  3+9+0%10 ==2
            result.append(digit)          #  add to result
            move = (arr1[i]+arr2[j]+move)//10     # 10-19/10 == 1
            i -=1
            j -=1

        while i>=0:
            result.append((arr1[i]+move)%10)
            move = (arr1[i]+move)/10
            i -=1

        while j>=0:
           result.append((arr2[j]+move)%10)   # [] append(1) [1] append(2) [1,2]   # result.insert(0,x)  [1,2,3]
           move = (arr2[j]+move)/10
           j -=1
        if move !=0:
            result.append(move)

        result.reverse()
        result = map(str,result)       #  map(func(), list)   ['1','2','3']   func()-> int(), [1,2,3]

        return ''.join(result)  # 'result'

    def Big_Number_Minus(self,s1, s2):
        result = []
        minus  = self.Islarge(s1,s2)   # bool

        arr1 = map(self.convertNum,s1) if minus == True else map(self.convertNum,s2)
        arr2 = map(self.convertNum,s2) if minus == True else map(self.convertNum,s1)
        i, j = len(arr1)-1,len(arr2)-1
        move = 0  # 0,-1
        while i>=0 and j>=0:
            digit = arr1[i]-arr2[j]+ move
            if digit >=0:
                result.append(digit)     # [1,2,3,4,2]
            else:
                digit = digit+10
                move = -1
                result.append(digit)
            i -=1
            j -=1

        while i>=0:
            digit = arr1[i]+move
            if digit<0:
                result.append(digit+10)
                move = -1
            else:
                result.append(digit)
            i -=1

        result.reverse()
        while result[0] == 0 and len(result)>1:
            result = result[1:]    # [1,2,3,4]   r[1:] -> [1,2,3]     [:-1]
        result = map(str,result)
        if minus == False:
            result.insert(0,'-')
        return ''.join(result)   # ['1','2','3']  -》 '123'









