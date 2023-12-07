from tkinter import *
def ss():
    global ssscore,con,cur,x
    from PIL import ImageTk,Image
    import mysql.connector as m
    main2=Tk()
    main2.title('Musical Connections!')
    main2.geometry('800x650')
    main2['bg']='red'
    con=m.connect(host='localhost',user='root',passwd='Chinmaiyee1$',database='swarakreeda')
    cur=con.cursor()
    ssscore=0
    cur.execute('select * from sangeetha_sambandam where qno=1')
    j=cur.fetchall()
    con.commit()
    for x in j:
        qs1=x[1]
        ssimg1,ssimg2,ssimg3,ssimg4=x[2],x[3],x[4],x[5]
        opt1,opt2,opt3,opt4=x[6],x[7],x[8],x[9]
        ssl=[opt1,opt2,opt3,opt4]
    lbq1=Label(main2,text=qs1,font=('Pristina',20),fg='purple',bg='yellow').grid(row=0,column=0)
    cimg1=PhotoImage(file=ssimg1,master=main2)
    ciml1=Label(main2,image=cimg1).grid(row=1,column=0)
    cimg2=PhotoImage(file=ssimg2,master=main2)
    ciml2=Label(main2,image=cimg2).grid(row=1,column=1)
    cimg3=PhotoImage(file=ssimg3,master=main2)
    ciml3=Label(main2,image=cimg3).grid(row=2,column=0)
    cimg4=PhotoImage(file=ssimg4,master=main2)
    ciml4=Label(main2,image=cimg4).grid(row=2,column=1)
    con1=IntVar(main2,value=0)
    for j in range(0,4):
        Radiobutton(main2,text=ssl[j],variable=con1,value=j,bg='yellow',selectcolor='yellow',font=('Arial',12),fg='red',width=20,relief=RAISED).grid(row=j+3,column=0)
    def nextcon1():
        global ssscore,con,cur,cimg5,cimg6
        cur.execute('select ans from sangeetha_sambandam where qno=1')
        j=cur.fetchall()
        con.commit()
        for x in j:
            l=x[0]
        if con1.get()==l:
            ssscore+=1
        main2.destroy()
        main3=Tk()
        main3.title('Sangeetha Sambandam!')
        main3['bg']='red'
        cur.execute('select * from sangeetha_sambandam where qno=2')
        j=cur.fetchall()
        con.commit()
        for x in j:
            qs1=x[1]
            ssimg1,ssimg2=x[2],x[3]
            opt1,opt2,opt3,opt4=x[6],x[7],x[8],x[9]
            ssl=[opt1,opt2,opt3,opt4]
        lbq1=Label(main3,text=qs1,font=('Pristina',20),fg='purple',bg='yellow').grid(row=0,column=0)
        cimg5=ImageTk.PhotoImage(Image.open(ssimg1),master=main3)
        ciml5=Label(main3,image=cimg5).grid(row=1,column=0)
        cimg6=ImageTk.PhotoImage(Image.open(ssimg2),master=main3)
        ciml6=Label(main3,image=cimg6).grid(row=1,column=1)
        con2=IntVar(main3,value=0)
        for j in range(0,4):
            Radiobutton(main3,text=ssl[j],variable=con2,value=j,bg='yellow',selectcolor='yellow',font=('Arial',12),fg='red',width=20,relief=RAISED).grid(row=j+3,column=0)
        def r1():
            cur.execute('select reasoning from sangeetha_sambandam where qno=1')
            p=cur.fetchall()
            con.commit()
            for x in p:
                l=x[0]
            info1=Tk()
            info1.title('Reasoning!')
            info1['bg']='#add8e6'
            infolbl1=Label(info1,text=l,font=('Bradley Hand ITC',20),fg='green',bg='#add8e6').pack()
            def ok1des():
                info1.destroy()
            ok1=Button(info1,text='Ok!',font=('Andalus',18),fg='blue',bg='violet',command=ok1des).pack()
        cinfo1=Button(main3,text='Reason for Q1',font=('Berlin Sans FB',14),bg='yellow',fg='green',command=r1).grid(row=6,column=1)
        def nextcon2():
            global ssscore,con,cur,cimg7,cimg8
            cur.execute('select ans from sangeetha_sambandam where qno=2')
            j=cur.fetchall()
            con.commit()
            for x in j:
                l=x[0]
            if con2.get()==l:
                ssscore+=1
            

            main3.destroy()
            main4=Tk()
            main4.title('Sangeetha Sambandam!')
            main4['bg']='red'
            cur.execute('select * from sangeetha_sambandam where qno=3')
            j=cur.fetchall()
            con.commit()
            for x in j:
                qs1=x[1]
                ssimg1,ssimg2=x[2],x[3]
                opt1,opt2,opt3,opt4=x[6],x[7],x[8],x[9]
                ssl=[opt1,opt2,opt3,opt4]
            lbq7=Label(main4,text=qs1,font=('Pristina',20),fg='purple',bg='yellow').grid(row=0,column=0)
            cimg7=ImageTk.PhotoImage(Image.open(ssimg1),master=main4)
            ciml7=Label(main4,image=cimg7).grid(row=1,column=0)
            cimg8=ImageTk.PhotoImage(Image.open(ssimg2),master=main4)
            ciml8=Label(main4,image=cimg8).grid(row=1,column=1)
            con3=IntVar(main4,value=0)
            for j in range(0,4):
                Radiobutton(main4,text=ssl[j],variable=con3,value=j,bg='yellow',selectcolor='yellow',font=('Arial',12),fg='red',width=20,relief=RAISED).grid(row=j+3,column=0)
            def r2():
                cur.execute('select reasoning from sangeetha_sambandam where qno=2')
                p=cur.fetchall()
                con.commit()
                for x in p:
                    l=x[0]
                info1=Tk()
                info1.title('Reasoning!')
                info1['bg']='#add8e6'
                infolbl1=Label(info1,text=l,font=('Bradley Hand ITC',20),fg='green',bg='#add8e6').pack()
                def ok1des():
                    info1.destroy()
                ok1=Button(info1,text='Ok!',font=('Andalus',18),fg='blue',bg='violet',command=ok1des).pack()
            cinfo2=Button(main4,text='Reason for Q2',font=('Berlin Sans FB',14),bg='yellow',fg='green',command=r2).grid(row=6,column=1)
            def nextcon3():
                global ssscore,con,cur,cimg9,cimg10
                cur.execute('select ans from sangeetha_sambandam where qno=3')
                j=cur.fetchall()
                con.commit()
                for x in j:
                    l=x[0]
                if con3.get()==l:
                    ssscore+=1
                

                main4.destroy()
                main5=Tk()
                main5.title('Sangeetha Sambandam!')
                main5['bg']='red'
                cur.execute('select * from sangeetha_sambandam where qno=4')
                j=cur.fetchall()
                con.commit()
                for x in j:
                    qs1=x[1]
                    ssimg1,ssimg2=x[2],x[3]
                    opt1,opt2,opt3,opt4=x[6],x[7],x[8],x[9]
                    ssl=[opt1,opt2,opt3,opt4]
                lbq9=Label(main5,text=qs1,font=('Pristina',20),fg='purple',bg='yellow').grid(row=0,column=0)
                cimg9=ImageTk.PhotoImage(Image.open(ssimg1),master=main5)
                ciml9=Label(main5,image=cimg9).grid(row=1,column=0)
                cimg10=ImageTk.PhotoImage(Image.open(ssimg2),master=main5)
                ciml10=Label(main5,image=cimg10).grid(row=1,column=1)
                con4=IntVar(main5,value=0)
                for j in range(0,4):
                    Radiobutton(main5,text=ssl[j],variable=con4,value=j,bg='yellow',selectcolor='yellow',font=('Arial',12),fg='red',width=20,relief=RAISED).grid(row=j+3,column=0)
                def r3():
                    cur.execute('select reasoning from sangeetha_sambandam where qno=3')
                    p=cur.fetchall()
                    con.commit()
                    for x in p:
                        l=x[0]
                    info1=Tk()
                    info1.title('Reasoning!')
                    info1['bg']='#add8e6'
                    infolbl1=Label(info1,text=l,font=('Bradley Hand ITC',20),fg='green',bg='#add8e6').pack()
                    def ok1des():
                        info1.destroy()
                    ok1=Button(info1,text='Ok!',font=('Andalus',18),fg='blue',bg='violet',command=ok1des).pack()
                cinfo3=Button(main5,text='Reason for Q3',font=('Berlin Sans FB',14),bg='yellow',fg='green',command=r3).grid(row=6,column=1)
                def conend():
                    global ssscore,con,cur,img11
                    cur.execute('select ans from sangeetha_sambandam where qno=4')
                    j=cur.fetchall()
                    con.commit()
                    for x in j:
                        l=x[0]
                    if con4.get()==l:
                        ssscore+=1
                    
                    main5.destroy()
                    main6=Tk()
                    main6.title('Sangeetha Sambandam Valedictory!')
                    main6.geometry('700x550')
                    cend=Canvas(main6,width=500,height=500,background='yellow')
                    cend.pack(fill='both',expand=True)
                    query='select * from ssval where ssscore={}'
                    if ssscore==4:
                        cur.execute(query.format(ssscore))
                        p=cur.fetchall()
                        for x in p:
                            j='Score='+str(x[0])+'.'+' '+x[2]
                            m=x[1]
                        img11=ImageTk.PhotoImage(Image.open(m),master=main6) 
                        cend.create_image(100,100, anchor='nw', image=img11) 
                        cend.create_text(300,50,text=j,font=('Lucida Calligraphy',15),fill='brown')
                        con.commit()
                    elif ssscore==3:
                        cur.execute(query.format(ssscore))
                        p=cur.fetchall()
                        for x in p:
                            j='Score='+str(x[0])+'.'+' '+x[2]
                            m=x[1]
                        img11=ImageTk.PhotoImage(Image.open(m),master=main6) 
                        cend.create_image(100,100, anchor='nw', image=img11) 
                        cend.create_text(300,50,text=j,font=('Lucida Calligraphy',15),fill='brown')
                        con.commit()
                    elif ssscore==2 or ssscore==1 or ssscore==0:
                        cur.execute(query.format(ssscore))
                        p=cur.fetchall()
                        for x in p:
                            j='Score='+str(x[0])+'.'+' '+x[2]
                            m=x[1]
                        img11=ImageTk.PhotoImage(Image.open(m),master=main6) 
                        cend.create_image(100,100, anchor='nw', image=img11) 
                        cend.create_text(300,50,text=j,font=('Lucida Calligraphy',15),fill='brown')
                        con.commit()
                    def r4():
                        cur.execute('select reasoning from sangeetha_sambandam where qno=4')
                        p=cur.fetchall()
                        con.commit()
                        for x in p:
                            l=x[0]
                        info1=Tk()
                        info1.title('Reasoning!')
                        info1['bg']='#add8e6'
                        infolbl1=Label(info1,text=l,font=('Bradley Hand ITC',20),fg='green',bg='#add8e6').pack()
                        def ok1des():
                            info1.destroy()
                        ok1=Button(info1,text='Ok!',font=('Andalus',18),fg='blue',bg='violet',command=ok1des).pack()
                    def exitc():
                        main6.destroy()
                    exit2=Button(main6,text='Exit',font=('Arial Rounded MT Bold',20),fg='brown',bg='yellow',command=exitc)
                    exit2btn_window=cend.create_window(300,400,anchor='nw',window=exit2)
                    cinfo4=Button(main6,text='Reason for Q4',font=('Berlin Sans FB',14),bg='yellow',fg='green',command=r4)
                    cinfo4_window=cend.create_window(100,400,anchor='nw',window=cinfo4)
                cend=Button(main5,text='Sampoornam',font=('Britannic Bold',20),fg='green',bg='yellow',command=conend).grid(row=6,column=1)
            cnext3=Button(main4,text='Next Connect!',font=('Arial Rounded MT Bold',14),fg='brown',bg='yellow',command=nextcon3).grid(row=6,column=2)
        cnext2=Button(main3,text='Next Connect!',font=('Arial Rounded MT Bold',14),fg='brown',bg='yellow',command=nextcon2).grid(row=6,column=2) 
    cnext1=Button(main2,text='Next Connect!',font=('Arial Rounded MT Bold',14),fg='brown',bg='yellow',command=nextcon1).grid(row=6,column=1)  
    main2.mainloop()
#ss()