from tkinter import*

root = Tk()
root.title("TestingInTesting")
root.geometry("1000x1000")

label1 = Label(root,text = "Hello This Is login")
label1.pack()

label2 = Label(root,text = "Name")
label2.pack()

input1 = Entry(root)
input1.pack()


label3 = Label(root,text = "Password")
label3.pack()

input2 = Entry(root)
input2.pack()



label4 = Label(root,text = "Captcha")
label4.pack()

input3 = Entry(root)
input3.pack()



label5 = Label(root)
label5.pack()

label6 = Label(root)
label6.pack()

label7 = Label(root)
label7.pack()




def jiop():
    e1 = input1.get()
    e2 = input1.get()
    e3 = input1.get()
    
    
    label5['text'] = str(e1)
    label6['text'] = str(e2)
    label7['text'] = str(e3)
    
button = Button(root,text = "Hey,Its a Button!",command = jiop)
button.pack()

root.mainloop()





