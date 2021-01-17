#import of modules
from tkinter import *
import random
import time

class Type_test:
    def __init__(self,master):

        # setting main frame properties
        frame=Frame(master,bg="gray") # assigning frame to master and setting background to gray
        master.geometry("300x80") # setting size of the window
        master.title("Speed typing test") # setting name of the window
        master.config(bg="gray") # setting the rest of the window to the same color
        frame.pack() # packing the frame

        # setting up main label
        self.name = Label(frame, text="Speed typing test", bg="gray", fg="white") #assignig label to the main frame, setting its text, color of background and color of text
        self.name.grid(row=0, column=0, columnspan=2) # putting label in grid with span trough 2 collums

        # setting up defined text test button
        self.def_mode = Button(frame, text="Defined text", command=self.def_txt) #assignig button to the main frame, setting its text, color of background and color of text and command to execute when pressed
        self.def_mode.grid(row=1, column=0, padx=5) # putting button in grid with x padding

        # setting up words per minute button
        self.own_mode = Button(frame, text="Words per minute", command=self.wpm)
        self.own_mode.grid(row=1, column=1, padx=5)

    def def_txt(self): #Defined text test
        # setting main frame properties
        member_def=Tk() #creating new tk object
        frame_def=Frame(member_def, bg="gray")
        member_def.geometry("950x350")
        member_def.title("Defined text test")
        member_def.config(bg="gray")
        frame_def.pack()

        # reading sample texts from .txt file with newline strip
        grabbed_txt = [] #new variable for saving texts
        with open('Test text.txt') as f: # open text file as f
            grabbed_txt = [line.rstrip() for line in f] # assing each line in f to one item in grabbed_txt while stripping \n
        
        # variable for starting the timer
        self.start_time=1
        
        # setting up main label
        self.name_def = Label(frame_def, text="Defined text test", bg="gray", fg="white")
        self.name_def.grid(row=0, column=0, pady=5)

        # setting up sample texbox
        self.assignment_def = Text(frame_def) # assigning textbox to frame
        self.assignment_def.insert(END, grabbed_txt[random.randint(0,9)]) # insert randomly chosen text
        self.assignment_def.config(state=DISABLED, height= 3, wrap=WORD, bg="light gray") # set read only state, height of box, wrapping to word and background color
        self.assignment_def.grid(row=1, column=0, columnspan=2, pady=5) # putting text box in grid with span trough 2 collum a y padding

        # setting up input texbox
        self.ans_def = Text(frame_def)
        self.ans_def.config(state=DISABLED, height= 3, wrap=WORD, bg="light gray")
        self.ans_def.focus_set() # setting focus to this widget
        self.ans_def.bind('<<Modified>>', self.changed) # if contents of the box change, then call changed function
        self.ans_def.grid(row=2, column=0, columnspan=2, pady=10)
        
        # setting up label for time
        self.name_time_def = Label(frame_def, text="Time", bg="gray", fg="white")
        self.name_time_def.grid(row=3, column=0, pady=10)

        # setting up entry box for time
        self.time_def = Entry(frame_def) # assigning entry box to frame
        self.time_def.config(state=DISABLED, bg="light gray") # set read only state and background color
        self.time_def.grid(row=3 ,column=1, pady=10) # putting button in grid with y padding

        # setting up label for words per minute
        self.name_wpm_def = Label(frame_def, text="Words per minute", bg="gray", fg="white")
        self.name_wpm_def.grid(row=4, column=0, pady=10)

        # setting up entry box for words per minute
        self.wpm_def = Entry(frame_def)
        self.wpm_def.config(state=DISABLED, bg="light gray")
        self.wpm_def.grid(row=4 ,column=1, pady=10)

        # setting label for instructions
        self.misstype = Entry(frame_def, text="")
        self.misstype.config(state=DISABLED, bg="light gray")
        self.misstype.grid(row=5, column=0, columnspan=2)

        # setting label for instructions
        self.inst_wpm = Label(frame_def, text="Welcome to the Predefined text test! When you press start, you can start typing text you see above into the input box. When your text matches the text above you'll se your results", bg="gray", fg="white")
        self.inst_wpm.grid(row=6, column=0, columnspan=2)

        # setting up button for starting the test
        self.def_start = Button(frame_def, text="Start", command=self.start_type)
        self.def_start.grid(row=0, column=1, pady=5)
    
    def start_type(self): # starting function which enables the imput box
        self.ans_def.config(state=NORMAL)

    def changed(self, value=None):# function that checks if input box matches with sample text everytime when there is a change in input box
        if self.start_time==1: # conditon that allow only one pass for timer to start
            self.s_time=time.perf_counter() #save of starting time
            self.start_time=0
        flag = self.ans_def.edit_modified() #get modified flag of text box
        checked=str(self.ans_def.get("1.0", END)) #getting strings to compare
        sample=str(self.assignment_def.get("1.0", END)) #getting strings to compare
        if flag:     # prevent from getting called twice
            if sample[len(checked)-2] != checked[len(checked)-2]: # condition that checks the misstypes
                self.misstype.config(state=NORMAL) # enabling writing to the entry box
                self.misstype.delete(0, END) # deleting previous contents of te box
                self.misstype.insert(0,"Warning: MISSTYPE") # inserting new contents of the box
                self.misstype.config(state=DISABLED) # disabling writing to the entry box
            else:
                self.misstype.config(state=NORMAL) # enabling writing to the entry box
                self.misstype.delete(0, END) # deleting previous contents of te box
                self.misstype.config(state=DISABLED) # disabling writing to the entry box

            if sample == checked: # condition that chechks if sample text matches the submited one

               # calculating elapsed time
               time_s=time.perf_counter() - self.s_time

               # writing time to entry box
               self.time_def.config(state=NORMAL)
               self.time_def.insert(0,time_s)
               self.time_def.config(state=DISABLED)
               
               # calculating words per minute and writing it to entry box
               time_mins=time_s/60
               words=checked.count(" ")+1
               self.wpm_def.config(state=NORMAL)
               self.wpm_def.insert(0,(words/(time_mins)))
               self.wpm_def.config(state=DISABLED)
               
               # setting imput check box to read only 
               self.ans_def.config(state=DISABLED)
        # reset so this will be called on the next change
        self.ans_def.edit_modified(False)

    def wpm(self):
        # setting main frame properties
        member_wpm=Tk()
        frame_wpm=Frame(member_wpm, bg="gray")
        member_wpm.geometry("950x400")
        member_wpm.title("Words per minute test")
        member_wpm.config(bg="gray")
        frame_wpm.pack()

        # setting up main label
        self.name_wpm = Label(frame_wpm, text="Words per minute test", bg="gray", fg="white")
        self.name_wpm.grid(row=0, column=0, pady=5,)

        # setting up input textbox
        self.ans_wpm = Text(frame_wpm)
        self.ans_wpm.config(state=DISABLED, height= 15, wrap=WORD, bg="light gray")
        self.ans_wpm.grid(row=1, column=0, columnspan=2, pady=5)
        
        # setting up label for time
        self.name_time_wpm = Label(frame_wpm, text="Time", bg="gray", fg="white")
        self.name_time_wpm.grid(row=3, column=0, pady=10)

        # setting up entry box for time
        self.time_wpm = Entry(frame_wpm)
        self.time_wpm.config(state=DISABLED, bg="light gray")
        self.time_wpm.grid(row=3 ,column=1, pady=10)

        # setting up label for words per minute
        self.name_wpm_wpm = Label(frame_wpm, text="Words per minute", bg="gray", fg="white")
        self.name_wpm_wpm.grid(row=4, column=0, pady=10)

        # setting up entry box for words per minute
        self.wpm_wpm = Entry(frame_wpm)
        self.wpm_wpm.config(state=DISABLED, bg="light gray")
        self.wpm_wpm.grid(row=4 ,column=1, pady=10)

        # setting up button for starting the test
        self.wpm_start = Button(frame_wpm, text="Start", command=self.start_wpm)
        self.wpm_start.grid(row=0, column=1, pady=5)

        # setting label for instructions
        self.inst_wpm = Label(frame_wpm, text="Welcome to the Words per minute test! When you press start, you can start typing anythin you want into the input box. You'll have 1 minute to do so and the you'll se your results", bg="gray", fg="white")
        self.inst_wpm.grid(row=5, column=0, columnspan=2)

    def start_wpm(self):# starting function which enables the imput box and starts the timer
        self.ans_wpm.config(state=NORMAL)
        self.timer(60)

    def timer(self,count): # timer function
        self.time_wpm.config(state=NORMAL) # enabling writing to the entry box
        self.time_wpm.delete(0, END) # deleting previous contents of te box
        self.time_wpm.insert(0,count) # inserting new contents of the box
        self.time_wpm.config(state=DISABLED) # disabling writing to the entry box
        if count>0: # condition that checks state of the timer
            self.time_wpm.after(1000, self.timer, count-1) # every second call itself and decrease time by 1 sec
        
        if count <=0: # condition that passes when timer runs out
            # insterting Time's up message
            self.time_wpm.config(state=NORMAL)
            self.time_wpm.delete(0, END)
            self.time_wpm.insert(0,"Time's up!")
            self.time_wpm.config(state=DISABLED)

            # disabling the input text box
            self.ans_wpm.config(state=DISABLED)

            # calling the evaluate function
            self.evaluate()

    def evaluate (self): # evaluate function that counts words written
        words=self.ans_wpm.get("1.0", END) # getting words form input box
        lenght=len(words) # gerring size of words

        # declaring variables needed
        was_char=0
        number_of_words=0
        i=0

        # cycle that check number of words and ignores multipe spaces at row
        while i<lenght:
            if words[i] == " " and was_char==1:
                number_of_words+=1
                was_char=0
            if words[i] != " ":
                was_char=1 
            i+=1
        
        # correction for the last word
        if words[i-1]!= " " and was_char==1:
            number_of_words+=1
        
        # writing the results
        self.wpm_wpm.config(state=NORMAL)
        self.wpm_wpm.insert(0, number_of_words)
        self.wpm_wpm.config(state=DISABLED)
            
if __name__=="__main__": # main body
    root=Tk() # creating the main tk object
    run=Type_test(root) # runnig the app
    root.mainloop() # endless refresh loop for tk app
    