from button import Button
class Board(object):
    def __init__(self,data,size):
        #Size is a tuple (y,x)
        #Board is a list of lists
        self.size=size
        self.board=[]
        for x in range(self.size[0]):
            self.board.append([])
            for y in range(self.size[1]):
                if (y+x)%2==0:
                    checker="white"
                else: checker="black"
                self.board[x].append(Button((0,0,0,0),action=5,color={"On":checker,"Over":"blue"}
                        ,text=""))
                self.resize(data)
                
    def resize(self,data):
        self.cell=data.width/(self.size[0]+2)
        self.cell=(self.cell,data.height/self.size[1])
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                self.board[x][y].pos=((x+1)*self.cell[0],y*self.cell[1],(x+2)*self.cell[0],(y+1)*self.cell[1])

