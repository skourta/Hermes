# # app.py
import BranchNBound
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance


@app.route("/")                   # at the end point /
def hello():                      # call method hello
    tour, cost, time = BranchNBound.run()
    return "Hello"         # which returns "hello world"


if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app

# from tkinter import *

# window = Tk()
# window.geometry('350x200')
# # lbl.grid(column=0, row=0)


# def clicked():
#     BranchNBound.run()


# window.title("Welcome to LikeGeeks app")
# btn = Button(window, text="Click Me", command=clicked)
# btn.grid(column=1, row=0)
# window.mainloop()
