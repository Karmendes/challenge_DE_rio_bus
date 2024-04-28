from etl.main import Extractors
from library.requester.main import Request

URL = 'https://dados.mobilidade.rio/gps/brt'

class ExtractAPI(Extractors):
    def __init__(self):
        self.request = Request({})
    def extract(self):
        response = self.request.get(URL)
        return response.content