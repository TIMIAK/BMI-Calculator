
import tkinter
from tkinter import*
import time
from tkinter.messagebox import*
    #import BMI Calculator GUI pack
    #from BMI Calculator GUI pack import*
root=Tk()
root.title('BMI Calculator')
root.configure(width=600,height=600,bg='powder blue')
root.wm_iconbitmap('favicon.ico')

root.resizable(False,False)

    #===================MENU=========================

#root.wm_iconbitmap('favicon.ico')

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='file',menu=filemenu)
menu.add_cascade(label='About',)
menu.add_cascade(label='Help')
menu.add_cascade(label='Contact Us')
menu.add_cascade(label='Services')
filemenu.add_command(label='New')
filemenu.add_command(label='open')


    #====================FUNCTIONS==========================
def Quit2():
    quit

def Quit1():
    quitty =tkinter.messagebox.askquestion('Quit','Are you sure')
    if quitty == ('yes'):
        root.destroy
        
    elif quitty == False:
        pass
        
                

def text_input():
    text_input = StringVar()
    operator = ''
    

         #===========CALCULATION============================
def calculate():
    height = float(heightDisplay.get())
    weight = float(weightDisplay.get())

    heightSq = height * height

    BMI = weight/heightSq
        
        #Entry(left_frame,text='%s' %(ans)).pack()
    result_input = Label(left_frame,text='This is the result')
    result_input.pack()
    result_input.configure(bg='powder blue',fg='white',font=('Arial',20,'italic'))
        
    result = Entry(left_frame,font=('Arial',20,'bold'),bd=20)
    result.pack()
        
    result.insert(0,BMI)
        #print (BMI)
        
        #=========================BMI RESULTS================================
            
    if BMI < 18.5:
            #Msglow = Message(right_frame,text='You are UnderWeight and possibly malnourshed.',font=('Arial',20,'bold'))
           # Msglow.pack(side=LEFT)
        showinfo('BMI Result','You are UnderWeight and possibly malnourshed.')
           
            
    elif BMI >=18.5 and BMI <= 24.9:
            #msgmid = Message(right_frame,text='You are within a healthy weight ''\n''range for young and middle aged adults.',font=('Arial',20,'bold'))
            #msgmid.pack(side=LEFT)
        showinfo('BMI Result','You are within a healthy weight ''\n''range for young and middle aged adults.')
    elif BMI >24.9 and BMI <=29.9:
            #msgover = Message(right_frame,text='You are Considered Overweight.',font=('Arial',20,'bold'))
            #msgover.pack(side=LEFT)
        showinfo('BMI Result','You are Considered Overweight.')
    elif BMI >30.0:
            #msgobs = Message(right_frame,text='You are Considered Obese',font=('Arial',20,'bold'))
            #msg#obs.pack(side=LEFT)
        showwarning('BMI Result','You are Considered Obese.')
            

        
    #==========================FRAMES=======================
top_frame = Frame(root,bg='powder blue',width=1600,height=70,relief=SUNKEN)
top_frame.pack(side=TOP)

left_frame = Frame(root,bg='powder blue',width=600,height=700)
left_frame.pack(side=LEFT)



    #================TOP FRAME==============================

heading = Label(top_frame,text='BMI Calculator',font=('Arial',20,'bold'),bg='powder blue',fg='white')
heading.pack()

localtime = time.asctime(time.localtime(time.time()))

time = Label(top_frame,font=('Arial',20,'bold'),text=localtime,bg='powder blue',fg='white',bd=10,anchor='w')
time.pack()

    #===============LEFT FRAME==============================

            #=================WEIGHT===============================
weight_input = Label(left_frame,text='Enter your weight in kilogram (kg)')
weight_input.pack()
weight_input.configure(bg='powder blue',fg='white',font=('Arial',20,'italic'))
weightDisplay = Entry(left_frame,font=('Arial',20,'bold'),textvariable=text_input,bd=20,insertwidth=4,bg='red',justify='right')
weightDisplay.pack()

            #===============HEIGHT======================================

height_input = Label(left_frame,text='Enter your height in Meters (M)')
height_input.pack()
height_input.configure(bg='powder blue',fg='white',font=('Arial',20,'italic'))
heightDisplay = Entry(left_frame,font=('Arial',20,'bold'),textvariable=text_input,bd=20,insertwidth=4,bg='red',justify='right')
heightDisplay.pack()

            #=================BUTTON================================

def Qreset():
    text_input = ''
    weightDisplay =('')
    heightDisplay.set('')
    result = ('')


Calculate = Button(left_frame,text='Calculate',font=('Arial',20,'bold'),command=calculate)
Calculate.pack()

Quit = Button(left_frame,text='Quit',font=('Arial',20,'bold'),command=Quit1)
Quit.pack(side=LEFT)

Reset = Button(left_frame,text='Reset',font=('Arial',20,'bold'),command=Qreset)
Reset.pack(side=RIGHT)




root.mainloop()





