import logging
import tkinter
import numpy as np
import tkinter.messagebox
from tkinter import *
from Graphs import Graphs
import pandas as pd
from Data import Machine

# Sommer Starr, C964 Computer Science Capstone, ID: 001059225
# Username and password are both the word 'test'


def graph_data():
    graph = Graphs()
    graph.plot_graphs(cereal_data)


def calculate(p1, p2, p3, p4, p5):
    name = p1.get()
    sugar = p2.get()
    fat = p3.get()
    calories = p4.get()
    rating_box = p5
    machine2 = Machine()
    m = machine2.get_machine(cereal_data)
    x = pd.DataFrame([[calories, fat, sugar]], columns=['Calories', 'Fat (g)', 'Sugar (g)'])
    rating = machine2.predict(m, x)
    rating.astype(np.float64)
    rating = rating[0]
    rating_box.insert(END, '%s: %.2f' % (name, rating))

    p1.delete(0, END)
    p2.delete(0, END)
    p3.delete(0, END)
    p4.delete(0, END)


def delete_selected(b):
    box = b
    box.delete(tkinter.ANCHOR)


def predict_page(rooty):
    rooty.destroy()
    root3 = Tk()
    root3.geometry("885x560+230+60")
    root3.iconbitmap("food.ico")
    root3.config(bg='gray93')
    image1 = PhotoImage(file='cereal.png')
    label3 = Label(root3, image=image1)
    label3.grid(row=10, column=5)
    root3.resizable(False, False)
    root3.title("")
    title = Label(text="Predict Cereal Ratings", font=('Arial', 15), bg='gray93')
    title.grid(row=1, column=5, pady=50, padx=10)
    name_label = Label(root3, text="Name:", font=('Arial', 15), bg='gray93')
    name_label.grid(row=5, column=2, padx=10, pady=20)
    sugar_label = Label(root3, text="Sugar (g):", font=('Arial', 15), bg='gray93')
    sugar_label.grid(row=10, column=2, padx=10, pady=20)
    fat_label = Label(root3, text="Fat (g):", font=('Arial', 15), bg='gray93')
    fat_label.grid(row=15, column=2, padx=10, pady=20)
    calories_label = Label(root3, text="Calories:", font=('Arial', 15), bg='gray93')
    calories_label.grid(row=20, column=2, padx=10, pady=20)
    name_box = Entry(root3)
    name_box.grid(row=5, column=4, padx=50)
    sugar_box = Entry(root3)
    sugar_box.grid(row=10, column=4, padx=50)
    fat_box = Entry(root3)
    fat_box.grid(row=15, column=4, padx=50)
    calories_box = Entry(root3)
    calories_box.grid(row=20, column=4, padx=50)
    box = Listbox(root3, height=18, width=30, font=('Arial', 10))
    box.grid(row=1, column=30, columnspan=100, rowspan=100, padx=50, pady=10, sticky='e')
    button4 = Button(root3, text="Calculate", command=lambda: calculate(name_box, sugar_box, fat_box, calories_box,
                                                                        box), bg='white', font=('Arial', 10))
    button4.grid(row=35, column=4, ipadx=5, pady=20)
    button5 = Button(root3, text="Back", command=lambda: load_main_page(root3), bg='white', font=('Arial', 10))
    button5.grid(ipadx=15, sticky='se', row=80, column=125, pady=6, padx=2)
    button6 = Button(root3, text="Delete Selected", command=lambda: delete_selected(box),
                     bg='white', font=('Arial', 10))
    button6.grid(row=35, column=110, sticky='ne')
    root3.mainloop()

    machine = Machine()
    scores = machine.score_machine(cereal_data)
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='Logging',
                        level=logging.INFO)
    logging.info(scores)


def check_login():
    username = entry.get()
    password = entry2.get()
    if username == "test" and password == "test":
        load_main_page(root)
    else:
        tkinter.messagebox.showwarning(title="Error", message="Wrong username/password combination")


def load_main_page(rooty):
    root_d = rooty
    root_d.destroy()
    root2 = Tk()
    root2.geometry("660x320+340+150")
    root2.config(bg='gray93')
    root2.iconbitmap("food.ico")
    root2.resizable(False, False)
    root2.title("")
    title = Label(root2, text="What would you like to do?", font=('Arial', 14), bg='gray93')
    title.grid(row=10, column=50, padx=10, pady=80)
    button2 = Button(root2, text="Graph Data", command=graph_data, bg='white')
    button2.grid(row=50, column=45, padx=50, ipadx=20)
    button3 = Button(root2, text="Predict", command=lambda: predict_page(root2), bg='white')
    button3.grid(row=50, column=55, padx=40, ipadx=30)
    root2.mainloop()


if __name__ == '__main__':
    cereal_data = pd.read_csv("cereal.csv")
    cereal_data = cereal_data.dropna()
    cereal_data = cereal_data.drop(["mfr", "name", "carbo", "type", "protein",
                                    "sodium", "fiber", "potass", "vitamins", "shelf", "weight", "cups"], axis=1)
    cereal_data.rename(columns={"sugars": "Sugar (g)"}, inplace=True)
    cereal_data.rename(columns={"fat": "Fat (g)"}, inplace=True)
    cereal_data.rename(columns={"rating": "Rating"}, inplace=True)
    cereal_data.rename(columns={"calories": "Calories"}, inplace=True)

    root = Tk()
    root.geometry("520x300+400+200")
    root.iconbitmap("food.ico")
    root.resizable(False, False)
    root.title("Log In")
    root.config(bg='gray93')
    label = Label(root, text="Username:", bg='gray93', font=('Arial', 10))
    label.grid(row=5, column=15, pady=60, padx=70)
    label2 = Label(root, text="Password:", bg='gray93', font=('Arial', 10))
    label2.grid(row=10, column=15)
    entry = Entry(root)
    entry.grid(row=5, column=20, pady=80, padx=10)
    entry2 = Entry(root)
    entry2.grid(row=10, column=20)
    button = Button(root, text="Enter", command=check_login, bg='white', font=('Arial', 10))
    button.grid(row=100, column=100, pady=50, padx=60, ipadx=20)
    root.mainloop()
