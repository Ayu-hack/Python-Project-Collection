#Calculator in Python

from tkinter import *                                                   

def Click_button(numbers):                                                  
    global value                                                     
    value = value + str(numbers)
    text_Input.set(value)                                            
    
def Backspace():                                                        
    global value
    value=""
    text_Input.set("")                                                 
def Equal():
    global value
    sumup=str(eval(value))                                           
    text_Input.set(sumup)                                            
    value=""       

_main_ = Tk()                                                             
_main_.title("Calculator")                                                
value=""
text_Input= StringVar()


txtDisplay = Entry(_main_, font=('times new roman', 32,"bold"), textvariable=text_Input,bd=10,insertwidth=72,bg="white",justify="center").grid(columnspan=10)

button_7=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="7", command=lambda:Click_button(7), bg="Black").grid(row=1,column=0)
button_8=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="8", command=lambda:Click_button(8),bg="Black").grid(row=1,column=1)
button_9=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="9",command=lambda:Click_button(9),bg="Black").grid(row=1,column=2)
button__add=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="+",command=lambda:Click_button("+"),bg="Black").grid(row=1,column=3)

button_4=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="4",command=lambda:Click_button(4),bg="Black").grid(row=2,column=0)
button_5=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="5",command=lambda:Click_button(5),bg="Black").grid(row=2,column=1)
button_6=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="6",command=lambda:Click_button(6),bg="Black").grid(row=2,column=2)
button__times=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="*",command=lambda:Click_button("*"),bg="Black").grid(row=2,column=3)

button_1=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="1",command=lambda:Click_button(1),bg="Black").grid(row=3,column=0)
button_2=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="2",command=lambda:Click_button(2),bg="Black").grid(row=3,column=1)
button_3=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="3",command=lambda:Click_button(3),bg="Black").grid(row=3,column=2)
button__minus=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="-",command=lambda:Click_button("-"),bg="Black").grid(row=3,column=3)

button_0=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="0",command=lambda:Click_button(0),bg="Black").grid(row=4,column=0)
button__clear=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="C",bg="Black",command=Backspace).grid(row=4,column=1)
button__equals=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="=",bg="Black",command=Equal).grid(row=4,column=2)
button__div=Button(_main_,padx=16,pady=8,bd=8, fg="Black",font=('times new roman',24,'bold'),text="/",command=lambda:Click_button("/"),bg="Black").grid(row=4,column=3)


_main_.mainloop()    


                                                  
    
