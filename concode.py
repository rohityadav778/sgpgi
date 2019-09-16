#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
#print n
e=data.getvalue('email')
#print e
num=data.getvalue('number')
#print num
m=data.getvalue('massage')
#print m
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_contact(name,email,mobile,massage,date) values('"+n+"','"+e+"','"+num+"','"+m+"',curdate())"
cur=con.cursor()
a=cur.execute(query)
con.commit()
con.close()
if a==1:
 print """
 <script>
  alert('Massage Send');
  window.location.href="contact.py"
 </script>
 """
else:
 print """
 <script>
  alert('Massage Not Send');
  window.location.href="contact.py"
 </script>
 """