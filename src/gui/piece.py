class Piece(object):
    def __init__(self,name,color,pos,data):
        self.name=name
        self.letter="Y"
        self.color=color
        self.selfCapture=False
        self.font="times 50"
        self.moves=[
                [False for x in range(8)] for y in range(8)
                ]
        self.pos=pos
        self.dirs={"up","side","down"}
        self.vecs=[(1,0),(1,1)]
        self.mult=-1
        self.max=8
        if self.color=='black':
            self.mult*=-1
        self.update(data)
    def move(self,data,pos):
        data.select=False
        if moves[pos[0]][pos[1]]:
            data.pieces[pos[0]][pos[1]]=data.pieces[self.pos[0]][self.pos[1]]
            data.pieces[self.pos[0]][self.pos[1]]=None
            self.pos=pos
            for x in data.pieces:
                for y in x:
                    if y!=None:
                        y.update(data)
    def draw(self,data,canvas):
        cell=data.board.cell
        size=data.board.size
        pos=((self.pos[0]+1.25)*cell[0],(self.pos[1]+.25)*cell[1],(self.pos[0]+1.75)*cell[0]
                ,(self.pos[1]+.75)*cell[1])
        canvas.create_oval(pos,fill=self.color,outline="red")
        pos=((pos[0]+pos[2])/2,(pos[1]+pos[3])/2)
        canvas.create_text(pos,text=self.letter,font="times 50",fill="red")
    def update(self,data,pos=False,vec=False,count=0):
        if pos==False:
            self.update(data,self.pos)
            self.moves=[[False for x in range(8)]for y in range(8)]
        elif vec==False:
            vecs=set()
            if "up" in self.dirs:
                for x1 in range(-1,2,2):
                    for x in self.vecs:
                        print(vecs)
                        vecs.add((pos[0]+x[0]*x1,pos[1]+x[1]*self.mult))
            if "right" in self.dirs:
                for  x1 in range(-1,2,2):
                    for x2 in range(-1,2,2):
                        for x in self.vecs:
                            vecs.add((pos[0]+x[1]*x1,pos[1]+x[0]*x2))
            if "down" in self.dirs:
                for  x1 in range(-1,2,2):
                    for x in self.vecs:
                        vecs.add((pos[0]+x[0]*x1,pos[1]-x[1]*self.mult))
            vecs=list(vecs)
            for vec in vecs:
                self.update(data,(pos[0]+vec[0],pos[1]+vec[1]),vec,count+1)
        elif count>self.max or (0>=pos[0]>=7 or 0>=pos[1]>=7):
            print('nope')
            return None
        else:
            print(pos)
            if data.pieces[pos[0]][pos[1]]!=None:
                if self.selfCapture:
                    self.moves[pos[0]][pos[1]]=True
                elif self.color!=data.pieces[pos[0]][pos[1]].color:
                    self.moves[pos[0]][pos[1]]=True
            else:
                self.moves[pos[0]][pos[1]]=True
                self.update(data,(pos[0]+vec[0],pos[1]+vec[1]),vec,count+1)

class Pawn(Piece):
    def __init__(self,color,pos,data):
        super().__init__("",color,pos,data)
        self.letter="P"
        if color=='black':
            fun=lambda x,y:(y==-1 and x==0)
            self.change(fun,self.moves)
            fun=lambda x,y:(y==-1 and abs(x)==1)
            self.change(fun,self.captures)
        else:
            fun=lambda x,y:(y==1 and x==0)
            self.change(fun,self.moves)
            fun=lambda x,y:(y==1 and abs(x)==1)
            self.change(fun,self.captures)
    def move(self,data,pos):
        super().move(data,pos)
        if self.color=='black' and self.pos[1]==len(data.board.board)-1:
            data.pieces[self.pos[0]][self.pos[1]]=Queen('black',self.pos)
        elif self.pos[1]==0:
            data.pieces[self.pos[0]][self.pos[1]]=Queen('white',self.pos)
class Queen(Piece):
    def __init__(self,color,pos,data):
        super().__init__("",color,pos,data)
        self.letter="Q"
        fun=lambda x,y:((x==0 or y==0) or (abs(x)==abs(y)))
        self.change(fun,self.moves)
        self.change(fun,self.captures)
class Rook(Piece):
    def __init__(self,color,pos,data):
        super().__init__("",color,pos,data)
        self.letter="R"
        fun=lambda x,y:((x==0 or y==0))
        self.change(fun,self.moves)
        self.change(fun,self.captures)
class Bishop(Piece):
    def __init__(self,color,pos,data):
        super().__init__("",color,pos,data)
        self.letter="B"
        fun=lambda x,y:abs(x)==abs(y)
        self.change(fun,self.moves)
        self.change(fun,self.captures)
class King(Piece):
    def __init__(self,color,pos,data):
        super().__init__("",color,pos,data)
        self.letter="K"
        fun=lambda x,y:abs(x)<=1 and abs(y)<=1
        self.change(fun,self.moves)
        self.change(fun,self.captures)
