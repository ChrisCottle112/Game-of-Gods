from appJar import gui
import winsound

#2019/3/04
players = []


class Player:
    def __init__(self,name):
        self.name = name
    
    def printDetails(self):
        info = "Name : {}".format(self.name)
        return(info)

player1 = Player("McLeod")
players.append(player1)

            
def enterData(button):
    if button == "Enter":
        name = app.getEntry("Name")
        info = "Name : {}".format(name)
            
        players.append(Player(name))
            
        print(info)
        app.setLabel("Welcome","Welcome "+name)


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

app.go()