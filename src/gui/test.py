from tkinter import *
from button import Button
from button import default
from board import Board
from piece import Piece

def redrawAll(canvas,data):
    canvas.create_text(0,0,text=str(data.width),anchor=NW)
    for x in range(data.board.size[0]):
        for y in range(data.board.size[1]):
            data.board.board[x][y].draw(canvas)
    for x in data.pieces:
        for y in x:
            if isinstance(y,Piece):
                y.draw(data,canvas)


def configure(event,data):
    data.width=event.width
    data.height=event.height
    data.board.resize(data)

def keyPressed(event,data):
    pass

def mousePressed(event,data):
    

def buttonCheck(event,button):
    if button.pos[0]<=event.x<=button.pos[2] and button.pos[1]<=event.y<=button.pos[3]:
        button.state="Over"
    else:
        button.state="On"

def mouseMoved(event,data):
    for x in data.board.board:
        for y in x:
            buttonCheck(event,y)

def init(data):
    #data.button=Button((0,0,100,100),default,color={"On":"red","Over":"blue"})
    data.board=Board(data,(8,8))
    data.pieces=[[None for x in range(8)] for y in range(8)]
    data.pieces[0][0]=Piece("","black",(0,0))
def timerFired(data):
    pass


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def mouseMovedWrapper(event, canvas, data):
        mouseMoved(event,data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    
    def configureWrapper(event,canvas,data):
        configure(event,data)
        redrawAllWrapper(canvas,data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack(fill=BOTH,expand=YES)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Configure>", lambda event:
                            configureWrapper(event, canvas,data))
    root.bind("<Motion>", lambda event:
                            mouseMovedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)
