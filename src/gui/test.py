from tkinter import *
from button import Button
from button import default

def redrawAll(canvas,data):
    canvas.create_text(0,0,text=str(data.width),anchor=NW)
    data.button.draw(canvas)

def configure(event,data):
    data.width=event.width
    data.height=event.height
    data.button.pos=(data.width/3,data.height/3,data.width/3*2,data.height/3*2)

def keyPressed(event,data):
    pass

def mousePressed(event,data):
    pass

def mouseMoved(event,data):
    if data.button.pos[0]<=event.x<=data.button.pos[2] and data.button.pos[1]<=event.y<=data.button.pos[3]:
        data.button.state="Over"
    else:
        data.button.state="On"

def init(data):
    data.button=Button((0,0,100,100),default,color={"On":"red","Over":"blue"})

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
