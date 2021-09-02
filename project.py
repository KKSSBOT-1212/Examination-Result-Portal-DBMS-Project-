import sqlite3

#conn=sqlite3.connect('project.db')
class my_database:
    def __init__(self,name):
        self.conn=sqlite3.connect(name)
        self.conn.execute('''CREATE TABLE student(id integer primary key,name text not null);''')
        self.conn.execute('''CREATE TABLE sem1(id integer primary key,sub1 integer,sub2 integer,
        sub3 integer,sub4 integer,sub5 integer);''')
        self.conn.execute('''CREATE TABLE sem2(id integer primary key,sub1 integer,sub2 integer,
        sub3 integer,sub4 integer,sub5 integer);''')
        self.conn.execute('''CREATE TABLE sem3(id integer primary key,sub1 integer,sub2 integer,
        sub3 integer,sub4 integer,sub5 integer);''')
        self.conn.execute('''CREATE TABLE sem4(id integer primary key,sub1 integer,sub2 integer,
        sub3 integer,sub4 integer,sub5 integer);''')
        self.conn.execute('''CREATE TABLE sem5(id integer primary key,sub1 integer,sub2 integer,
        sub3 integer,sub4 integer,sub5 integer);''')
        self.conn.execute('''CREATE TABLE sem6(id integer primary key,sub1 integer,sub2 integer,
        sub3 integer,sub4 integer,sub5 integer);''')
        self.conn.execute('''CREATE TABLE grade(first integer,second integer,points integer);''')
        self.conn.execute('''INSERT INTO grade(first,second,points) VALUES(91,100,10);''')
        self.conn.execute('''INSERT INTO grade(first,second,points) VALUES(81,90,9);''')
        self.conn.execute('''INSERT INTO grade(first,second,points) VALUES(71,80,8);''')
        self.conn.execute('''INSERT INTO grade(first,second,points) VALUES(61,70,7);''')
        self.conn.execute('''INSERT INTO grade(first,second,points) VALUES(51,60,6);''')
        self.conn.execute('''INSERT INTO grade(first,second,points) VALUES(41,50,5);''')
        self.conn.execute('''INSERT INTO grade(first,second,points) VALUES(0,40,0);''')
        x=self.conn.execute('''select * from grade;''')
        """for i in x.fetchall():
            print(i)"""
    def add_user(self,name,id1):
        query=self.conn.execute('''select * from student where student.id=? and student.name=?;''',[id1,name])
        if(len(query.fetchall())==0):
            self.conn.execute('''insert into student (id,name) values (?,?);''',[id1,name])
        print("enter which sem details u want to enter\n")
        sem=int(input())
        l=[]
        print("enter marks of 5 sem\n")
        l=list(map(int,input().split()))
        l=[id]+l
        n=[]
        n.append(id)
        for i in range(5):
            p=self.conn.execute('''select grade.points from grade where ? between grade.first and grade.second;''',[l[i+1]])
            for i in p:
                n.append(i[0])
        if(sem==1):
            self.conn.execute('''insert into sem1(id,sub1,sub2,sub3,sub4,sub5) values (?,?,?,?,?,?);''',n)
        if(sem==2):
            self.conn.execute('''insert into sem2(id,sub1,sub2,sub3,sub4,sub5) values (?,?,?,?,?,?);''',n)
        if(sem==3):
            self.conn.execute('''insert into sem3(id,sub1,sub2,sub3,sub4,sub5) values (?,?,?,?,?,?);''',n)
        if(sem==4):
            self.conn.execute('''insert into sem4(id,sub1,sub2,sub3,sub4,sub5) values (?,?,?,?,?,?);''',n)
        if(sem==5):
            self.conn.execute('''insert into sem5(id,sub1,sub2,sub3,sub4,sub5) values (?,?,?,?,?,?);''',n)
        if(sem==6):
            self.conn.execute('''insert into sem6(id,sub1,sub2,sub3,sub4,sub5) values (?,?,?,?,?,?);''',n)
    def results_publish(self):
        print("enter which sem results u want sorted sgpa\n")
        sem=int(input())
        print('------------------------------------------')
        if(sem==1):
            query=self.conn.execute('''select sem1.id,s.name,round(sem1.sub1+sem1.sub2+sem1.sub3+sem1.sub4+sem1.sub5,2) from sem1 join student s where sem1.id=s.id order by 3 DESC,1;''')
            for i in query:
                print(i[0],i[1],float(i[2]/5))
                print('-------------------------------------------')
        if(sem==2):
            query=self.conn.execute('''select sem2.id,s.name,round(sem2.sub1+sem2.sub2+sem2.sub3+sem2.sub4+sem2.sub5,2) from sem2 join student s where sem2.id=s.id order by 3 DESC,1;''')
            for i in query:
                print(i[0],i[1],float(i[2]/5))
                print('-------------------------------------------')
        if(sem==3):
            query=self.conn.execute('''select sem3.id,s.name,round(sem3.sub1+sem3.sub2+sem3.sub3+sem3.sub4+sem3.sub5,2) from sem3 join student s where sem3.id=s.id order by 3 DESC,1;''')
            for i in query:
                print(i[0],i[1],float(i[2]/5))
                print('-------------------------------------------')
        if(sem==4):
            query=self.conn.execute('''select sem4.id,s.name,round(sem4.sub1+sem4.sub2+sem4.sub3+sem4.sub4+sem4.sub5,2) from sem4 join student s where sem4.id=s.id order by 3 DESC,1;''')
            for i in query:
                print(i[0],i[1],float(i[2]/5))
                print('-------------------------------------------')
        if(sem==5):
            query=self.conn.execute('''select sem5.id,s.name,round(sem5.sub1+sem5.sub2+sem5.sub3+sem5.sub4+sem5.sub5,2) from sem5 join student s where sem5.id=s.id order by 3 DESC,1;''')
            for i in query:
                print(i[0],i[1],float(i[2]/5))
                print('-------------------------------------------')
        if(sem==6):
            query=self.conn.execute('''select sem6.id,s.name,round(sem6.sub1+sem6.sub2+sem6.sub3+sem6.sub4+sem6.sub5,2) from sem6 join student s where sem6.id=s.id order by 3 DESC,1;''')
            for i in query:
                print(i[0],i[1],float(i[2]/5))
                print('-------------------------------------------')

print('-----------------------------------')
print('Welcome To Basic Result Portal\n')
print('------------------------------------')
print('enter name of your university')
name=input()
ob1=my_database(name)
while(1):
    print('----------------------')
    print("1)To Add User")
    print("2)To retrive results\n")
    print('---------------------')
    x=int(input())
    if(x==1):
        print("enter id and name of user\n")
        id=int(input())
        name=input()
        ob1.add_user(name,id)
        continue
    if(x==2):
        ob1.results_publish()
        continue
    break



