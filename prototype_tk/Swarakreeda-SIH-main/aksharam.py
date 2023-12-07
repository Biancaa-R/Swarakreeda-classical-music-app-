from tkinter import *
def ak():
    global bgrs,con,cur
    #from tkinter import ttk
    import mysql.connector as m
    from PIL import ImageTk,Image
    tap=Tk()
    tap.title('Aksharam!')
    con=m.connect(host='localhost',user='root',passwd='Chinmaiyee1$',database='swarakreeda')
    cur=con.cursor()
    bgm=PhotoImage(file='D:\\12B\\CS\\proj board\\bg ak.png',master=tap)
    c1=Canvas(tap,width=500,height=500,bd=0,highlightthickness=0)
    c1.pack(fill='both',expand=True)
    c1.create_image(0,0,image=bgm,anchor='nw')
    options1=[]
    c1.create_text(90,110,text='Raaga',font=('Lucida Calligraphy',15,'bold'),fill='white')
    cur.execute('select raaga from madhuragaanam_aksharam')
    g=cur.fetchall()
    for y in g:
        for m in y:
            options1.append(m)
    def selectedr(event):
        global bgrs,con,cur
        toplevel1=Toplevel()
        toplevel1.title('Aksharam!')
        toplevel1.geometry('900x700')
        bgrs=PhotoImage(file='D:\\12B\\CS\\proj board\\bgrs resized.png',master=toplevel1)
        c2=Canvas(toplevel1,width=900,height=700,bd=0,highlightthickness=0)
        c2.pack(fill='both',expand=True)
        c2.create_image(0,0,image=bgrs,anchor='nw')
        cur=con.cursor()
        m=raaga.get()[:5]+'%'
        q="select * from madhuragaanam_aksharam where raaga like '{}'".format(m)
        cur.execute(q)
        ly=cur.fetchall()
        for x in ly:
            l='Raaga:'+x[0]+'       '+'Thalam:'+x[1]+'\n\n'+'Composer:'+x[2]+'    '+"Language:"+x[3]+'\n\n'+\
                x[-1]+'\n\n'+x[-2]
            c2.create_text(420,300,text=l,font=('Helvetica',13),fill='white')
        con.commit()
        def Exit():
            toplevel1.destroy()
        backbtn=Button(toplevel1,text='Back',font=('Merriweather',12),bg='light blue',fg='brown',command=Exit)
        backbtn_window=c2.create_window(600,600,anchor='nw',window=backbtn)

    raaga=StringVar()
    drop1=OptionMenu(tap,raaga,*options1,command=selectedr)
    drop1_window=c1.create_window(50,130,anchor='nw',window=drop1)
    options2=[]
    c1.create_text(350,110,text='Composer',font=('Lucida Calligraphy',15,'bold'),fill='white')
    cur.execute('select distinct composer from madhuragaanam_aksharam')
    j=cur.fetchall()
    for x in j:
        for m in x:
            options2.append(m)
    def selectedc(event):
        global bgrs,con,cur
        toplevel2=Toplevel()
        toplevel2.title('Aksharam!')
        toplevel2.geometry('900x700')
        bgrs=PhotoImage(file='D:\\12B\\CS\\proj board\\bgrs resized.png',master=toplevel2)
        c2=Canvas(toplevel2,width=900,height=700,bd=0,highlightthickness=0)
        c2.pack(fill='both',expand=True)
        c2.create_image(0,0,image=bgrs,anchor='nw')
        cur=con.cursor()
        m=comp.get()[:5]+'%'
        q="select * from madhuragaanam_aksharam where composer like '{}'".format(m)
        cur.execute(q)
        ly=cur.fetchall()
        for x in ly:
            l='Raaga:'+x[0]+'       '+'Thalam:'+x[1]+'\n\n'+'Composer:'+x[2]+'    '+"Language:"+x[3]+'\n\n'+\
                x[-1]+'\n\n'+x[-2]
            c2.create_text(420,300,text=l,font=('Helvetica',13),fill='white')
        con.commit()
        def Exit():
            toplevel2.destroy()
        backbtn=Button(toplevel2,text='Back',font=('Merriweather',12),bg='light blue',fg='brown',command=Exit)
        backbtn_window=c2.create_window(600,600,anchor='nw',window=backbtn)

    comp=StringVar()
    drop2=OptionMenu(tap,comp,*options2,command=selectedc)
    drop2_window=c1.create_window(300,130,anchor='nw',window=drop2)
    options3=[]
    c1.create_text(100,280,text='Language',font=('Lucida Calligraphy',15,'bold'),fill='white')
    cur.execute('select distinct language from madhuragaanam_aksharam')
    k=cur.fetchall()
    for z in k:
        for m in z:
            options3.append(m)
    def selectedl(event):
        global bgrs,con,cur
        toplevel3=Toplevel()
        toplevel3.title('Aksharam!')
        toplevel3.geometry('900x700')
        bgrs=PhotoImage(file='D:\\12B\\CS\\proj board\\bgrs resized.png',master=toplevel3)
        c2=Canvas(toplevel3,width=900,height=700,bd=0,highlightthickness=0)
        c2.pack(fill='both',expand=True)
        c2.create_image(0,0,image=bgrs,anchor='nw')
        cur=con.cursor()
        m=language.get()
        q="select * from madhuragaanam_aksharam where language like '{}'".format(m)
        cur.execute(q)
        ly=cur.fetchall()
        for x in ly:
            l='Raaga:'+x[0]+'       '+'Thalam:'+x[1]+'\n\n'+'Composer:'+x[2]+'    '+"Language:"+x[3]+'\n\n'+\
                x[-1]+'\n\n'+x[-2]
            c2.create_text(420,300,text=l,font=('Helvetica',13),fill='white')
        con.commit()
        def Exit():
            toplevel3.destroy()
        backbtn=Button(toplevel3,text='Back',font=('Merriweather',12),bg='light blue',fg='brown',command=Exit)
        backbtn_window=c2.create_window(600,600,anchor='nw',window=backbtn)

    language=StringVar()
    drop3=OptionMenu(tap,language,*options3,command=selectedl)
    drop3_window=c1.create_window(50,300,anchor='nw',window=drop3)
    options4=[]
    c1.create_text(330,280,text='Deity',font=('Lucida Calligraphy',15,'bold'),fill='white')
    cur.execute('select distinct deity from madhuragaanam_aksharam')
    c=cur.fetchall()
    for z in c:
        for m in z:
            options4.append(m)
    def selecteddeity(event):
        global bgrs,con,cur,b,f
        toplevel4=Toplevel()
        toplevel4.title('Aksharam!')
        toplevel4.geometry('900x700')
        bgrs=PhotoImage(file='D:\\12B\\CS\\proj board\\bgrs resized.png',master=toplevel4)
        c2=Canvas(toplevel4,width=900,height=700,bd=0,highlightthickness=0)
        c2.pack(fill='both',expand=True)
        c2.create_image(0,0,image=bgrs,anchor='nw')
        cur=con.cursor()
        d=deity.get()
        q="select * from madhuragaanam_aksharam where deity='{}'".format(d)
        cur.execute(q)
        ly=cur.fetchall()
        for x in ly:
            l='Raaga:'+x[0]+'       '+'Thalam:'+x[1]+'\n\n'+'Composer:'+x[2]+'    '+"Language:"+x[3]+'\n\n'+\
                    x[-1]+'\n\n'+x[-2]
            
            c2.create_text(420,300,text=l,font=('Helvetica',13),fill='white')
        con.commit()
        def Exit():
            toplevel4.destroy()
        backbtn=Button(toplevel4,text='Back',font=('Merriweather',12),bg='light blue',fg='brown',command=Exit)
        backbtn_window=c2.create_window(600,600,anchor='nw',window=backbtn)
    deity=StringVar()
    drop4=OptionMenu(tap,deity,*options4,command=selecteddeity)
    drop4_window=c1.create_window(300,300,anchor='nw',window=drop4)
    con.commit()
    tap.mainloop()
#ak()