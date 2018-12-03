class Files:
    def __init__(self):
        self._list = []
        
    def storeToFile(self):
        f = open("C:\\Users\\ana-diana\\new workspace\\scramble\\input.txt","w")
        st = " "
        while st != "":
            st = input()
            f.write(st)
        f.close()
        
        
    def loadfromFile(self):
        self._list = []
        f = open("C:\\Users\\ana-diana\\new workspace\\scramble\\input.txt","r")
        line  = f.readline().strip()
        while line != "":
            self._list.append(line)
            line = f.readline().strip()
        f.close()
        return self._list[:]
        
    def getList(self):
        return self._list[:]
    
    def setList(self,l):
        self._list = l 
 
                
        
        
        
        
        

