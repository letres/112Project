from button import Button
class Board(object):
    def __init__(self,data,size):
        self.size=size
        self.board=[]
        for x in range(self.size[0]):
            self.board.append([])
            for y in range(self.size[1]):
                self.board[x].append(Button((0,0,0,0),action=5,color={"On":"red","Over":"blue"}
                        ,text=""))
        self.resize(data)
    def resize(self,data):
        self.cell=data.width/(self.size[0]+2)
        self.cell=(self.cell,data.height/self.size[1])
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.board[x][y].pos=(
                        (x+1)*self.cell[0],y*self.cell[1],(x+2)*self.cell[0],(
                            y+1)*self.cell[1])
