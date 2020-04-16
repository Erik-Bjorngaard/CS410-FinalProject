from Request import Request
from Result import Result

class CensicalInterface:
    __dataTopic = ""
    __timeFrame = ""
    __geographies = ""

    def get_dataTopic(self):
        return __dataTopic

    def get_timeFrame(self):
        return __timeFrame
    
    def get_geographies(self):
        return __geographies

    def display_result(self, query):
        request = Request.__convertQuery(query)
        result = Result.

        return result