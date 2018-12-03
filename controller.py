from repository.repository import Repository
class Game:
    def __init__(self):
        self.__repo = Repository()
    
    def playerMove(self,w1,l1,w2,l2,lst,scor):
        ls = lst.split(' ')
        l = []
        for i in range(0,len(ls)):
            l.append([])
            for j in range(0,len(ls[i])):
                l[i].append(ls[i][j])
        aux = l[w1-1][l1-1]
        l[w1-1][l1-1] = l[w2-1][l2-1]
        l[w2-1][l2-1] = aux
        ls = ""
        for i in range(0,len(l)-1):
            for j in range(0,len(l[i])):
                ls = ls + str(l[i][j])
            ls = ls + " "
        for i in range(0,len(l[len(l)-1])):
            ls = ls + str(l[len(l)-1][i])
        scor = scor - 1
        return ls,scor  
        
    def computerMove(self):
        s = self.__repo.choosePhrase()
        st = self.__repo.scramblePhrase()
        return s,st