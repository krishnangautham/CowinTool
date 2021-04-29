import requests
import schedule
import time, json, sys, configparser

config = configparser.ConfigParser()
config.read('prop.properties')

district_id = config.get("cowin", "district_id")
date = config.get("cowin", "date")
cowin_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + district_id + "&date=" + date

from_number = config.get("sinch", "from_number")
to_number = config.get("sinch", "to_number")
message_body = config.get("sinch", "message_body")
sinch_url = "https://sms.api.sinch.com/xms/v1/" + config.get("sinch", "sinch_service_plan_id")+ "/batches"
sinch_token = "Bearer " + config.get("sinch", "sinch_api_token")

type = "application/json"
data = {
    "from": from_number,
    "to": [to_number],
    "body": message_body
    }
payload = json.dumps(data)

def send_sms(): 
    headers = {'Content-Type': type, 'Authorization': sinch_token}
    response = None
    response = requests.post(sinch_url, headers = headers, data = payload)
    print(response) 
    
def find_vaccine_center():
    headers = {'Content-Type': type}
    response = None
    response = requests.get(cowin_url, headers = headers)
    output = response.content
    item_dict = json.loads(output)
    length = len(item_dict['centers'])
    print(length)
    if length>0 :
        send_sms()
        sys.exit()
    

schedule.every(10).seconds.do(find_vaccine_center)

while True:
    schedule.run_pending()
    time.sleep(1)
