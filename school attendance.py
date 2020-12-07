import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root", password="privacyisamyth",database="gaurav")
cur=conn.cursor()
if conn.is_connected:
    print("connection successful")
else:
    print("connection issue")
_SQL = """SHOW TABLES LIKE 'ATTENDANCE'"""
cur.execute(_SQL)
results = cur.fetchone()
if results:
    print("table was found")
else:
    cur.execute("Create table attendance ( student_name varchar (20), dt date, status varchar (10))")
    conn.commit()
    print("no tables were found so new table was created  ")
import datetime
currentTime = datetime.datetime.now()
currentTime.hour
if currentTime.hour < 12:
     print('Good morning.')
elif 12 <= currentTime.hour < 18:
    print('Good afternoon.')
else:
     print('Good evening.')
print("========Welcome To Attendance Management System======")
def menu():
    print("press 1 for taking attendance  ")
    print("press 2 for showing attendance  ")
    print("press 3 for changing the entry  ")
    print("press 4 for clearing all the records  ")
    print ("press 5 to exit")
    ch=eval(input("Please enter your your choice  "))
    if ch==1:
       p=int(input("please enter the no. of students absent  "))
       for x in range(0,p):
         cur.execute("insert into attendance values(%s,curdate(),%s)",(input("enter absentee name  "),"absent"))
         conn.commit()
       l=int(input("please enter the no. of students present  "))
       for x in range(0,l):
          cur.execute("insert into attendance values(%s,curdate(),%s)",(input("enter student's  name  "),"present"))
          conn.commit()
       print("attendance taken")
       menu()
    elif ch==2:
        print("press 1 for attendance by date")
        print("press 2 for attendance by student")
        print("press 3 for attendance ratio")
        print("pess 4 for number of times a student is present/absent")
        print("press 5 for number of students present/absent between a date ")
        c=int(input("please enter your choice    "))
        if c==1:
            y=input("please enter date YYYY-MM-DD   ")
            cur.execute("select student_name,status from attendance where dt='"+y+"'")
            conn.commit
            print(cur.fetchall())
            menu()
        if c==2:
            yt=input("enter student's name    ")
            cur.execute("select dt,status from attendance where student_name='"+yt+"'")
            print(cur.fetchall())
            menu()
        if c==3:
            cur.execute("select status,count(*) as entries from attendance group by status")
            print(cur.fetchall())
            menu()
        if c==4:
            print("enter a for number of times a student is absent")
            print("enter p for number of times a student is present")
            le=input("please enter your choice ")
            if le=="a":
                cur.execute("select count(*) from attendance where status like %s and student_name = %s",
                            ("absent",input("enter students name  ")))
                print(cur.fetchall())
                menu()
            if le=="p":
                cur.execute("select count(*) from attendance where status like %s and student_name = %s",
                            ("present",input("enter students name  ")))
                print(cur.fetchall())
                menu()
        if c==5:
            print("press 1 for  number of student absent between a date")
            print("press 2 for  number of student present between a date")
            inp=int(input("please enter your choice   "))
            if inp==1:
              cur.execute('select count(*) from attendance where status like %s and dt between %s and %s',
                          ("absent",input(" enter starting date YYYY-MM-DD "),input("enter ending date YYYY-MM-DD  ")))
              print(cur.fetchall())
              menu()
            if inp==2:
                 cur.execute('select count(*) from attendance where status like %s and dt between %s and %s',
                          ("present",input(" enter starting date YYYY-MM-DD "),input("enter ending date YYYY-MM-DD  ")))
                 print(cur.fetchall())
                 menu()
    elif ch==3:
        y=input("enter the student's name  ")
        zz= input("enter the date you want to change the entry of  ")
        xo=input("enter the new entry, i.e absent/present   ")
        cur.execute('update attendance set status =%s where student_name like %s and dt = %s',
                    (xo,y,zz))
        conn.commit()
        print("the new entry is succesfully saved")
        menu()
    elif ch==4:
        print("please note that this process is not at all reversible  ")
        uwu=input("enter yes if you want to continue ")
        password="barcabarcabarca"
        if uwu=="yes":
            j=input("enter the password")
            if j==password:
                cur.execute('truncate attendance')
                conn.commit()
                print("data succesfully delted")
                menu()
        else:
            menu()
    elif ch==5:
        currentTime = datetime.datetime.now()
        currentTime.hour
        if currentTime.hour < 12:
           print('Have a good day ahead ')
        elif 12 <= currentTime.hour < 18:
           print('Good afternoon.')
        else:
         print('Good night')
        
menu()