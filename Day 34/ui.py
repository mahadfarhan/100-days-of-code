from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BACKGROUND = "white"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.labels()
        self.make_canvas()
        self.buttons()
        self.get_next_question()
        self.window.mainloop()

    def make_canvas(self):
        self.canvas = Canvas(self.window, width=300, height=250, background=BACKGROUND)
        self.canvas.grid(columnspan=2, row=1, column=0, padx=20, pady=50)
        self.text = self.canvas.create_text(
            150,
            125,
            text="Amazon acquired Twitch in August 2014 for $970 million dollars.",
            font=("Arial", 20, "italic"),
            width=280,
            justify="center",
            fill=THEME_COLOR,
        )

    def labels(self):
        self.label_1 = Label(
            text=f"Score: {self.score}",
            font=("Arial", 12, "normal"),
            bg=THEME_COLOR,
            fg="white",
        )
        self.label_1.grid(column=1, row=0)

    def buttons(self):
        self.correct_image = PhotoImage(file="./images/true.png")
        self.incorrect_image = PhotoImage(file="./images/false.png")
        self.correct_btn = Button(
            image=self.correct_image,
            highlightthickness=0,
            bg=BACKGROUND,
            bd=0,
            command=self.correct_answer,
        )
        self.incorrect_btn = Button(
            image=self.incorrect_image,
            highlightthickness=0,
            bg=BACKGROUND,
            bd=0,
            command=self.incorrect_answer,
        )
        self.correct_btn.grid(row=2, column=0, padx=20)
        self.incorrect_btn.grid(row=2, column=1, padx=20)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
            self.label_1.config(text=f"Score: {self.score}")
            self.correct_btn.config(state=NORMAL)
            self.incorrect_btn.config(state=NORMAL)
        else:
            self.canvas.itemconfig(
                self.text, text=f"End of quiz! Your final score is {self.score}"
            )

    def correct_answer(self):
        self.correct_btn.config(state=DISABLED)
        self.incorrect_btn.config(state=DISABLED)
        if self.quiz.check_answer():
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.give_feedback()

    def incorrect_answer(self):
        self.correct_btn.config(state=DISABLED)
        self.incorrect_btn.config(state=DISABLED)
        if not self.quiz.check_answer():
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.give_feedback()

    def give_feedback(self):
        self.window.after(1000, self.get_next_question)
