#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Code wala page"
import cgi
import MySQLdb
data=cgi.FieldStorage()
sl=data.getvalue('login')
#print sl
e=data.getvalue('email')
#print e
p=data.getvalue('password')
#print p
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
if sl=="Doctor":
	query="select * from tbl_doctor where email='"+e+"' and password='"+p+"'"
	cur=con.cursor()
	a=cur.execute(query)
	con.commit()
	con.close()
	if a==1:
		print"""
		<script>
			window.location.href="dprofile.py"
		</script>
		"""
	else:
		print"""
		<script>
			window.location.href="login.py"
		</script>
		"""
if sl=="Patient":
	query="select * from tbl_patient where email='"+e+"' and password='"+p+"'"
	cur=con.cursor()
	b=cur.execute(query)
	con.commit()
	con.close()
	if b==1:
		print"<script>window.location.href='pprofile2.py?id="+e+"'</script>"
	else:
		print"<script>window.location.href='login.py'</script>"