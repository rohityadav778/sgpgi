#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "hello"
print """
<html>
<head>
     <title></title>
<link rel="stylesheet" type="text/css" href="css/pupdate.css">
<link rel="stylesheet" type="text/css" href="css/style.css">
<link rel="stylesheet" type="text/css" href="css/contact.css">
<body>
<div id="main">
    <nav>
	<img src="images/pgilogo.png" style="width:120px;height:80px;">
	   <ul>
	      <li><a href="index.html">Home</a></li>
	      <li><a href="doctorviewprofile.py">View Appointment</a></li>
	      <li><a href="cancelappointment.py">Cancel Appointment</a></li>
	      <li><a href="doctorupdatelogin.py">Update Profile</a></li>
	      <li><a href="doctorchangepass.py">Change Password</a></li>
	      <li><a href="logout.py">Log Out</a></li>
	   </ul>
	</nav>
<center>
<table border="1" style="font-size:25px; width:800px; color:#fff;">
<h1>Edit Your Profile Here<h1/>
"""
import cgi,MySQLdb
e=cgi.FieldStorage().getvalue('id')
#print e
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
q="select * from tbl_doctor where email='"+e+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr><td>Name :</td><td>",r[1],"</td></tr>"
 print "<tr><td>Father Name :</td><td>",r[2],"</td></tr>"
 print "<tr><td>Gender :</td><td>",r[3],"</td></tr>"
 print "<tr><td>Mobile :</td><td>",r[6],"</td></tr>"
 print "<tr><td>Address :</td><td>",r[10],"</td></tr>"
 print "<tr><td>Reg. Date :</td><td>",r[11],"</td></tr>"
 print "<tr><td>Email :</td><td>",r[4],"</td></tr>"
 print "<tr><td colspan='2' align='center'><a href='dedit.py?id="+e+"'>Edit Profile</a></td></tr>"
print """
</table>
</center>
</div>
<div class="middle">
		     <h1>OUR BEST <span style="color:#2da5ca;">SERVICES<span></h1>
			<p>SGPGIMS is a great hospital in lucknow it has many branch
			divided it provide a great medicine facility it has many 
			great doctors it also have lift for the paten.Find 
			24 Hours Home Nursing Services,
			Senior Citizen Care Taker Services, Patient Care Takers, 95 Nurse
			Bureaus in Sgpgi Campus, Lucknow.</p>
			<a href="#"><button value="submit">Read more</button></a>
</div>
<div class="slidebar">
  <div class="left">
       <img src="images/s5.jpg">
	   <h2>Orthodontics</h2>
	   <hr/>
	   <p>Orthodontics and dentofacial orthopedics, 
	   formerly referred to as orthodontia, 
	   is a specialty of dentistry that deals with the diagnosis, 
	   prevention and correction of malpositioned teeth and jaws.
	   The field was established by such
	   pioneering orthodontists as Edward Angle and Norman William Kingsley.
	   Orthodontic treatment can focus on dental displacement only, 
	   or deal with the control and modification of facial growth. 
	   In the latter case it is better defined as "dentofacial orthopedics".
	   In severe malocclusions that can be a part of craniofacial abnormality, 
	   management often requires a combination of orthodontics 
	   with headgear or reverse pull facemask and/or jaw surgery.
	   deal with the control and modification of facial growth. 
	   In the latter case it is better defined as "dentofacial orthopedics".
	   In severe malocclusions that can be a part of craniofacial abnormality, 
	   management often requires a combination of orthodontics 
	   with headgear or reverse pull facemask and/or jaw surgery.
	   </p>
	   <a href="#"  style="color:red; text-color:red;"><p  style="color:#2da5ca;">Read more>></p></a>
    </div>
   <div class="mid"> 
	   <img src="images/s6.jpg">
	   <h2>Tooth Extraction</h2>
	   <hr/>
	   <p>Orthodontics and dentofacial orthopedics, 
	   formerly referred to as orthodontia, 
	   is a specialty of dentistry that deals with the diagnosis, 
	   prevention and correction of malpositioned teeth and jaws.
	   The field was established by such
	   pioneering orthodontists as Edward Angle and Norman William Kingsley.
	   Orthodontic treatment can focus on dental displacement only, 
	   or deal with the control and modification of facial growth. 
	   In the latter case it is better defined as "dentofacial orthopedics".
	   In severe malocclusions that can be a part of craniofacial abnormality, 
	   management often requires a combination of orthodontics 
	   with headgear or reverse pull facemask and/or jaw surgery.
	   In severe malocclusions that can be a part of craniofacial abnormality, 
	   management often requires a combination of orthodontics 
	   with headgear or reverse pull facemask and/or jaw surgery.
	   Orthodontic treatment can focus on dental displacement only, 
	   or deal with the control and modification of facial growth.
	   </p>
	   <a href="#"  style="color:red; text-color:red;">
	   <p style="color:#2da5ca;">Read more>></p></a>
  </div>
  <div class="right">
        <img src="images/s7.jpg">
		<h2>Dental Fillings</h2>
		<hr/>
	   <p>Orthodontics and dentofacial orthopedics, 
	   formerly referred to as orthodontia, 
	   is a specialty of dentistry that deals with the diagnosis, 
	   prevention and correction of malpositioned teeth and jaws.
	   The field was established by such
	   pioneering orthodontists as Edward Angle and Norman William Kingsley.
	   Orthodontic treatment can focus on dental displacement only, 
	   or deal with the control and modification of facial growth. 
	   In the latter case it is better defined as "dentofacial orthopedics".
	   In severe malocclusions that can be a part of craniofacial abnormality, 
	   management often requires a combination of orthodontics 
	   with headgear or reverse pull facemask and/or jaw surgery.
	   In severe malocclusions that can be a part of craniofacial abnormality, 
	   management often requires a combination of orthodontics 
	   with headgear or reverse pull facemask and/or jaw surgery.
	   </p>
	   <a href="#"  style="color:red; text-color:red;">
	   <p  style="color:#2da5ca;">Read more>></p></a>		
   </div>
</div>
<!-----------------Middle Sectoin End Here---------------------------------------->
<!-----------------footer Start Here---------------------------------------->
<div class="footer">
  <div class="f1">
      <h2>MEDICAL</h2>
	  <br/>
	 <p> &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Call Us : +1 718-955-2838 
	 <br/>
	 <br/>
	 &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  Raebareli Rd, Haibat Mau Mawaiya, <br/> &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Lucknow, Uttar Pradesh 226014 
	 <br/>
	 <br/>
	 &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp contect@gmail.com 
	 <br/>
	 <br/>
	  </p>
  </div>
  <div class="f2">
  <h2>Useful Links</h2><br/>
  <p>&nbsp &nbsp Life Insurance</p>
  <p>&nbsp &nbsp Home Insurance</p>
  <p>&nbsp &nbsp Child Insurance</p>
  <p>&nbsp &nbsp Family Health Plan</p>
  <p>&nbsp &nbsp Company Insurance</p>
  </div>
  <div class="f3">
  <h2>News And Media</h2><br/>
  <p>  News Hospital Campus <br/>
   Training Institute  <br/>
   Training Institute <br/>
     Media Contect  <br/>	
   Interviews  <br/>
      Events  </p>
  </div>
  </div>
  <div id="Copyright">
 <br/>
<p style="margin-left:-50px;">&copy copyright 2019 Allright Reserved By SGPGI /Designed by Rohit Yadav</p></center> 
</div>
</body>
</html>
<!-----------------footer End Here---------------------------------------->
"""