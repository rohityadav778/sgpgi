#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
id=data.getvalue('id')
#print id
name=data.getvalue('ptname')
#print name
appdate=data.getvalue('dt')
#print appdate
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_appointment(doc_id,pname,doa,date,status) values('"+id+"','"+name+"','"+appdate+"',curdate(),'y')"
cur=con.cursor()
a=cur.execute(query)
con.commit()
con.close()
#print "thanks"
if a==1:
 print "<script>alert('Appointment Book Sucessfully');window.location.href='pprofile.py';</script>"
else:
 print "<script>alert('Appointment not Book Sucessfully');window.location.href='appointment.py';</script>"