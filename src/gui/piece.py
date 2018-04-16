class Piece(object):
    def __init__(self,name,color,pos):
        self.name=name
        self.letter="Y"
        self.color=color
        self.font="times 50"
        self.moves=[
                [True for x in range(8)] for y in range(8)
                ]
        self.captures=self.moves
        self.pos=pos
    def move(self,data,pos):
        if isinstance(data.pieces[pos[0]][pos[1]],Piece) and (
                data.pieces[pos[0]][pos[1]].color!=self.color):
            moves=self.captures
        else:
            moves=self.moves
        moveX=self.pos[0]-pos[0]
        moveY=self.pos[1]-pos[1]
        if moves[moveX][moveY]:
            data.pieces[pos[0]][pos[1]]=self
            data.pieces[self.pos[0]][self.pos[1]]=None
            self.pos=pos
    def draw(self,data,canvas):
        cell=data.board.cell
        size=data.board.size
        pos=((self.pos[0]+1.25)*cell[0],(self.pos[1]+.25)*cell[1],(self.pos[0]+1.75)*cell[0]
                ,(self.pos[1]+.75)*cell[1])
        canvas.create_oval(pos,fill=self.color)
        pos=((pos[0]+pos[2])/2,(pos[1]+pos[3])/2)
        canvas.create_text(pos,text=self.letter,font="times 50",fill="red")


