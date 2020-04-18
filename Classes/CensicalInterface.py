from request import Request
from result import Result

class CensicalInterface:
    __data_topic = ""
    __time_frame = ""
    __geographies = ""

    def get_data_topic(self):
        return __data_topic

    def set_data_topic(self, data_topic):
        __data_topic = data_topic

    def get_time_frame(self):
        return __time_frame

    def set_time_frame(self, time_frame):
        __time_frame = time_frame
    
    def get_geographies(self):
        return __geographies

    def set_geographies(self, geographies):
        __geographies = geographies

    def display_result(self, query):
        # Create new request
        request = Request.__convertQuery(query)
        
        # Determine which graph to display based on data topic
        graphType = Result.get_graph_type(__data_topic)

        # Parse request
        result = Result.get_result(request)

        return result