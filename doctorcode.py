#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
#print n
fn=data.getvalue('fname')
#print fn
g=data.getvalue('a')
#print g
e=data.getvalue('email')
#print e
p=data.getvalue('password')
#print p
m=data.getvalue('mobile')
#print m
s=data.getvalue('specialization')
#print s
f=data.getvalue('fees')
#print f
t=data.getvalue('timing')
#print t
a=data.getvalue('address')
#print a
sum=data.getvalue('sum')
total=data.getvalue('t')

con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_doctor(name,fname,gender,email,password,mobile,specialization,fees,timing,address,date) values('"+n+"','"+fn+"','"+g+"','"+e+"','"+p+"','"+m+"','"+s+"','"+f+"','"+t+"','"+a+"',curdate())"
cur=con.cursor()
if sum==total:

 a=cur.execute(query)        
 con.commit()
 con.close()
 if a==1:
  print """
  <script>
   window.location.href="dprofile.py"
  </script>
  """
 else:
  print """
  <script>
   window.location.href="login.py"
  </script>
  """
else:
 print "<script>alert('Invalid Captcha');window.location.href='doctor.py';</script>"