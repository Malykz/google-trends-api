import requests, json
from user_agent import generate_navigator

class GoogleTrends :
    def __init__(
            self,
            geo,
            url = "https://trends.google.com/_/TrendsUi/data/batchexecute",
            headers = None,
            rdpids = "i0OFE"
        ):

        self.url = url
        self.rdpids = rdpids
        self.headers = headers or generate_navigator()
        self.geo = geo

        self.payload = f"f.req=%5B%5B%5B%22{rdpids}%22%2C%22%5Bnull%2Cnull%2C%5C%22{geo.upper()}%5C%22%2C0%2C%5C%22en-US%5C%22%2C24%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&"
        self.headers.update({'Content-Type' : 'application/x-www-form-urlencoded;charset=utf-8'})

    @property
    def result(self) :
        try :
            response = requests.request("POST", self.url, headers=self.headers, data=self.payload)

            data  = response.text.strip().replace("\\", "")
            start = data.index('"i0OFE","') + 9
            end   = data.index(']]]"') + 3

            form = json.loads(data[start : end])[1]
            data = [{} for i in form]

            i = 0
            for el in form :
                data[i]["title"] = el[0]
                data[i]["region"] = el[2]
                data[i]["category"] = el[10][0]
                data[i]["searchVolume"] = el[6]
                data[i]["breakdown"] = el[9]
                i += 1
                
            return data        
        
        except : return None