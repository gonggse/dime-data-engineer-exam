import requests
import json

class initfmp :
    """
    FMP Api driver to get data with attached apikeys and main endpoint
    """
    def __init__(self) :
        self.config = self.get_config()
        self.endpoint = self.config['fmp']['endpoint']
        self.api_key = self.config['fmp']['api_key']

    def get_config(self) -> dict :
        with open('./credentials/config.json', 'r') as config_file:
            configs = json.load(config_file) 
        return configs 

    def get_data(self, api_path:str) -> json :
        """
        api_path(str): the target api path for example -> "historical-price-full/stock_dividend/AAPL?"
        """

        url = "{}/{}".format(self.endpoint,api_path)
        res = requests.get(url, params = {"apikey":self.api_key})
        status_code = res.status_code
        if status_code == 200 :
            data = json.loads(res.text)
            return data
        else :
            e = "Getting Data Error With status code: {}".format(status_code)
            raise Exception(e)