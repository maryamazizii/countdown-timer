from tkinter import*
from tkinter import messagebox
win=Tk()
win.title('تایمرشمارش معکوس')
win.geometry('350x250+800+300')

#function

time=0
def set():
    global time 
    time=int(entry_time.get())

def reset():
    global time
    time=0
    lbl_timemakos.configure(text='')
    entry_time.delete(0,END)
    btn_set.configure(state=NORMAL)
    btn_start.configure(state=NORMAL)

def start():
    global time
    if time >= 0 :
        btn_set.configure(state=DISABLED)
        btn_start.configure(state=DISABLED)
        lbl_timemakos.configure(text=time)
        time-=1
        lbl_timemakos.after(1000,start)
        entry_time.delete(0,END)
               
    if time == 0 :
        lbl_timemakos.configure(text='')  
        messagebox.showinfo('information','زمان به اتمام رسید')
        btn_set.configure(state=NORMAL)
        btn_start.configure(state=NORMAL)
        lbl_timemakos.configure(text='')
 

lbl_timemakos=Label(win,font='tahoma 10 ',background='black',foreground='white',width=2)
lbl_timemakos.place(x=150,y=35)

lbl_time=Label(win,text='زمان رابرحسب ثانیه وارد کنید',font='tahoma 10 ')
lbl_time.place(x=10,y=85)


entry_time=Entry(win,width=25)
entry_time.place(x=180,y=88)

btn_set=Button(win,text='set',font='tahoma 10',width=7,command=set)
btn_set.place(x=50,y=140)

btn_start=Button(win,text='start',font='tahoma 10',width=7,command=start)
btn_start.place(x=130,y=140)

btn_reset=Button(win,text='reset',font='tahoma 10',width=7,command=reset)
btn_reset.place(x=210,y=140)



win.mainloop()
