# Header Files
from tkinter import *
from tkinter import ttk
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
from finding_match import BestMatch
import sys
from tkinter import*

texts = []
current_bar = 0
def print_progress_bar(description, iteration_counter, total_items, progress_bar_length=20):

    global current_bar

    global bars

    global texts

    global training_window

    # update the window and the bars

    button, values = training_window.ReadNonBlocking()
chatbot=ChatBot('Venis',
	logic_adapter=[{
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
	]
)
#Train Chat Bot
conv=open('kkwagh.txt','r').read()
conv1=conv.strip().split('\n')
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train('chatterbot.corpus.english.greetings')
chatbot.set_trainer(ListTrainer)
chatbot.train(conv1)
list=['bye','not responding well']
wrongip=['not correct','wrong','what are you saying?','are you idiot']

#create Chat Window
master = Tk()
master.title("Chat Window")
master.minsize(700,500)
master.maxsize(700,500)
ment = StringVar()
mlabel1 =Label(master,text='Welcome To KKW Chat Bot',height=3,width=50,fg='black',bg='light pink',font='helvetica 13 bold ').pack()

# Code To Vertical ScrollBar for Frame

class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=1,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)

#main

if __name__ == "__main__":

# Create Frame

            frame = VerticalScrolledFrame(master,highlightbackground="turquoise",highlightthickness=3)
            frame.place(x=50,y=60,height=360,width=600)

#Show The Chat Between User And Bot

def retrieve_input():
		inputValue=textBox.get("1.0","end-1c")
		textBox.delete("1.0","end")
		mtext = inputValue

		if inputValue=="" or inputValue.isspace():
			mlabel3 =Label(frame.interior,text=" Please ask Something about KKWagh College ",height=2,width=80,fg='red',bg='light blue').pack(fill=X)
		else:
			response = chatbot.get_response(inputValue)
			mlabel2 =Label(frame.interior,text="You : \t"+mtext,height=2,wraplength=550,fg='red',bg='light blue',font='helvetica 11 bold ',borderwidth=2,relief="groove").pack(fill=X)
			mlabel4 =Label(frame.interior,text=response,wraplength=550,fg='black',bg='light green',font='helvetica 12 bold ',borderwidth=2,relief="solid").pack(fill=X)

# Close The Chat
def exitSystem():
	exit();

# Text Box For Input
textBox=Text(master,height=20,width=200,bg='LightSkyBlue1')
textBox.pack()
textBox.place(x=0,y=450)

#Buttons Of SEND and EXIT
b1 =Button(master,text="SEND",command=lambda: retrieve_input(),fg = 'white',bg='blue').place(x = 500,y = 450,height=50,width=100)
b2 = Button(master,text="EXIT",command=lambda: exitSystem(),fg = 'white',bg='blue').place(x = 600,y = 450,height=50,width=100)
textBox.delete(1.0,'end')

#app = SampleApp()
mainloop()
