from tkinter import *
from tkinter import messagebox as mb
import json

#class to define the components of the GUI
class Quiz:
	
	def __init__(self):
		
		# set question number to 0
		self.q_no=0
		
		#assigns question to display_ques function
		self.display_title()
		self.display_question()
		
		# opt_selected holds an integer value which is used for selected option in a question.
		self.opt_selected=IntVar()
		
		#display radio buttons for current question and used to display options for current question
		self.opts=self.radio_buttons()
		
		#display options for current ques
		self.display_options()
		
		# displays the button for next and exit.
		self.buttons()
        
		# no of questions
		self.data_size=len(question)
		
		# keep a counter of correct answers
		self.correct=0


	#Used to display result. Counts number of correct and wrong answers and displays them at the end as messagebox
	def display_result(self):
		
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	# This method checks the Answer after we click on Next.
	def check_ans(self, q_no):
		
		# checks for if the selected option is correct
		if self.opt_selected.get() == answer[q_no]:
			# if the option is correct it return true
			return True

    # This method is used to check the answer of the
    # current question by calling the check_ans and question no.
    # if the question is correct it increases the count by 1
    # and then increase the question number by 1. If it is last
    # question then it calls display result to show the message box.
    # otherwise shows next question
    
	def next_btn(self):
		
		# Check if the answer is correct
		if self.check_ans(self.q_no):
			
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		
        #Move to next Ques  
		self.q_no += 1
		
		# checks if the q_no size is equal to the data size
		if self.q_no==self.data_size:
			
			# if it is true then it displays the score
			self.display_result()
			
			# destroys the GUI
			root.destroy()
		else:
			# shows the next question
			self.display_question()
			self.display_options()

    # This method shows the two buttons on the screen- Next and Quit
	def buttons(self):
		
		next_button = Button(root, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		
		next_button.place(x=350,y=380)
		
		quit_button = Button(root, text="Quit", command=root.destroy,
		width=5,bg="red", fg="white",font=("ariel",16," bold"))
		
		quit_button.place(x=700,y=50)


	# This method deselect the radio button on the screen
    # Then it is used to display the options available for the current
	def display_options(self):
		val=0
		
		# deselecting the options
		self.opt_selected.set(0)
		
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1


	# This method shows the current Question on the screen
	def display_question(self):
		
		q_no = Label(root, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		
		q_no.place(x=70, y=100)


	# This method is used to Display Title
	def display_title(self):
		
		title = Label(root, text="Welcome to QUIZ",
		width=50, bg="light blue",fg="black", font=("ariel", 20, "bold"))
		
		title.place(x=0, y=2)


	# This method shows the radio buttons to select the Question
    # on the screen at the specified position.
	def radio_buttons(self):
		
		q_list = []
		
		y_pos = 150
		
		while len(q_list) < 4:
			
			radio_btn = Radiobutton(root,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			
			q_list.append(radio_btn)
			
			radio_btn.place(x = 100, y = y_pos)
			
			y_pos += 40

		return q_list

# Create a GUI Window
root = Tk()

# set the size of the GUI Window
root.geometry("800x450")

# set the title of the Window
root.title("Quiz")

# get the data from the json file
with open('D:\GITHUB PROJECTS\Tkinter Projects\MCQ_Game\data.json') as f:
	data = json.load(f)

# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

# create an object of the Quiz Class.
quiz = Quiz()

root.mainloop()
