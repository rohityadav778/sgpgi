#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
name=f.getvalue('name')
fname=f.getvalue('fname')
gender=f.getvalue('gender')
number=f.getvalue('mobile')
email=f.getvalue('email')
address=f.getvalue('address')
#print name,fname,gender,mobile,email,address
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
#print con
q="update tbl_patient set name='"+name+"',fname='"+fname+"',gender='"+gender+"',mobile='"+number+"',address='"+address+"' where email='"+email+"'"
cur=con.cursor()
cur.execute(q)
print "<script>window.location.href='pprofile.py?id="+email+"';</script>"