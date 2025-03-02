from tkinter import*
from tkinter import messagebox
import csv
from datetime import datetime
from datetime import timedelta
from datetime import date
#import mysql.connector
root=Tk()
root.configure(background='black')
frame=Frame(root,height=700,width=900,bg="orange red") # creating the first frame
frame.place(relx=0.5,rely=0.5,anchor=CENTER)
u=StringVar() # for storing username
p=StringVar() # for storing password
c=StringVar() # for storing movie name
d=StringVar() #storing date
t=StringVar() #storing time
n=StringVar()# for storing theatre
m=StringVar()# for storing seats
l1=[]
def main():# main function which consist all the function 
    def create():# for creating a register page
        def gotomain():
            x=e2.get()
            y=e3.get()
            f=open("data.csv","a",newline="")
            w=csv.writer(f)
            w.writerow([x,y])
            f.close()
            global frame
            frame.destroy() 
            main()#for going back to the first page
        global frame
        frame.destroy()
        frame=Frame(root,height=700,width=800,bg="orange red")
        frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        l1=Label(frame,text="Register new account",font=("candara",30,"bold"))
        l1.place(relx=0.2,rely=0.1)
        l2=Label(frame,text="Username",bg="white")
        l3=Label(frame,text="Password",bg="white")
        l2.place(relx=0.1,rely=0.4)
        l3.place(relx=0.1,rely=0.5)
        l2.config(font=('Candara',30,"bold"))
        l3.config(font=('Candara',30,"bold"))
        e2=Entry(frame,font=('Candara',30))
        e3=Entry(frame,show="*",font=('Candara',30))
        e2.place(relx=0.4,rely=0.4)
        e3.place(relx=0.4,rely=0.5)
        button=Button(frame,text="Next",height=2,width=10,font=(10),command=gotomain,bd=5,relief="raised")
        button.place(relx=0.5,rely=0.6)
    
    def function():
        global c
        global d
        def click(name):
            global c
            c=name
            global frame
            frame.destroy() # destroying the second frame
            frame=Frame(root,height=700,width=800,bg="orange red") # creating the third frame
            frame.place(relx=0.5,rely=0.5,anchor=CENTER)
            function1()
        u=e2.get()
        
        p=e3.get()
        def func():
            file=open("data.csv","r")
            r=csv.reader(file)
            
            for i in r:
                if i[0]==u and i[1]==p:
                    break
            else:
                messagebox.showerror("CAUTION","username or password is incorrect")
                main()
        func()
        frame=Frame(root,height=700,width=800,bg="orange red") # creating the second frame
        frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        label=Label(frame,text=" Movie's list",font=("candara",30,"bold"),width=30)
        label.place(relx=0.1,rely=0.1)
        button1=Button(frame,text=" KGF 2 ",font=('candara',20,"bold"),width=30,command= lambda:click("KGF 2"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black") 
        button1.place(relx=0.1,rely=0.3)
        button2=Button(frame,text=" RRR ",font=('candara',20,"bold"),width=30,command= lambda: click("RRR"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button2.place(relx=0.1,rely=0.4)
        button3=Button(frame,text=" VIKRAM ",font=('candara',20,"bold"),width=30,command= lambda: click("VIKRAM"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button3.place(relx=0.1,rely=0.5)
        button4=Button(frame,text=" PONNIYIN SELVAN 1",font=('candara',20,"bold"),width=30,command= lambda: click("PONNIYIN SELVAN 1"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button4.place(relx=0.1,rely=0.6)
    def function1():
        global d
        def click(name):
            global d
            d=name
            global frame
            frame.destroy() # destroying the third frame
            frame=Frame(root,height=700,width=800,bg="orange red") # creating the fourth frame
            frame.place(relx=0.5,rely=0.5,anchor=CENTER)
            function3()
        Begindatestring = date.today()
        l=[]

        for i in range(6):
            Enddate = Begindatestring + timedelta(days=i)
            l.append(str(Enddate))
        frame=Frame(root,height=700,width=800,bg="orange red")#creating third frame
        frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        label=Label(frame,text="select date",font=("candara",30,"bold"),width=30)
        label.place(relx=0.1,rely=0.1)
        button5=Button(frame,text=l[0],font=('candara',20,"bold"),width=30,command= lambda:click(l[0]),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black") 
        button5.place(relx=0.1,rely=0.3)
        button6=Button(frame,text=l[1],font=('candara',20,"bold"),width=30,command= lambda: click(l[1]),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button6.place(relx=0.1,rely=0.4)
        button7=Button(frame,text=l[2],font=('candara',20,"bold"),width=30,command= lambda: click(l[2]),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button7.place(relx=0.1,rely=0.5)
        button8=Button(frame,text=l[3],font=('candara',20,"bold"),width=30,command= lambda: click(l[3]),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button8.place(relx=0.1,rely=0.6)
        button9=Button(frame,text=l[4],font=('candara',20,"bold"),width=30,command= lambda:click(l[4]),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black") 
        button9.place(relx=0.1,rely=0.7)
        button10=Button(frame,text=l[5],font=('candara',20,"bold"),width=30,command= lambda: click(l[5]),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button10.place(relx=0.1,rely=0.8)
    def function3():
        global n
        def click(name):
            global n
            n=name
            global frame
            frame.destroy() # destroying the fourth frame
            frame=Frame(root,height=700,width=800,bg="orange red") # creating the fifth frame
            frame.place(relx=0.5,rely=0.5,anchor=CENTER)
            function2()
        frame=Frame(root,height=700,width=800,bg="orange red")#creating fourth frame
        frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        label=Label(frame,text="Select the Theatre",font=("candara",30,"bold"),width=30)
        label.place(relx=0.1,rely=0.1)
        button5=Button(frame,text=" PVR ",font=('candara',20,"bold"),width=30,command= lambda:click("PVR"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black") 
        button5.place(relx=0.1,rely=0.3)
        button6=Button(frame,text=" SATHYAM ",font=('candara',20,"bold"),width=30,command= lambda: click("SATHYAM"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button6.place(relx=0.1,rely=0.4)
        button7=Button(frame,text=" AGS ",font=('candara',20,"bold"),width=30,command= lambda: click("AGS"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button7.place(relx=0.1,rely=0.5)
        button8=Button(frame,text=" MAYAJAL ",font=('candara',20,"bold"),width=30,command= lambda: click("MAYAJAL"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button8.place(relx=0.1,rely=0.6)
        button9=Button(frame,text=" ROHINI ",font=('candara',20,"bold"),width=30,command= lambda:click("ROHINI"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black") 
        button9.place(relx=0.1,rely=0.7)
        button10=Button(frame,text="LUXE CINEMAS ",font=('candara',20,"bold"),width=30,command= lambda: click("LUXE CINEMAS"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button10.place(relx=0.1,rely=0.8)
    def function2():
        global t
        def click(name):
            global t
            t=name
            global frame
            frame.destroy() # destroying the fourth frame
            frame=Frame(root,height=700,width=800,bg="orange red") # creating the fifth frame
            frame.place(relx=0.5,rely=0.5,anchor=CENTER)
            function4()
        frame=Frame(root,height=700,width=800,bg="orange red")#creating fourth frame
        frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        label=Label(frame,text="select time",font=("candara",30,"bold"),width=30)
        label.place(relx=0.1,rely=0.1)
        button11=Button(frame,text=" 9:30 AM",font=('candara',20,"bold"),width=30,command= lambda:click("9:30 AM"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black") 
        button11.place(relx=0.1,rely=0.3)
        button12=Button(frame,text=" 10:30 AM",font=('candara',20,"bold"),width=30,command= lambda: click("10:30 AM"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button12.place(relx=0.1,rely=0.4)
        button13=Button(frame,text=" 1:00 PM ",font=('candara',20,"bold"),width=30,command= lambda: click("1:00 PM"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button13.place(relx=0.1,rely=0.5)
        button14=Button(frame,text=" 2:20 PM ",font=('candara',20,"bold"),width=30,command= lambda: click("2:20 PM"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button14.place(relx=0.1,rely=0.6)
        button15=Button(frame,text=" 7:00 PM",font=('candara',20,"bold"),width=30,command= lambda: click("7:00 PM"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button15.place(relx=0.1,rely=0.4)
        button16=Button(frame,text="8:00 PM ",font=('candara',20,"bold"),width=30,command= lambda: click("8:00 PM"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button16.place(relx=0.1,rely=0.5)
        button17=Button(frame,text="10:00 PM ",font=('candara',20,"bold"),width=30,command= lambda: click("10:00 PM "),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button17.place(relx=0.1,rely=0.6)
        button18=Button(frame,text="11:00 PM ",font=('candara',20,"bold"),width=30,command= lambda: click("11:00 PM"),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button18.place(relx=0.1,rely=0.7)
        button19=Button(frame,text="10:00 PM ",font=('candara',20,"bold"),width=30,command= lambda: click("10:00 PM "),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
        button19.place(relx=0.1,rely=0.8)
        def function4():
            def cl1(name1):
                global frame
                frame.destroy() # destroying the fourth frame
                frame=Frame(root,height=700,width=800,bg="orange red") # creating the fifth frame
                frame.place(relx=0.5,rely=0.5,anchor=CENTER)
                function4()
          
            global l1
            
            def cl1(arg):
                if arg not in l1:
                    l1.append(arg)
                    
                #print(l1)    
                    
                if arg==1:
                    b1.config(bg="yellow")
                if arg==2:
                    b2.config(bg="yellow")
                if arg==3:
                    b3.config(bg="yellow")
                if arg==4:
                    b4.config(bg="yellow")
                if arg==5:
                    b5.config(bg="yellow")
                if arg==6:
                    b6.config(bg="yellow")
                if arg==7:
                    b7.config(bg="yellow")
                if arg==8:
                    b8.config(bg="yellow")
                if arg==9:
                    b9.config(bg="yellow")
                if arg==9:
                    b9.config(bg="yellow")
                if arg==10:
                    b10.config(bg="yellow")
                if arg==11:
                    b11.config(bg="yellow")
                if arg==12:
                    b12.config(bg="yellow")
                if arg==13:
                    b13.config(bg="yellow")
                if arg==14:
                    b14.config(bg="yellow")
                if arg==15:
                    b15.config(bg="yellow")
                if arg==16:
                    b16.config(bg="yellow")
                if arg==17:
                    b17.config(bg="yellow")
                if arg==18:
                    b18.config(bg="yellow")
                if arg==19:
                    b19.config(bg="yellow")
            frame=Frame(root,height=700,width=800,bg="orange red")
            frame.place(relx=0.5,rely=0.5,anchor=CENTER)
            label=Label(frame,text="SCREEN",font=("candara",30,"bold"),width=30)
            label.place(relx=0.1,rely=0.1)
            b1=Button(frame,text="1",height=5,state="disable",bg="grey",fg="white",width=10,command=lambda:cl1(1),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b1.place(x=100,y=200)
            b2=Button(frame,text="2",height=5,width=10,command=lambda:cl1(2),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b2.place(x=200,y=200)
            b3=Button(frame,text="3",height=5,width=10,command=lambda:cl1(3),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b3.place(x=300,y=200)
            b4=Button(frame,text="4",height=5,width=10,command=lambda:cl1(4),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b4.place(x=400,y=200)
            b5=Button(frame,text="5",height=5,width=10,command=lambda:cl1(5),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b5.place(x=500,y=200)
            b6=Button(frame,text="6",height=5,width=10,command=lambda:cl1(6),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b6.place(x=600,y=200)
            b7=Button(frame,text="7",height=5,state="disable",bg="grey",fg="white",width=10,command=lambda:cl1(7),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b7.place(x=100,y=400)
            b8=Button(frame,text="8",height=5,width=10,command=lambda:cl1(8),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b8.place(x=200,y=400)
            b9=Button(frame,text="9",height=5,width=10,command=lambda:cl1(9),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b9.place(x=300,y=400)
            b10=Button(frame,text="10",height=5,width=10,command=lambda:cl1(10),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b10.place(x=400,y=400)
            b11=Button(frame,text="11",height=5,width=10,command=lambda:cl1(11),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b11.place(x=500,y=400)
            b12=Button(frame,text="12",height=5,width=10,command=lambda:cl1(12),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b12.place(x=600,y=400)
            b13=Button(frame,text="13",height=5,width=10,command=lambda:cl1(13),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b13.place(x=100,y=600)
            b14=Button(frame,text="14",height=5,state="disable",bg="grey",fg="white",width=10,command=lambda:cl1(14),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b14.place(x=200,y=600)
            b15=Button(frame,text="15",height=5,width=10,command=lambda:cl1(15),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b15.place(x=300,y=600)
            b16=Button(frame,text="16",height=5,width=10,command=lambda:cl1(16),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b16.place(x=400,y=600)
            b17=Button(frame,text="17",height=5,width=10,command=lambda:cl1(17),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b17.place(x=500,y=600)
            b18=Button(frame,text="18",height=5,width=10,command=lambda:cl1(18),cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
            b18.place(x=600,y=600)
            button=Button(frame,text="Next",height=2,width=8,font=(10),command=function5,cursor="circle",bd=5,relief="raised",activebackground="blue",activeforeground="black")
            button.place(relx=0.9,rely=0.9)
        
        def function5():
            global n
            global c
            global d
            global n
            global l1
            l=str(l1)
            p1=len(l1)*200
            def destroy():
                try:
                    root.destroy()
                    con=mysql.connector.connect(host="localhost",user="root",password="dipaknaveen2010",database="movieticket ")
                    cur=con.cursor()
                    cur.execute("create table if not exists ticket(MovieName varchar(30),Date varchar(30),ShowTime varchar(30),Theatre varchar(30),Seats varchar(40),Cost int)")
                    cur.execute("insert into ticket values('{}','{}','{}','{}','{}',{})".format(c,d,t,n,l,p1))
                    con.commit()
                    con.close()
                except:
                    con=mysql.connector.connect(host="localhost",user="root",password="dipaknaveen2010")
                    cur=con.cursor()
                    cur.execute("create database MovieTicket")
                    con.close()
                    destroy()
                    
            root.attributes("-fullscreen",True)
            frame=Frame(root,height=700,width=900,bg="orange red") 
            frame.place(relx=0.5,rely=0.5,anchor=CENTER)
            l15=Label(frame,text="TICKET DETAILS",bg="white",font=("candara",30,"bold"),bd=8,relief="raised")
            l15.place(relx=0.2,rely=0.1)
            l1=Label(frame,text="MOVIE:",bg="white",font=("candara",27,"bold"),bd=6,relief="raised")
            l1.place(relx=0.2,rely=0.2)
            l2=Label(frame,text=c,bg="white",font=("candara",27,"bold"),bd=5,relief="raised")
            l2.place(relx=0.4,rely=0.2)
            l3=Label(frame,text="DATE:",font=("candara",27,"bold"),bd=6,relief="raised",bg="white")
            l3.place(relx=0.2,rely=0.3)
            l4=Label(frame,text=d,bg="white",font=("candara",27,"bold"),bd=5,relief="raised")
            l4.place(relx=0.4,rely=0.3)
            l5=Label(frame,text="TIME:",font=("candara",27,"bold"),bd=6,relief="raised",bg="white")
            l5.place(relx=0.2,rely=0.4)
            l6=Label(frame,text=t,font=("candara",27,"bold"),bd=5,relief="raised",bg="white")
            l6.place(relx=0.4,rely=0.4)
            l7=Label(frame,text="THEATRE:",font=("candara",27,"bold"),bd=6,relief="raised",bg="white")
            l7.place(relx=0.2,rely=0.5)
            l8=Label(frame,text=n,font=("candara",27,"bold"),bd=5,relief="raised",bg="white")
            l8.place(relx=0.4,rely=0.5)
            l9=Label(frame,text="SEATS:",font=("candara",27,"bold"),bd=6,relief="raised",bg="white")
            l9.place(relx=0.2,rely=0.6)
            l10=Label(frame,text=l,font=("candara",27,"bold"),bd=5,relief="raised",bg="white")
            l10.place(relx=0.4,rely=0.6)
            l11=Label(frame,text="PAYMENT:",font=("candara",27,"bold"),bd=6,relief="raised",bg="white")
            l11.place(relx=0.2,rely=0.7)
            l12=Label(frame,text=p1,font=("candara",27,"bold"),bd=5,relief="raised",bg="white")
            l12.place(relx=0.4,rely=0.7)
            l13=Label(frame,text="EACH TICKET:",font=("candara",17,"bold"),bd=5,relief="raised",bg="white")
            l13.place(relx=0.7,rely=0.7)
            l14=Label(frame,text="₹200",font=("candara",17,"bold"),bd=5,relief="raised",bg="white")
            l14.place(relx=0.9,rely=0.7)
            l15=Label(frame,text="Enjoy your movie !",font=("candara",25,"bold"),bd=5,relief="raised",bg="white")
            l15.place(relx=0.1,rely=0.9)
            button=Button(frame,text="close",height=2,width=5,font=("candara",15,"bold"),command=destroy,cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black",bg="white")
            button.place(relx=0.7,rely=0.9)        
    root.attributes("-fullscreen",True) # for displaying the window in full screen 
    frame=Frame(root,height=700,width=900,bg="orange red") # creating the first frame
    frame.place(relx=0.5,rely=0.5,anchor=CENTER)# for placing the frame in the center of the root window
    l1=Label(frame,text="MOVIE TICKET BOOKING",font=("candara",30,"bold"),bd=6,relief="raised")
    l1.place(relx=0.2,rely=0.1)
    l2=Label(frame,text="Email ID",bg="black",bd=5,relief="raised",fg="white")
    l3=Label(frame,text="Password",bg="black",bd=5,relief="raised",fg="white")
    l2.place(relx=0.1,rely=0.4)
    l3.place(relx=0.1,rely=0.5)
    l2.config(font=('Candara',30,"bold"))
    l3.config(font=('Candara',30,"bold"))
    e2=Entry(frame,font=('Candara',30),bd=5,relief="raised")
    e3=Entry(frame,show="*",font=('Candara',30),bd=5,relief="raised")
    e2.place(relx=0.4,rely=0.4)
    e3.place(relx=0.4,rely=0.5)
    button=Button(frame,text="Next",height=2,width=8,font=("candara",10,"bold"),command=function,cursor="circle",bd=5,relief="raised",activebackground="green",activeforeground="black")
    button.place(relx=0.5,rely=0.6)
    button1=Button(frame,text="Don't have an account click here",height=1,width=30,font=("candara",15,"bold"),cursor="circle",command=create,bd=5,relief="raised",activebackground="green",activeforeground="black")
    button1.place(relx=0.4,rely=0.7)
    root.mainloop()
main()
