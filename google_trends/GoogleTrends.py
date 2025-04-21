import requests, json
from user_agent import generate_navigator

class GoogleTrends :
    # This is a constant value that when encoded will have value = f.req=[[["{rdpids}","[null,null,\"{geo}\",0,\"en-US\",24,1]",null,"generic"]]]
    PAYLOAD_FORMAT = "f.req=%5B%5B%5B%22{rdpids}%22%2C%22%5Bnull%2Cnull%2C%5C%22{geo}%5C%22%2C0%2C%5C%22id%5C%22%2C24%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D"

    # The URL that will be used to send requests with POST method.
    BASE_URL = "https://trends.google.com/_/TrendsUi/data/batchexecute"

    # ID for RDP
    RDPIDS = "i0OFE"

    def __init__(
            self,
            geo:str ,
            url = None,
            headers = None,
            rdpids = None
        ):

        self.geo = geo
        self.url = url or self.BASE_URL
        self.rdpids = rdpids or self.RDPIDS
        self.headers = headers or generate_navigator() # Navigator template for sending requests, Fake user-agent included.

        self.payload = self.PAYLOAD_FORMAT.format(rdpids=self.rdpids, geo=self.geo.upper())
        self.headers.update({'Content-Type' : 'application/x-www-form-urlencoded;charset=utf-8'}) # Additional headers that will affect the response format.
        self.response = requests.request("POST", self.url, headers=self.headers, data=self.payload) # Send the Request.

    @property
    def result(self) :
        # The response received is in the form of a messy Array, so this method functions to parse it and convert it into JSON format.
        # If you want to see the raw result. It is better to use the self.response.text
        
        try :
            data  = self.response.text.strip().replace("\\", "")
            start = data.index(f'"{self.RDPIDS}","') + 4 + len(self.RDPIDS)
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
        
