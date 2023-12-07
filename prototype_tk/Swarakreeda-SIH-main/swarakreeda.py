# main page
from tkinter import *
from PIL import ImageTk,Image
import pygame
import mysql.connector as m
from raagasukha123 import rs 
from sang_s import ss        
from aksharam import ak     
root=Tk()
root.geometry('1500x1125')
root.title('Swarakreeda!')
bg=PhotoImage(file='D:\\12B\\CS\\proj board\\violin bgr resized.png')
c1=Canvas(root,width=800,height=600,bd=0,highlightthickness=0)
c1.pack(fill='both',expand=True)
c1.create_image(0,0,image=bg,anchor='nw')
c1.create_text(610,20,text='Take a deep dive into the ocean of carnatic music!',font=('Helvetica',20),fill='white')
en=Entry(root,width=20,font=('Book Antiqua',15),bg='#CC7722',text='Enter your name:',bd=0)
en.insert(0,'Enter your name:')
def click():
    if en.get()!='Enter your name:':
        l1=Label(c1,text='Welcome '+en.get()+'!',font=('Helvetica',15),fg='white',bg='#CC7722')
        l1_window=c1.create_window(120,160,anchor='nw',window=l1)
bdone=Button(root,text='Done',font=("Helvetica",12),fg='white',bg='#CC7722',command=click)
bdone_window=c1.create_window(160,110,anchor='nw',window=bdone)
en_window=c1.create_window(80,60,anchor='nw',window=en)
def entry_clear(e):
    if en.get()=='Enter your name:':
        en.delete(0,END)
en.bind('<Button-1>',entry_clear)
akr=PhotoImage(file='D:\\12B\\CS\\proj board\\aksharam.png')
ak_lb=Label(c1,image=akr)
def akf():
    ak()
ak_btn=Button(root,image=akr,command=akf)
ak_window=c1.create_window(500,246,anchor='nw',window=ak_btn)
ssr=PhotoImage(file='D:\\12B\\CS\\proj board\\ss resized.png')
ss_lb=Label(c1,image=ssr)
def ssf():
    ss()
ss_btn=Button(root,image=ssr,command=ssf)
ss_window=c1.create_window(100,250,anchor='nw',window=ss_btn)
rsr=PhotoImage(file='D:\\12B\\CS\\proj board\\raagasukha resized.png')
rs_lb=Label(c1,image=rsr)
def rsf():
    rs()
rs_btn=Button(root,image=rsr,command=rsf)
rs_window=c1.create_window(100,500,anchor='nw',window=rs_btn)
root.mainloop()
