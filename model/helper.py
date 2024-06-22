API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjYWZlNWY4Nzc4MjEyNDY1ZTU4MDE4NTJkNWZkY2JhMSIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC0xMjIzNjk4OTkyLmFwLXNvdXRoZWFzdC0xLmVsYi5hbWF6b25hd3MuY29tL2FwaS92Mi91c2VyL3Bhc3N3b3JkIiwiaWF0IjoxNzE5MDQ0MTk2LCJleHAiOjE3MTkzMDMzOTYsIm5iZiI6MTcxOTA0NDE5NiwianRpIjoiM3RIb3dmbWNrNFlicTNEbCIsInVzZXJfaWQiOjMwNDEsImZvcmV2ZXIiOmZhbHNlfQ.WbSq_SyBlTrjPakM9tiVQs3K69_V74kHfNNjq3ugTsM"

import json
import requests


def get_postalcode(blocknumber_n_streetname):
    try:
        list_tokens = blocknumber_n_streetname.split(' ')
        check_len = len(list_tokens)
        if check_len > 1:
            cleaned_blocknumber_n_streetname = '%20'.join(list_tokens)
        else:
            cleaned_blocknumber_n_streetname = blocknumber_n_streetname
        
        url = f"https://www.onemap.gov.sg/api/common/elastic/search?searchVal={cleaned_blocknumber_n_streetname}&returnGeom=Y&getAddrDetails=Y"
        header = {'Authorization': f"Bearer ${API_KEY}"}
        response = requests.request("GET",url,headers=header)
        result = json.loads(response.text)
        postalcode = result['results'][0]['POSTAL']
    except:
        postalcode = "000000"
    #print(postalcode)
    return postalcode


def get_age(duration):
    parts = duration.split()
    years = int(parts[0])
    if len(parts)<3:
        months = 0
    else:
        months = int(parts[2])
    return years*12 + months



