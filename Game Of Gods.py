from appJar import gui
import winsound

players = []

class Player:
    def __init__(self,name):
        self.name = name
    
    def printDetails(self):
        info = "Name : {}".format(self.name)
        return(info)

player1 = Player("McLeod")
players.append(player1)

def press(btn):
    if btn == "Next":
        app.nextFrame("Pages")
        app.startFrame()
        for i in range(5):
            app.addLabel("hello") 
        app.stopFrame()
        app.stopFrameStack()


def enterData(button):
    if button == "Enter":
        name = app.getEntry("Name")
        info = "Name : {}".format(name)
            
        players.append(Player(name))
            
        print(info)
        app.setLabel("Welcome","Welcome "+name)
    if button == "Enter":
        app.hideSubWindow("GOD")
        app.showSubWindow("Main")
       


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

app.startSubWindow("GOD", modal=True)


"""
sound is play when opening the game for Assessment file but not when in Wing?
app.playSound("wii.wav", wait=False)
app.playSound("bg.wav", wait=False)
app.playSound("got.wav", wait=False)
app.playSound("dbs.wav", wait=False)
"""
app.setBg("Black")
app.setSize("fullscreen")
app.addLabel("Whats your name?")
app.addLabelEntry("Name")
app.addButtons(["Enter"],enterData)       
app.addButtons(["Exit"],launch)


app.startSubWindow("Main", modal=True)
app.setBg("Black")
app.setSize("fullscreen")
app.addLabel("Intro")
app.addLabel("Welcome")
app.addLabel("This is your world " 
"please look after it, as the new life on this plant is slowly but surly destroying it!")
app.startFrameStack("Pages")
app.buttons(["Next"], press)
app.addButtons(["Exit."],launch)
app.setFocus("Name")
app.go()
