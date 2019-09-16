#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/style.css">
<link rel="stylesheet" type="text/css" href="css/patient.css">
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css"> 
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="js/slider.js"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
<body onload="slide()" bgcolor="black">
	<div class="top-nav-bar">  
     <div  class="search-box">
     <img src="images/pgilogo.png" class="logo">
     <input type="text" class="form-control">
     <span class="input-group-text"><i class="fa fa-search"></i></span>
     </div>
	<div class="menu-bar">
	<ul>
	    <li><a href="index.html"></i>Home</a></li>
	    <li><a href="about.py">About</a></li>
	    <li><a href="contact.py">Contect</a></li>
	    <li><a href="doctor.py">Docter</a></li>
	    <li><a href="patient.py">Patient</a></li>
	    <li><a href="login.py">Login</a></li>
	</ul>
	</div>
</div>
	    <!-----------form stars here------------->
		<div class="outer">
	 <div class="r">
	  <h2><b>WELCOME TO SGPGI PATIENT REGISTRATION<h2>
	 </div>
   	   <div class="form">
   	   
   	     
   	    <div class="formbox">
        <form action="patientcode.py" method="post" style="margin-left:100px;">
          <span> Name</span></br>
          <input type="text" name="name" placeholder="Name">
		  <br/><br/>
           <span>Father Name</span></br>
           <input type="text" name="fname" placeholder="Father name">
           <br/><br/>
          <span>Gender &nbsp &nbsp
           <input type="radio" name="a" value="male">male
           <input type="radio" name="a" value="female">female</span>
            <br/><br/>
           <span> Email</span></br>
           <input type="email" name="email" placeholder="Email address"/>
		   <br/><br/>
           <span>Password</span></br>
           <input type="password" name="password" placeholder="Password"/>
		   <br/><br/>
            <span>Mobile No.</span></br>
           <input type="number" name="mobile" placeholder="Mobile number"/>
		   <br/><br/>
           <span>Address</span></br>
            <textarea name="address" style="height: 100px; width: 435px;">
           </textarea>
             <br/><br/>
             <div>
			 <a href="#"><input style="background-color:#2da5ca;height:40px;width:130px;" type="submit"/></a>
            </div>
           </form>
    </div>
   	   </div>
   </div>
	<!----------form ends here------------>
<div class="middle">
		     <h1>OUR BEST <span style="color:#2da5ca;font-size:40px;">SERVICES<span></h1>
			<p style="color:#000;">SGPGIMS is a great hospital in lucknow it has many branch
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
	   <p style="font-size:lighter;">Orthodontics and dentofacial orthopedics, 
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
<p style="color:#000;"> &copy copyright 2019 Allright Reserved By SGPGI /Designed by Rohit Yadav</p></center> 
</div>
</body>
</html>
"""