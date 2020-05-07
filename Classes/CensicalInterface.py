from Classes.Request import Request
from Classes.Result import Result
from Classes.API import Adapter

class CensicalInterface:
    __data_topic = ""
    __time_frame = ""
    __geographies = ""

    def __init__(self, data_topic, geographies, time_frame = ""):
        self.__data_topic = data_topic
        self.__geographies = geographies
        self.__time_frame = time_frame

    def get_data_topic(self):
        return self.__data_topic

    def set_data_topic(self, data_topic):
        self.__data_topic = data_topic

    def get_time_frame(self):
        return self.__time_frame

    def set_time_frame(self, time_frame):
        self.__time_frame = time_frame
    
    def get_geographies(self):
        return self.__geographies

    def set_geographies(self, geographies):
        self.__geographies = geographies

    def display_result(self):
        # Create new request
        adapter = Adapter(self.get_data_topic())
        stateResult = adapter.execute_query(self.get_geographies())
        usResult = adapter.execute_query()
        censusRequest = {"stateResult": stateResult, "usResult": usResult}
        
        result = Result()

        graph_type = result.get_graph_type(self.get_data_topic())
        results = result.get_result(censusRequest,graph_type,self.get_geographies())

        #display message
        if(self.__data_topic == "totalPop"):
            message = f'The state of: {self.get_geographies()}' + \
                                f' has a total population of: {stateResult}'
        if(self.__data_topic == "percentPop"):
            message = f'Minors make up {stateResult}% of state: {self.get_geographies()}' + \
                        f's population'
        if(self.__data_topic == "medianAges"):
            message = f'The state of: {self.get_geographies()}' + \
                        f' has a median age of: {stateResult}'
        if(self.__data_topic == "medianIncome"):
            message = f'The state of: {self.get_geographies()}' + \
                        f' has a median household income of: ${stateResult}'
        if(self.__data_topic == "medianRent"):
            message = f'The state of: {self.get_geographies()}' + \
                        f' has a median rent of: ${stateResult}'

        output = {"stateResult": stateResult, "render": results, "message": message}

        return output