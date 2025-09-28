import tkinter as tk
from tkinter import messagebox
import random


questions = [
    
  
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. Bjarne Stroustrup", "C. Guido van Rossum", "D. James Gosling"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the output of the expression 3 * 'python'?",
        "options": ["A. python", "B. python*3", "C. pythonpythonpython", "D. Error"],
        "answer": "C"
    },
    {
        "question": "In Python, at which number does list indexing start?",
        "options": ["A. 1", "B. 0", "C. -1", "D. None"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to break a loop in Python?",
        "options": ["A. exit", "B. stop", "C. break", "D. end"],
        "answer": "C"
    },
    {
        "question": "Which data type is used to store multiple items in Python?",
        "options": ["A. List", "B. Loop", "C. Function", "D. Class"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. def", "B. func", "C. define", "D. function"],
        "answer": "A"
    },
    {
        "question": "Which syntax is correct to reverse a string in Python?",
        "options": ["A. str[::-1]", "B. reverse(str)", "C. str.reverse()", "D. str[-1]"],
        "answer": "A"
    },
    {
        "question": "Which method is used to access a value by key in a Python dictionary?",
        "options": ["A. get()", "B. set()", "C. append()", "D. pop()"],
        "answer": "A"
    }
]

    

random.shuffle(questions)

def show_quiz(name, roll, branch, section):
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz Time")
    
    quiz_window.geometry("1500x750")  # Width x Height
    quiz_window.resizable(False, False)  # Prevent resizing
    quiz_window.update_idletasks()
    x = (quiz_window.winfo_screenwidth() // 2) - (1500 // 2)
    y = (quiz_window.winfo_screenheight() // 2) - (750 // 2)
    quiz_window.geometry(f"+{x}+{y}")  # Center the window

    score = [0]
    q_index = [0]

    question_label = tk.Label(quiz_window, text="", font=("Arial", 20))
    question_label.pack(pady=20)
   

    option_buttons = []
    for i in range(4):
        btn = tk.Button(quiz_window, text="", width=40,
                        command=lambda i=i: check_answer(option_buttons[i].cget("text")))
        btn.pack(pady=40)
        option_buttons.append(btn)
        
     # back buttun  
        back_button = tk.Button(quiz_window, text="Back", font=("Arial", 20), bg="lightgray",
                            command=quiz_window.destroy)
    back_button.pack(pady=20)

    

    def next_question():
        if q_index[0] < len(questions):
            q = questions[q_index[0]]
            question_label.config(text=f"Q {q_index[0] + 1}: {q['question']}")
            for i, opt in enumerate(q["options"]):
                option_buttons[i].config(text=opt)
        else:
            messagebox.showinfo("Quiz Completed", f"Your Score: {score[0]}/{len(questions)}")
            # with open("quiz_results.txt", 'a') as file:
            with open("quiz_results.txt", 'a', encoding='utf-8') as file:

                file.write(f"Name: {name}, Roll: {roll}, Branch: {branch}, Section: {section}, Score: {score[0]}/{len(questions)}\n")
            quiz_window.destroy()

    def check_answer(selected):
        if q_index[0] < len(questions):
            correct = questions[q_index[0]]["answer"]
            if selected.startswith(correct + "."):  # Match by prefix like "C. HTML"
        # if selected == correct:
             score[0] += 1
        q_index[0] += 1
        next_question()



    next_question()


  



# -------------------- Login Screen --------------------
def start_quiz():
    name = name_entry.get().strip()
    roll = roll_entry.get().strip()
    branch = branch_entry.get().strip()
    section = section_entry.get().strip()
    
    if name and roll and branch and section:
        messagebox.showinfo("Welcome", f"Hello {name}!\nRoll No: {roll}\nBranch: {branch}\nSection: {section}")
        show_quiz(name, roll, branch, section)
    else:
        messagebox.showwarning("Missing Info", "Please fill all fields.")
        


        
# -------------------- GUI Setup --------------------
import tkinter as tk

root = tk.Tk()
root.title("Quiz Login")
root.attributes("-fullscreen", True)  
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))  


# Create a frame and center it
form_frame = tk.Frame(root)
form_frame.place(relx=0.5, rely=0.5, anchor='center')  # Center horizontally and vertically

# Add form elements inside the frame
tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=20, pady=10)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=20, pady=10)

tk.Label(form_frame, text="Roll No").grid(row=1, column=0, padx=20, pady=10)
roll_entry = tk.Entry(form_frame)
roll_entry.grid(row=1, column=1, padx=20, pady=10)

tk.Label(form_frame, text="Branch").grid(row=2, column=0, padx=20, pady=10)
branch_entry = tk.Entry(form_frame)
branch_entry.grid(row=2, column=1, padx=20, pady=10)

tk.Label(form_frame, text="Section").grid(row=3, column=0, padx=20, pady=10)
section_entry = tk.Entry(form_frame)
section_entry.grid(row=3, column=1, padx=20, pady=10)

login_button = tk.Button(form_frame, text="Login", command=start_quiz)
login_button.grid(row=4, column=1, padx=20, pady=10)

root.mainloop()


















































































