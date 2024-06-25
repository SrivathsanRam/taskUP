from secrets_key import API_KEY
import json
import requests
import random


def calculate_proximity(address1,address2):
    header = {'Authorization': f"Bearer ${API_KEY}"}
    url1 = f"https://www.onemap.gov.sg/api/common/elastic/search?searchVal={address1}&returnGeom=Y&getAddrDetails=Y&pageNum=1"
    url2 = f"https://www.onemap.gov.sg/api/common/elastic/search?searchVal={address2}&returnGeom=Y&getAddrDetails=Y&pageNum=1"
    try:
        resp1 = requests.request("GET",url1,headers=header)
        resp2 = requests.request("GET",url2,headers=header)
        lat1 = json.loads(resp1.text)['results'][0]['LATITUDE']
        long1 = json.loads(resp1.text)['results'][0]['LONGITUDE']
        lat2 = json.loads(resp2.text)['results'][0]['LATITUDE']
        long2 = json.loads(resp2.text)['results'][0]['LONGITUDE']
        print(lat1,long1,lat2,long2)

        url = f"https://www.onemap.gov.sg/api/public/routingsvc/route?start={lat1}%2C{long1}&end={lat2}%2C{long2}&routeType=walk"
        #url = f"https://www.onemap.gov.sg/api/public/routingsvc/route?start={lat1}%2C{long1}&end={lat2}%2C{long2}&routeType=pt&date=08-13-2023&time=07%3A35%3A00&mode=TRANSIT&maxWalkDistance=1000"
        headers = {"Authorization": API_KEY}
        response = requests.request("GET",url,headers=headers)
        return (int(round(json.loads(response.text)['route_summary']["total_time"]/60,0)))
    except:
        pass
    
    return random.randint(1,10)

print(calculate_proximity('520828','520813'))