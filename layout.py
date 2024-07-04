#step 1 import modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
import os
import csv
# upgrdess
import pyqrcode
import png
from pyqrcode import QRCode
img=None

#step2 create obj of tk

width,height,xpos,ypos=600,400,300,150
win=Tk()
win.title('Resume App')
win.geometry('{}x{}+{}+{}'.format(width,height,xpos,ypos))

name=StringVar()
gender=StringVar(value='M')
hindi=StringVar(value='N')
english=StringVar(value='N')
city=StringVar()

def showClick():
    message=None
    
    if gender.get()=='M':
        message='Name: Mr.' + name.get() +'\n'
    else: 
        message='Name: Ms.'+name.get()+'\n'
    if hindi.get=='Y':
        message+='You can speak:Hindi\n'
    if english.get()=='Y':
        message+='can speak in English\n'
    message+='Your city is'+ city.get()
    messagebox.showinfo('You have entered',message)

#UPGRADES
    t1.delete("1.0","end")
    t1.insert("1.0",message)
    messagebox.showinfo('You have entered',message)
#new logic to display code'
    url=pyqrcode.create(message)
    filename=name.get()+".png"
    url.png(filename,scale=5)
    print('QR Code generated at', os.getcwd())
    global img
    img=PhotoImage(file=filename)
   # lblImage.config(image=img)
def emptyFields():

     name.set(value='')
     gender.set(value='')
     hindi.set(value='N')
     english.set(value='N')
     city.set(value='Bhopal')

        
def saveClick():
    
    data="{},{},{},{},{}\n".format(name.get(),gender.get(),hindi.get(),english.get(),city.get())
    confirm=askyesno(title='Does data is correct',message=data)
    if not confirm:
        return
    with open('resume2.csv','a') as f:
        f.write(data)
    messagebox.showinfo('success','data saved')
    name.set(value='')
    gender.set(value='M')
    hindi.set(value='N')
    english.set(value='N')
    city.set(value='Bhopal')

def saveclick2():
    data=[]
    data.append(name.get())
    data.append(gender.get())
    data.append(hindi.get())
    data.append(english.get())
    data.append(city.get())
    Confirm=askyesno(title='Does data is correct',message=data)
    if not Confirm:
        return
    f=None
    if os.path.exists('resumes.csv'):
        f=open('resumes.csv','a',encoding='UTF8')
    else:
        f=open('resumes.csv','a','w',encoding='UTF8')

        writer=csv.writer(f)
        writer.writerrow(data)
        f.close()
        messagebox.showinfo('Success','Data saved')
        emptyFields()
        # funtion to genrate html 
    def htmlClick():
        salutation='Mr.'if gender.get()=='M'else 'Ms.'
        h='Hindi' if hindi.get()=='Y' else ''
        e='English' if english.get()=='Y' else ''
        filename=name.get()+".png"
        global img
        if not os.path.exists(filename):
            showClick()
        img=PhotoImage(file=filename)
        print('QR code generated at',os.getcwd())
        html=""
       # <html>
                       
#step5 design the layout
Label(win,text='Enter name').grid(row=0,column=0)
Entry(win,width=30,textvariable=name).grid(row=0,column=1,padx=10,pady=10)

Label(win,text='select gender').grid(row=1,column=0)
Radiobutton(win,text='Male',variable=gender,value='M').grid(row=1,column=1)
Radiobutton(win,text='Female',variable=gender,value='F').grid(row=1,column=2)

Label(win,text='Language you speak').grid(row=2,column=0)
Checkbutton(win,text='Hindi',variable=hindi,onvalue='Y',offvalue='N').grid(row=2,column=1)
Checkbutton(win,text='English',variable=english,onvalue='Y',offvalue='N').grid(row=2,column=2)

Label(win,text='Select your city').grid(row=3,column=0)
c1=ttk.Combobox(win,width=30,textvariable=city)
c1.grid(row=3,column=1)
c1['values']=('Bhopal','Ujjain','Indore')
c1.current(2)

Button(win,text='show Data',command=showClick).grid(row=4,column=0,pady=10)
Button(win,text='save Data',command=saveClick).grid(row=4,column=1)

fra=LabelFrame(win,text='Preview')
fra.grid(row=5,column=0,columnspan=2,padx=30)
Label(fra,text='You have entered').pack()
t1=Text(fra,width=60,height=5)
t1.pack()

#creating menu 

menubar=Menu(win)
file=Menu(menubar)
help=Menu(menubar,tearoff=0)

#now add command actions inside menubar
file.add_command(label='show',command=showClick)
file.add_command(label='save',command=saveClick)
help.add_command(label='About us',command=showClick)
help.add_separator()
help.add_command(label='exit',command=win.quit)

#finally add menu nside menubar
menubar.add_cascade(label='File',menu=file)
menubar.add_cascade(label='Help',menu=help)
win.config(menu=menubar)
win.mainloop()