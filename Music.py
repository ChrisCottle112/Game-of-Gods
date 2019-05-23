from appJar import gui 

def blockingSound():
    app.playSound("bg.wav", wait=True)
    app.infoBox("Sound", "Finished sound")

# play the sound in a thread
def playSound():
    app.thread(blockingSound)

with gui("SOUND") as app:
    app.button("PLAY", playSound)