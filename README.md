# CowinTool

This tool will continously check for vaccine center availability in real time and notify by sms about the availability so that the user can login and complete schedule process.

1. Get value for district id. District id values for kerala are given below. You can fetch other other state district ids from cowin portal.

       {"district_id":301,"district_name":"Alappuzha"},{"district_id":307,"district_name":"Ernakulam"},{"district_id":306,"district_name":"Idukki"},          {"district_id":297,"district_name":"Kannur"},{"district_id":295,"district_name":"Kasaragod"},{"district_id":298,"district_name":"Kollam"},{"district_id":304,"district_name":"Kottayam"},{"district_id":305,"district_name":"Kozhikode"},{"district_id":302,"district_name":"Malappuram"},{"district_id":308,"district_name":"Palakkad"},{"district_id":300,"district_name":"Pathanamthitta"},{"district_id":296,"district_name":"Thiruvananthapuram"},  {"district_id":303,"district_name":"Thrissur"},{"district_id":299,"district_name":"Wayanad"}

2. Signup at sinch - https://www.sinch.com/sign-up/ for messaging service. Use your mobile number where you want to get vaccine notification for registration at sinch.

3. Get "SERVICE PLAN ID", "API TOKEN" and "from number" from sinch after registration. Sinch gives a free trial of 2 EUROs for messaging services. You can upgrade your membership or register with a new number later if your usage exceeds the free trial. You can only send customised messages to your registered mobile number only using trial subscription.

4. Download script.py and prop.properties files. Give valid values for all the fields in prop.properties file.

5. Run "python script.py" from the location where you have downloaded script.py and prop.properties files. The machine should have python3 installed before running the script.

6. Screenshots are also attached on how to get values from sinch.

#Further scope of customisations

The tool is checking for center availability across a district. Further code customisations can be done to check availability for private facilities/specific centre or vaccine availability for min-age limit of 18 above etc. This logic can be applied inside method find_vaccine_center(): line no: 37 (item_dict = json.loads(output)).

Note: Once an available vaccine center is found, the tool will send the sms and will exit the process. User needs to restart the tool again if he still needs to monitor the availability. 
