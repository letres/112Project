def default(*a):
    pass

class Button(object):
    #Creates a button on screen at the x1,y1,x2,y2 pos
    #Has a dictionary of colors for each posible state(str)
    #Text Displayed is a str
    def __init__(self,pos,action=default,color={"On":"red"},text="UNDEF"):
        self.pos=pos
        self.action=action
        self.color=color
        self.text=text
        self.state="On"
    def draw(self,canvas):
        canvas.create_rectangle(self.pos,fill=self.color[self.state])
        center=((self.pos[0]+self.pos[2])/2,(self.pos[1]+self.pos[3])/2)
        canvas.create_text(center,text=self.text)
    def click(self):
        return self.action
