#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
id=f.getvalue('id')
s=f.getvalue('s')
#print id,s
if s=='y':
 s='n'
else:
 s='y'
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
query="update tbl_appointment set status='"+s+"' where appid='"+id+"'"
a=cur.execute(query)
if a==1:
 print "<script>alert('Status Updated');window.location.href='cancelappointment.py';</script>"
else:
 "<script>alert('Status is Not Updated');window.location.href='cancelappointment.py';</script>"