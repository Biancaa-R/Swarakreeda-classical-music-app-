#raagasukha
from tkinter import *
def rs():
    global score,cur,con,x
    from PIL import Image,ImageTk
    from tkinter import messagebox
    import pygame
    import mysql.connector as m
    con=m.connect(host='localhost',user='root',passwd='Chinmaiyee1$',database='swarakreeda')
    cur=con.cursor()
    pygame.mixer.init()
    score=0
    main1=Tk()
    main1.geometry('300x300')
    main1.title('RaagaSukha!')
    main1['bg']='purple'
    lb1=Label(main1,text='Raaga 1',bg='orange',font=('Pristina',20,'bold'))
    lb1.grid(row=0,column=0)
    cur.execute('select * from raagasukha where qno=1')
    j=cur.fetchall()
    x=IntVar(main1,value=0)
    for m in j:
        qno=m[0]
        q=m[1]
        audio=m[2]
        opt1,opt2,opt3,opt4=m[3],m[4],m[5],m[6]
        rt=[opt1,opt2,opt3,opt4]
    def play1():
        pygame.mixer.music.load(audio)
        pygame.mixer.music.play(loops=0)
    bp1=Button(main1,text='Play song',bg='orange',font=('Comic Sans MS',12),command=play1)
    bp1.grid(row=0,column=2)
    def stop1():
        pygame.mixer.music.stop()
    bs1=Button(main1,text='Stop song',bg='orange',font=('Comic Sans MS',12),command=stop1)
    bs1.grid(row=1,column=2)    
    for q in range(0,4):
        Radiobutton(main1,text=rt[q],value=q,variable=x,bg='orange',selectcolor='orange',font=('Book Antiqua',12),fg='purple',relief=RAISED).grid(row=q+1,column=0)
    con.commit()
    def nextraaga1():
        global score,cur,con,x
        cur.execute('select ans from raagasukha where qno=1')
        p=cur.fetchall()
        for k in p:
            l=k[0]
        
        if x.get()==l:
            score+=1
        main1.destroy()
        main2=Tk()
        main2.geometry('300x300')
        main2.title('RaagaSukha')
        main2['bg']='purple'
        lb2=Label(main2,text='Raaga 2',bg='orange',font=('Pristina',20,'bold'))
        lb2.grid(row=0,column=0)
        infobtn1=Button(main2,text='Info on Q1',bg='orange',font=('Berlin Sans FB',14),fg='purple',command=popup1)
        infobtn1.grid(row=0,column=1)
        y=IntVar(main2,value=0)
        cur.execute('select * from raagasukha where qno=2')
        j=cur.fetchall()
        for m in j:
            qno=m[0]
            q=m[1]
            audio=m[2]
            opt1,opt2,opt3,opt4=m[3],m[4],m[5],m[6]
            rt=[opt1,opt2,opt3,opt4]
        con.commit()
        for q in range(0,4):
            Radiobutton(main2,text=rt[q],value=q,bg='orange',font=('Book Antiqua',12),fg='purple',variable=y,selectcolor='orange',relief=RAISED).grid(row=q+1,column=0)
        def play2():
            pygame.mixer.music.load(audio)
            pygame.mixer.music.play(loops=0)
        def stop2():
            pygame.mixer.music.stop()
        bp2=Button(main2,text='Play song',bg='orange',font=('Comic Sans MS',12),command=play2)
        bp2.grid(row=1,column=1)
        bs2=Button(main2,text='Stop song',bg='orange',font=('Comic Sans MS',12),command=stop2)
        bs2.grid(row=2,column=1)
        
        def nextraaga2():
            global score,cur,con
            nonlocal y
            cur.execute('select ans from raagasukha where qno=2')
            p=cur.fetchall()
            for k in p:
                l=k[0]
            
            if y.get()==l:
                score+=1
            main2.destroy()
            main3=Tk()
            main3.geometry('300x300')
            main3.title('RaagaSukha')
            main3['bg']='purple'
            lb3=Label(main3,text='Raaga 3',bg='orange',font=('Pristina',20,'bold'))
            lb3.grid(row=0,column=0)
            
            g=IntVar(main3,value=0)
            cur.execute('select * from raagasukha where qno=3')
            j=cur.fetchall()
            for m in j:
                qno=m[0]
                q=m[1]
                audio=m[2]
                opt1,opt2,opt3,opt4=m[3],m[4],m[5],m[6]
                rt=[opt1,opt2,opt3,opt4]
            con.commit()
            for q in range(0,4):
                Radiobutton(main3,text=rt[q],value=q,bg='orange',font=('Book Antiqua',12),fg='purple',variable=g,selectcolor='orange',relief=RAISED).grid(row=q+1,column=0)
            def play3():
                pygame.mixer.music.load(audio)
                pygame.mixer.music.play(loops=0)
            def stop3():
                pygame.mixer.music.stop()
            bp3=Button(main3,text='Play song',bg='orange',font=('Comic Sans MS',12),command=play3)
            bp3.grid(row=1,column=1)
            bs3=Button(main3,text='Stop song',bg='orange',font=('Comic Sans MS',12),command=stop3)
            bs3.grid(row=2,column=1)
            def popup2():
                cur.execute('select info from raagasukha where qno=2')
                p=cur.fetchall()
                for k in p:
                    l=k[0]
                messagebox.showinfo('More to know!',l)
            infobtn2=Button(main3,text='Info on Q2',bg='orange',font=('Berlin Sans FB',14),fg='purple',command=popup2)
            infobtn2.grid(row=0,column=1)
            def nextraaga3():
                global score,cur,con
                nonlocal g
                cur.execute('select ans from raagasukha where qno=3')
                p=cur.fetchall()
                for k in p:
                    l=k[0]
                
                if g.get()==l:
                    score+=1
                main3.destroy()
                main4=Tk()
                main4.geometry('300x300')
                main4.title('RaagaSukha')
                main4['bg']='purple'
                lb4=Label(main4,text='Raaga 4',bg='orange',font=('Pristina',20,'bold'))
                lb4.grid(row=0,column=0)
                
                e=IntVar(main4,value=-3)
                cur.execute('select * from raagasukha where qno=4')
                j=cur.fetchall()
                for m in j:
                    qno=m[0]
                    q=m[1]
                    audio=m[2]
                    opt1,opt2,opt3,opt4=m[3],m[4],m[5],m[6]
                    rt=[opt1,opt2,opt3,opt4]
                con.commit()
                for q in range(0,4):
                    Radiobutton(main4,text=rt[q],bg='orange',font=('Book Antiqua',12),fg='purple',value=q,variable=e,selectcolor='orange',relief=RAISED).grid(row=q+1,column=0)
                def play4():
                    pygame.mixer.music.load(audio)
                    pygame.mixer.music.play(loops=0)
                def stop4():
                    pygame.mixer.music.stop()
                bp4=Button(main4,text='Play song',bg='orange',font=('Comic Sans MS',12),command=play4)
                bp4.grid(row=1,column=1)
                bs4=Button(main4,text='Stop song',bg='orange',font=('Comic Sans MS',12),command=stop4)
                bs4.grid(row=2,column=1)
                def popup3():
                    cur.execute('select info from raagasukha where qno=3')
                    p=cur.fetchall()
                    for k in p:
                        l=k[0]
                    messagebox.showinfo('More to know!',l)
                infobtn3=Button(main4,text='Info on Q3',bg='orange',font=('Berlin Sans FB',14),fg='purple',command=popup3)
                infobtn3.grid(row=0,column=1)
                
                def end():
                    global score,cur,con,img1
                    nonlocal e
                    cur.execute('select ans from raagasukha where qno=4')
                    p=cur.fetchall()
                    for k in p:
                        l=k[0]
                    if e.get()==l:
                        score+=1
                    main4.destroy()
                    main5=Tk()
                    main5.geometry('700x600')
                    main5.title('RaagaSukha Valedictory!')
                    cend=Canvas(main5,width=500,height=500,background='yellow')
                    cend.pack(fill='both',expand=True)
                    
                    query='select * from rsval where score={}'
                    if score==4:
                        cur.execute(query.format(score))
                        p=cur.fetchall()
                        for x in p:
                            j='Score='+str(x[0])+"."+' '+x[2]
                            m=x[1]
                        
                        img1=ImageTk.PhotoImage(Image.open(m),master=main5) 
                        cend.create_image(200,100, anchor='nw', image=img1) 
                        cend.create_text(300,50,text=j,font=('Lucida Calligraphy',15),fill='brown')
                        con.commit()
                    elif score==3:
                        cur.execute(query.format(score))
                        p=cur.fetchall()
                        for x in p:
                            j='Score='+str(x[0])+"."+' '+x[2]
                            m=x[1]
                        
                        img1=ImageTk.PhotoImage(Image.open(m),master=main5)  
                        cend.create_image(200,100, anchor='nw', image=img1) 
                        cend.create_text(300,50,text=j,font=('Lucida Calligraphy',15),fill='brown')
                        con.commit()
                    elif score==2:
                        cur.execute(query.format(score))
                        p=cur.fetchall()
                        for x in p:
                            j='Score='+str(x[0])+"."+' '+x[2]
                            m=x[1]
                        
                        img1=ImageTk.PhotoImage(Image.open(m),master=main5)
                        cend.create_image(200,100, anchor='nw', image=img1) 
                        cend.create_text(300,50,text=j,font=('Lucida Calligraphy',15),fill='brown')
                        con.commit()
                    elif score==0 or score==1:
                        cur.execute(query.format(score))
                        p=cur.fetchall()
                        for x in p:
                            j='Score='+str(x[0])+"."+' '+x[2]
                            m=x[1]
                        
                        img1=ImageTk.PhotoImage(Image.open(m),master=main5)
                        cend.create_image(200,100, anchor='nw', image=img1) 
                        cend.create_text(300,50,text=j,font=('Lucida Calligraphy',15),fill='brown')
                        con.commit()
                    def final():
                        main5.destroy()
                    finalbtn=Button(main5,text='End game!',bg='yellow',font=('Britannic Bold',20),command=final)
                    finalbtn_window=cend.create_window(300,400,anchor='nw',window=finalbtn)
                endbtn=Button(main4,text='Sampoornam',bg='orange',font=('Britannic Bold',20),command=end).grid(row=5,column=1)
            nextbtn3=Button(main3,text='Next raaga!',bg='orange',font=('Arial Rounded MT Bold',10),command=nextraaga3).grid(row=5,column=1)
        nextbtn2=Button(main2,text='Next raaga!',bg='orange',font=('Arial Rounded MT Bold',10),command=nextraaga2).grid(row=5,column=1)
    nextbtn1=Button(main1,text='Next raaga!',bg='orange',font=('Arial Rounded MT Bold',10),command=nextraaga1).grid(row=5,column=1)
    def popup1():
        cur.execute('select info from raagasukha where qno=1')
        p=cur.fetchall()
        for k in p:
            l=k[0]
        messagebox.showinfo('More to know!',l)


    main1.mainloop()
#rs()