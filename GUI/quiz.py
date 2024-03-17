from tkinter import *
import random


names = []
asked = []
score = 0


# Dictionary of questions
questions_answers = {
    1: ["Where is the Eiffel Tower located?",
        'Paris, France',
        'London, England',
        'Rome, Italy',
        1],
    2: ["Which monument is also known as the 'City of Love'?",
        'Taj Mahal',
        'The Great Wall of China',
        'Colosseum',
        1],
    3: ["What is the nickname of the Statue of Liberty?",
        'Lady of Freedom',
        'Liberty Enlightening the World',
        'Statue of Hope',
        2],
    4: ["Which monument was built in honor of the first emperor of China?",
        'Pyramids of Egypt',
        'Petra, Jordan',
        'Terracotta Army',
        3],
    5: ["Which monument is one of the New Seven Wonders of the World and is located in Brazil?",
        'Machu Picchu',
        'Christ the Redeemer',
        'The Great Pyramid of Giza',
        2],
    6: ["Where is the Colosseum located?",
        'Athens, Greece',
        'Rome, Italy',
        'Cairo, Egypt',
        2],
    7: ["What is the ancient city located in Jordan that is famous for its rock-cut architecture?",
        'Petra',
        'Angkor Wat',
        'The Great Wall of China',
        1],
    8: ["Which monument is famous for its intricate carvings and is located in India?",
        'Stonehenge',
        'Taj Mahal',
        'Great Mosque of Mecca',
        2],
    9: ["Where is the Great Wall of China located?",
        'China',
        'India',
        'Japan',
        1],
    10: ["Which monument in Italy is known for its gladiator contests?",
          'Roman Forum',
          'Pantheon',
          'Colosseum',
          3],
}


def randomiser():
    """To select a random"""
    global qnum
    qnum = random.randint(1, 10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


class QuizStarter:
    def __init__(self, parent):
        background_color = "#40476D"


        # Frame setup
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()


        # Heading label
        self.heading_label = Label(self.quiz_frame, text="Famous Monuments Quiz", font=("Times New Roman", "18", "bold"), bg=background_color)
        self.heading_label.grid(row=0, padx=20)


        self.var1 = IntVar()


        # Username label
        self.user_label = Label(self.quiz_frame, text="Please enter your username below:", font=("Tw Cen MT", "16"), bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20)


        # Entry box for username
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)


        # Continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="orange", command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)


    def name_collection(self):
        """Collects username and starts the quiz."""
        name = self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()
        Quiz(root)


class Quiz:
    def __init__(self, parent):
        background_color = "#826754"  
        text_color = "#ffffff"  
        button_color = "#AD5D4E"  
        button_text_color = "#fffffff"  
       
        # Frame setup
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()


        randomiser()


        # Question label
        self.question_label = Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Times New Roman", "18", "bold"), bg=background_color, fg=text_color)
        self.question_label.grid(row=0, padx=20, pady=(20, 10))


        self.var1 = IntVar()


        # Radio buttons (four consistent options)
        self.rb1 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][1], variable=self.var1, value=1, indicator=0, background=background_color, fg=text_color)
        self.rb1.grid(row=1, sticky=W, padx=20, pady=5)


        self.rb2 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][2], variable=self.var1, value=2, indicator=0, background=background_color, fg=text_color)
        self.rb2.grid(row=2, sticky=W, padx=20, pady=5)


        self.rb3 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][3], variable=self.var1, value=3, indicator=0, background=background_color, fg=text_color)
        self.rb3.grid(row=3, sticky=W, padx=20, pady=5)


        # Confirm button
        self.confirm_button = Button(self.quiz_frame, text="Confirm", bg=button_color, command=self.test_progress)
        self.confirm_button.grid(row=8, padx=20, pady=(20, 10))


        # Score label
        self.score_label = Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT", "16"), bg=background_color, fg=text_color)
        self.score_label.grid(row=10, pady=(20, 10))


    def questions_setup(self):
        """Sets up the next question."""
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])


    def test_progress(self):
        """Checks user's answer and progresses through the quiz."""
        global score
        scr_label = self.score_label
        choice = self.var1.get()
       
        if len(asked) > 9:
            if choice == questions_answers[qnum][4]:
                score += 1
                scr_label.configure(text="SCORE: {} points".format(score))
                self.confirm_button.config(text="Confirm")
            else:
                # Display correct answer
                scr_label.configure(text="The correct answer was: " + questions_answers[qnum][questions_answers[qnum][4]])
                self.confirm_button.config(text="Confirm")
        else:
            if choice == questions_answers[qnum][4]:
                score += 1
                scr_label.configure(text="SCORE: {} points".format(score))
                self.confirm_button.config(text="Confirm")
                self.questions_setup()
            else:
                scr_label.configure(text="The correct answer was: " + questions_answers[qnum][questions_answers[qnum][4]])
                self.confirm_button.config(text="Confirm")
                self.questions_setup()

randomiser()


if __name__ == "__main__":
    root = Tk()
    root.title("Famous Monuments Quiz")
    quiz_instance = QuizStarter(root)
    root.mainloop()