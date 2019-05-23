from appJar import gui
import winsound

#2019/26/03

def launch(start):
    if start == "Game Of Gods":
        app.showSubWindow("GOD")
    if start == "Exit": 
        app.stop()
    if start == "Exit.":
        app.stop()    
app = gui("Game Of Gods", "fullscreen")

app.addButtons(["Game Of Gods"],launch)   
app.setBg("black", override=False, tint=False)
app.setFg("white", override=False)
app.setFont(15)

app.go()