from appJar import gui
import winsound

#2019/20/05


players = [] 
#Here is where the player name is save within a class
class Player:
    def __init__(self,name):
        self.name = name
        self.health = 100 #Setting the health of the player to a socre of 100   
    
    def printDetails(self):
        info = "Name : {}".format(self.name)
        return(info)


#NextData is where the right answer to the question will continue the game hide/close one Subwindow after a each other            
def nextData(button):
    if button == "Next":
        app.hideSubWindow("GOD")
        app.hideSubWindow("Main")
        app.showSubWindow("EarthSub")
    if button == "worng":
        app.hideSubWindow("EarthSub")
        app.showSubWindow("EarthSub2")
    if button == "No":
        app.hideSubWindow("EarthSub2")
        app.showSubWindow("EarthSub3")
    if button == "Intervene":
        app.hideSubWindow("EarthSub3")
        app.showSubWindow("EarthSub4")        
#this is where the player health is taken off from the main one i set
#exmaple if you get a qustion worng it will go from 100 down to 50.
#I have also add a setLabel to show ingame how much health the user has.
def updateData():
    players[0].health -= 100
    print(players[0].health)
    app.setLabel("label1",players[0].health)
    if players[0].health == 0:
        app.stop()
         
def enterData(button):
    if button == "Enter":
        name = app.getEntry("Name")
        players.append(Player(name))        
        info = "Name : {}".format(name)
            
        players.append(Player(name))
            
        print(info)
        app.setLabel("Welcome","Welcome "+name)
    if button == "Enter":
        app.hideSubWindow("GOD")
        app.showSubWindow("Main")
    if button == "wrong":
        updateData()
    if button == "Yes":
        updateData()
    if button == "Stand aside":
        updateData()    
    

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
app.addButtons(["Next"], nextData)
app.addButtons(["Exit."],launch)
app.setFocus("Name")



def EarthStart(Health,Happiness):
    print()


    
app.startSubWindow("EarthSub", modal=True)
app.setBg("Black")
app.setSize("fullscreen")
app.addLabel("label1","As a god you must choose worng and worng")
app.addButtons(["wrong"],enterData)
app.addButtons(["worng"],nextData)


app.startSubWindow("EarthSub2", modal=True)
app.setBg("Black")
app.setSize("fullscreen")
app.addLabel("Great Job, Now you know how to do the basic")
app.addLabel("Ok lets get started, you see a country wanting to poor oil in the sea, as the god of your world are you going let this stand?") 
app.addButtons(["No"],nextData)
app.addButtons(["Yes"],enterData)

app.startSubWindow("EarthSub3", modal=True)
app.setBg("Black")
app.setSize("fullscreen")
app.addLabel("Wow Your pertty good at being a god!")
app.addLabel("Oh No, A country is putting all of its plasitc in the sea! what are you going to do!")
app.addButtons(["Intervene"],nextData)
app.addButtons(["Stand aside"],enterData)

app.startSubWindow("EarthSub4", modal=True)
app.setBg("Black")
app.setSize("fullscreen")
app.addLabel("Dam! you put a stop to that!")






app.go()