import tkinter

FONT = ['Verdana',10,'bold']
#window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(300,300)
def click_button():
    try:
        kg = int(kg_text.get(1.0,'end-1c'))
        height = int(height_text.get(1.0,'end-1c'))
        bmi = kg/(height/100)**2
        if bmi < 18.5:
            result_label.config(text="Your BMI is Underweight", fg="blue")
        elif 18.5 <= bmi <= 24.9:
            result_label.config(text="Your BMI is Normal", fg="green")
        elif 25 <= bmi <= 29.9:
            result_label.config(text="Your BMI is Overweight", fg="orange")
        else:
            result_label.config(text="Your BMI is Obese", fg="red")
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="red")

kg_text = tkinter.Text(width=15,height=1)
kg_text.place(x=120,y=102)
height_text = tkinter.Text(width=15,height=1)
height_text.place(x=120,y=152)
#label
heading_label = tkinter.Label(text= "BMI CALCULATOR", font=FONT)
heading_label.pack()
kg_label = tkinter.Label(text= "Enter Kg:", font=('Verdana',10))
kg_label.place(x=40,y=100)
height_label = tkinter.Label(text= "Enter Height:", font=('Verdana',10))
height_label.place(x=15,y=150)

#button
my_button = tkinter.Button(text="Calculate",command=click_button,width=8,font=FONT)
my_button.place(x=140,y=185)

result_label = tkinter.Label(text="", font=("Verdana", 10, "bold"))
result_label.place(x=70, y=230)

window.mainloop()