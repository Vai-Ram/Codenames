from random import *
from tkinter import *
import tkinter.font as font
import csv

clue_count=0

def cluesubmit():
   
    name=name_var.get()
    global clue_count
    global row_num
    global col_num

    row_number=row_num
    col_number=col_num
    
    if name in '                                                                                               ':
        pass
    else:
        l=Label(text= name,font=('Arial',25),fg='black', bg='yellow')
        l.grid(row=row_number,column=col_number)
        row_num=row_number+1
        clue_count+=1   
        
    if row_number == 4:
        col_num = 11
        row_num = 1
    if row_number == 4 and col_number == 11:
        col_num = 10
        row_num = 1
    if clue_count>=9:
        gameover()
    operativeclick()
    
mode='spymaster'

def spymasterclick():
    global lg
    global lb
    global l3
    global clue_count
    global mode
    for i in range(len(l3)):
        l3[i]['state']=NORMAL
        
    for i in range(len(lb)):
        lb[i]['bg']='black'
        lb[i]['fg']='white'
        
    for i in range(len(lg)):
        lg[i]['bg']='#4CBB17'
        lg[i]['fg']='black'
    mode='spymaster'    
    if clue_count>=8:
        gameover()
        
def operativeclick():
    global l3
    global lg2
    for i in range(len(l3)):
        l3[i]['bg']='#FFFDD0'
        l3[i]['fg']='black' 
        l3[i]['state']=NORMAL 
        
    global mode    
    mode='operative'    

        
def greenClick(b):
    global mode
    global l3
    global lg
    if mode=='operative':
        lg.remove(b)
        l3.remove(b)
        b['bg']='#4CBB17'
        b['fg']='#4CBB17'
    else:
        pass
    if lg==[]:
        win()
    
def blackClick(b):
    global l3
    global lb
    global mode
    if mode=='operative':
        gameover()  
    else:
        pass
    
def beigeClick(b):
    global l3    
    global lo
    global mode
    if mode=='operative':
        l3.remove(b)
        b['bg']='#FFFDD0'
        b['fg']='#FFFDD0'
        for i in range(len(l3)):
            l3[i]['state']=DISABLED
          
            
def gameover():
    for i in range(7):
        for j in range(7):
            if i==2 and j==2:
                lbl=Label(m, text='GAME OVER',width=10, height=3, bg='black', fg='white', font=('Arial',38)).grid(row=2,column=2) 
            else:
                lbl=Label(m, text='               ', bg='black',width=10, height=3 ,font=('Arial',38)).grid(row=i,column=j)

def win():
    for i in range(7):
        for j in range(7):
            if i==2 and j==2:
                lbl=Label(m, text='YOU WIN!',width=10, height=3, bg='black', fg='white', font=('Arial',38)).grid(row=2,column=2) 
            else:
                lbl=Label(m, text='               ', bg='black',width=10, height=3 ,font=('Arial',38)).grid(row=i,column=j)


m=Tk()
m.title('Codenames')
lab1=Label(text='                ').grid(row=2,column=0)
lab2=Label(text='                ').grid(row=2,column=2)
lab3=Label(text='', width=10, height=0).grid(row=2,column=9)
lab4=Label(text='', width=10, height=0).grid(row=2,column=11)

lab5=Label(text='          ', width=10, height=5).grid(row=0,column=5)
lab6=Label(text='          ', width=10, height=5).grid(row=6,column=5)
lab7=Label(text='          ', width=10, height=5).grid(row=6,column=12)

bg=PhotoImage(file='background_csproject3.png')
bg_lbl=Label(m,image=bg).grid(row=0,column=0,rowspan=1000,columnspan=1000)

name_var=StringVar()
row_num=1
col_num=10

font=font.Font(size=15, family='arial')

b1=Button(m, text='Spymaster',width=15, height=3, bg='#5d16be', fg='white', font=('Arial','19'), relief='ridge',bd=7, command = spymasterclick).grid(row=4,column=1)
b1_border = Frame(m, highlightbackground = "gold", highlightthickness = 20, bd=5).grid(row=4,column=1)
spm_pic = PhotoImage(file = "Spymaster_Picture2.png")
spy_lbl=Label(m, image=spm_pic).grid(row=5,column=1, rowspan=2)

b2=Button(m, text='Operative',width=15, height=3, bg='#0F52BA', fg='white', font=('Arial','19'), relief='ridge',bd=7,  command = operativeclick).grid(row=2,column=1)
b1_border = Frame(m, highlightbackground = "silver", highlightthickness = 20, bd=5).grid(row=2,column=1)
op_pic = PhotoImage(file = "Operative_Picture2.png")
op_lbl=Label(m, image=op_pic).grid(row=0,column=1, rowspan=2)

entry1 = Entry(m,width=12,textvariable = name_var, bg='#B6D0E2', fg='black',relief='sunken',bd=5, font=('Arial',38))

entry1.grid(row=5,column=10)

sub_btn=Button(m, text='enter',width=10, height=2, bg='#3FFF00', fg='black', relief='raised', bd=5, font=font, command = cluesubmit)
sub_btn.grid(row=5,column=11)

l2=[] 
l=[]
with open('Codenames.csv', mode ='r')as file:
    csvfile=csv.reader(file)
    for i in csvfile:
        for j in range(1,len(i)):
            l.append(i[j])

for i in range(25):
    a=randint(0,49-i)
    b=l[a]
    del l[a]
    l2.append(b)
    
x=0
l3=[]
for i in range(1,6):
    for j in range(3,8):
        btn = Button(m, text=l2[x],width=10, height=4, bg='#FFFDD0', relief='ridge',bd=5, font=font)
        
        l3.append(btn)
        btn.grid(row=i,column=j)
        x+=1
        
lo=[]
for i in range(25):
    lo.append(l3[i])
    
lg=[]
for i in range(9):
    a=randint(0,24-i)
    b=lo[a]
    del lo[a]
    lg.append(b)

lb=[]    
for i in range(3):
    a=randint(0,15-i)
    b=lo[a]
    del lo[a]
    lb.append(b)

for i in range(3):
    lb[i]['bg']='black'
    lb[i]['fg']='white'
    lb[i]['activebackground']='#36454F'
 
for i in range(9):
    lg[i]['bg']='#4CBB17'
    lg[i]['fg']='black'
    lg[i]['activebackground']='#7CFC00'
    
#green buttons
btn1 = lg[0]
btn2 = lg[1] 
btn3 = lg[2]
btn4 = lg[3]  
btn5 = lg[4]
btn6 = lg[5]  
btn7 = lg[6]
btn8 = lg[7]
btn9 = lg[8]     

btn1['command']=lambda: greenClick(btn1)
btn2['command']=lambda: greenClick(btn2)
btn3['command']=lambda: greenClick(btn3)
btn4['command']=lambda: greenClick(btn4)
btn5['command']=lambda: greenClick(btn5)
btn6['command']=lambda: greenClick(btn6)
btn7['command']=lambda: greenClick(btn7)
btn8['command']=lambda: greenClick(btn8)
btn9['command']=lambda: greenClick(btn9)


#black buttons
btn10 = lb[0]
btn11 = lb[1] 
btn12 = lb[2]

btn10['command']=lambda: blackClick(btn10)
btn11['command']=lambda: blackClick(btn11)
btn12['command']=lambda: blackClick(btn12)


#beige buttons
btn13= lo[0]
btn14= lo[1] 
btn15= lo[2]
btn16= lo[3]  
btn17= lo[4]
btn18= lo[5]  
btn19= lo[6]
btn20= lo[7]
btn21= lo[8]   
btn22= lo[9]
btn23= lo[10]
btn24= lo[11] 
btn25= lo[12]  

btn13['command']=lambda: beigeClick(btn13)
btn14['command']=lambda: beigeClick(btn14)
btn15['command']=lambda: beigeClick(btn15)
btn16['command']=lambda: beigeClick(btn16)
btn17['command']=lambda: beigeClick(btn17)
btn18['command']=lambda: beigeClick(btn18)
btn19['command']=lambda: beigeClick(btn19)
btn20['command']=lambda: beigeClick(btn20)
btn21['command']=lambda: beigeClick(btn21)
btn22['command']=lambda: beigeClick(btn22)
btn23['command']=lambda: beigeClick(btn23)
btn24['command']=lambda: beigeClick(btn24)
btn25['command']=lambda: beigeClick(btn25)

m.mainloop()