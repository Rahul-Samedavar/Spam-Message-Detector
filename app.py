from customtkinter import *
import joblib

model = joblib.load('build/models/spam_detector_model.pkl')

bg = "#e8e8e8"
txt_clr  = "#000000"
btn_clr  = "#00BFA5"
spam_clr = "#FF7043"
ham_clr  = "#66BB6A"

win = CTk()
win.title("Spam Detector")
win.geometry("1000x600")

nav_bar = CTkFrame(win, corner_radius=0, fg_color=txt_clr)
nav_bar.pack(side="top", fill="x", expand=True, anchor="n")

main_title = CTkLabel(nav_bar, font=("Roboto bold", 34), anchor="w", text_color=bg, text="Spam Mail Detector".upper())
main_title.pack(side="top", fill="x", padx=10, pady=4)

body = CTkFrame(win, corner_radius=0, fg_color="transparent")
body.pack(side="bottom", fill="both", expand=True, anchor="n")

title = CTkLabel(body, font=("Roboto bold", 34), text_color=txt_clr, text="Enter a Mail to Check")
title.pack(side="top", fill="x", expand=True, anchor="n")

inp = CTkTextbox(body, font=("Roboto bold", 14),height=400, corner_radius=20)
inp.pack(fill="both", expand=True, anchor="center", padx=40)

btns= CTkFrame(body, fg_color="transparent")
btns.pack(side="bottom", pady=10)

def predict_spam():
    mail = [inp.get("1.0", END)]
    if model.predict(mail):
        print("spam")
        inp.configure(fg_color = spam_clr)
        title.configure(text_color=spam_clr, text="Spam Mail!!")
    else:
        print("ham")
        inp.configure(fg_color = ham_clr)
        title.configure(text_color=ham_clr, text="Not a Spam Mail :)")

def clear():
    inp.delete("1.0", END)
    inp.configure(fg_color = "white")
    title.configure(text_color=txt_clr, text="Enter a Mail to Check")

check_btn = CTkButton(btns, font=("Roboto bold", 30), fg_color=btn_clr, text_color=txt_clr, width=240,
                    command=predict_spam, text="Check Spam")
check_btn.pack(side="left", padx=10)

clear_btn = CTkButton(btns, font=("Roboto bold", 30), fg_color=btn_clr, text_color=txt_clr, width=240,
                    command=clear, text="Clear")
clear_btn.pack(side="right", padx=10)


win.mainloop()
