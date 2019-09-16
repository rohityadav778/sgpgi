#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "hello"
import cgi,MySQLdb
data=cgi.FieldStorage()
email=data.getvalue('email')
oldpass=data.getvalue('oldpass')
newpass=data.getvalue('newpass')
cpass=data.getvalue('cpass')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
st="false"
query="select password from tbl_patient where email='"+email+"'"
cur.execute(query)
res=cur.fetchall()
print res
p=""
for r in res:
 p=r[0]
 st="true"
 if newpass==cpass and oldpass==p and st=="true":
  q="update tbl_patient set password='"+newpass+"' where email='"+email+"'"
  print q
  n=cur.execute(q)
  if n==1:
   print "<script>alert('New Password Updated'); window.location.href='pprofile.py';</script>"
  else:
   print "<script>alert('Password Not Updated'); window.location.href='changepass.py';</script>"
 else:
  print "<script>alert('New Password or Old Password is not matched'); window.location.href='changepass.py';</script>"