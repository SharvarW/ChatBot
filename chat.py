from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
from finding_match import BestMatch
import tkinter as tk

'''training_layout = [[tk.T('TRAINING PROGRESS', size=(20, 1), font=('Helvetica', 17))], ]
training_window = tk.Window('Training').Layout(training_layout)
texts = []'''


current_bar = 0
def print_progress_bar(description, iteration_counter, total_items, progress_bar_length=20):

    global current_bar

    global bars

    global texts

    global training_window

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

conv=open('kkwagh.txt','r').read()
conv1=conv.strip().split('\n')

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train('chatterbot.corpus.english.greetings')

chatbot.set_trainer(ListTrainer)
chatbot.train(conv1)
list=['bye','not responding well']
wrongip=['not correct','wrong','what are you saying?','are you idiot']

master = tk()
master.minsize(300,100)
master.geometry("320*100")
def callback():
	print ("click!")
b = Button(master,text="Send",command=callback,height=50,width=150,compound=LEFT)
b.place(x = 20,y = 20)


while True:

    button, (value,) = window.Read()

    if button is not 'SEND':

        break

    string = value.rstrip()
    print('     '+string)

    response = chatbot.get_response(value.rstrip())

    print(response)
