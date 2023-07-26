import tkinter
screen = tkinter.Tk()
screen.title("BMI calculator")
screen.minsize(width=300,height=250)
FONT=('Times New Roman',12,'normal')
my_label=tkinter.Label(text="BMI calculator",font=FONT)
my_label.pack()
BMI = 0.0
#wightlabel
first_input=tkinter.Label(text="Please enter your weight!(kg)",font=FONT)
first_input.pack()
#entryone
my_entry_1=tkinter.Entry(width=20)
my_entry_1.pack()
#heightlabel
second_input = tkinter.Label(text="Please enter your height!(mt)",font=FONT)
second_input.pack()
#entrytwo
my_entry_2=tkinter.Entry(width=20)
my_entry_2.pack()
def calculate_button():
    try:
        user_weight = int(my_entry_1.get())
        user_height = int(my_entry_2.get())
    except ValueError:
        my_info_label.config(text="Enter valid number", font=FONT)
    except UnboundLocalError:
        my_info_label.config(text="Enter number not calculated!", font=FONT)
    finally:
        BMI = user_weight / ((user_height/100) ** 2)
    if BMI<=18.5:
        my_info_label.config(text=f"your BMI is:{round(BMI,3) } you're underweight.! eat something",font=FONT)
    elif 18.5<BMI<=24.9:
        my_info_label.config(text=f"your BMI is:{round(BMI, 3)} you're normal.!", font=FONT)
    elif 24.9<BMI<=29.9:
        my_info_label.config(text=f"your BMI is:{round(BMI, 3)} you're overweight. RUN!", font=FONT)
    else:
        my_info_label.config(text=f"your BMI is:{round(BMI, 3)} you're obese. Go to gym!", font=FONT)


#calculatebutton
my_button=tkinter.Button(text="calculate your BMI!",command=calculate_button)
my_button.pack()
#infolabel
my_info_label=tkinter.Label(text=f"your BMI is:{BMI}",font=FONT)
my_info_label.pack()

screen.mainloop()