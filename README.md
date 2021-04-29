# CowinTool

1. Register and signin at https://selfregistration.cowin.gov.in/ and get the token using chrome developer tools.
2. Get values for district id. District Id values for kerala are given below. You can fetch other other state district ids from cowin portal.
{"district_id":301,"district_name":"Alappuzha"},{"district_id":307,"district_name":"Ernakulam"},{"district_id":306,"district_name":"Idukki"},{"district_id":297,"district_name":"Kannur"},{"district_id":295,"district_name":"Kasaragod"},{"district_id":298,"district_name":"Kollam"},{"district_id":304,"district_name":"Kottayam"},{"district_id":305,"district_name":"Kozhikode"},{"district_id":302,"district_name":"Malappuram"},{"district_id":308,"district_name":"Palakkad"},{"district_id":300,"district_name":"Pathanamthitta"},{"district_id":296,"district_name":"Thiruvananthapuram"},{"district_id":303,"district_name":"Thrissur"},{"district_id":299,"district_name":"Wayanad"}
3.Signup at sinch - https://www.sinch.com/sign-up/ for messaging service. Use your mobile number where you want to get vaccine notification for registration at sinch.
4. Get "SERVICE PLAN ID", "API TOKEN" and "from number" from sinch after registration. Sinch gives a free trial of 2 EUROs for messaging services. You can upgrade your membership later if need to use more messaging service later.
5. Give values in propo.properties file.
