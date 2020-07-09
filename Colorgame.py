# import the modules  
import tkinter
import random 

# to submit the name
def callback():
    print ('You clicked the submit button! your name is:' + name.get())

def call():
    print ('Your score is:' + str(score))


  
# list of possible colour. 
colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown'] 
score = 0
  
# the game time left, initially 40 seconds. 
timeleft = 40
  
# function that will start the game. 
def startGame(event): 
      
    if timeleft == 40: 
          
        # start the countdown timer. 
        countdown() 
          
    # run the function to 
    # choose the next colour. 
    nextColour() 
  
# Function to choose and 
# display the next colour. 
def nextColour(): 
  
    # use the globally declared 'score' 
    # and 'play' variables above. 
    global score 
    global timeleft 
  
    # if a game is currently in play 
    if timeleft > 0: 
  
        # make the text entry box active. 
        e.focus_set() 
  
        # if the colour typed is equal 
        # to the colour of the text 
        if e.get().lower() == colours[1].lower(): 
              
            score += 1
  
        # clear the text entry box. 
        e.delete(0, tkinter.END) 
          
        random.shuffle(colours) 
          
        # change the colour to type, by changing the 
        # text _and_ the colour to a random colour value 
        label.config(fg = str(colours[1]), text = str(colours[0])) 
          
        # update the score. 
        scoreLabel.config(text = "Score: " + str(score)) 
  
  
# Countdown timer function  
def countdown(): 
  
    global timeleft 
  
    # if a game is in play 
    if timeleft > 0: 
  
        # decrement the timer. 
        timeleft -= 1
          
        # update the time left label 
        timeLabel.config(text = "Time left: "
                               + str(timeleft)) 
                                 
        # run the function again after 1 second. 
        timeLabel.after(1000, countdown) 
  
  
# Driver Code 
  
# create a GUI window 
root = tkinter.Tk() 
  
# set the title 
root.title("COLORGAME") 
  
# set the size 
root.geometry("600x400") 

root.configure(background='maroon')



  
# add an instructions label 
labels = tkinter.Label(root,text="NAME:",font = ('Helvetica', 17))
name = tkinter.StringVar()
entry1 = tkinter.Entry(root,text=name)


labels.pack()
entry1.pack()

button1=tkinter.Button(root,bd=4,relief="raised",text="submit:",fg="blue",bg="white",command=callback)
button1.pack()



instructions = tkinter.Label(root,bd=4,relief="solid", text = "Type in the colour"
                        "of the words, and not the word text!", 
                                      font = ('Helvetica', 17)) 
instructions.pack()  
  
# add a score label 
scoreLabel = tkinter.Label(root,bd=4,relief="solid", text = "Press enter to start", 
                                      font = ('Helvetica', 17)) 
scoreLabel.pack() 
  
# add a time left label 
timeLabel = tkinter.Label(root,bd=4,relief="solid", text = "Time left: " +
              str(timeleft), font = ('Helvetica', 17)) 
                
timeLabel.pack() 
  
# add a label for displaying the colours 
label = tkinter.Label(root,bd=4,relief="raised", font = ('Helvetica', 60)) 
label.pack() 

 
  
# add a text entry box for 
# typing in colours 
e = tkinter.Entry(root) 
  
# run the 'startGame' function  
# when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack() 
  
# set focus on the entry box 
e.focus_set() 

button1=tkinter.Button(root,bd=4,relief="raised",text="submit:",fg="blue",bg="white",command=call)
button1.pack()
  
# start the GUI 
root.mainloop()
