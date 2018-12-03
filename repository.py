from random import randint
from random import sample
from domain.domain import Files
class Repository():
    def __init__(self):
        self.__data = []
        
    def choosePhrase(self):
        l = Files.loadfromFile(self)
        n = len(l) - 1
        c = randint(0,n)
        self.setList(l[c])
        return l[c][:]
    
    def scramblePhrase(self):
        list = self.getList()
        list = list.split(" ")
        st = ""
        for i in range(0,len(list)):
            lst = []
            strn = ""
            for j in range(1,len(list[i])-1):
                strn = strn + str(list[i][j])
            lst.append(list[i][0])
            l = sample(strn,k = len(strn))
            for j in range(0,len(l)):
                lst.append(l[j])
            lst.append(list[i][len(list[i])-1])
            strn = ""
            for j in range(0,len(lst)-1):
                strn = strn + str(lst[j])
            strn = strn + str(lst[len(lst)-1])
            st = st + strn + " "
        v = ""
        for i in range(0,len(st)-1):
            v = v + str(st[i])
        a = []
        a.append(v)
        self.setList(a)    
        return v 
    
    def getList(self):
        return self.__data[:]
    
    def setList(self,list):
        self.__data = list
