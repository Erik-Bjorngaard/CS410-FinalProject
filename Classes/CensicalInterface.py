from Classes.Request import Request
from Classes.Result import Result
from Classes.API import Adapter

# The CensicalInterface class uses creates new requests and returns the results
class CensicalInterface:
    __data_topic = ""
    __time_frame = ""
    __geographies = ""

    # constructor
    def __init__(self, data_topic, geographies, time_frame = ""):
        self.__data_topic = data_topic
        self.__geographies = geographies
        self.__time_frame = time_frame

    # Getters and Setters
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

    # end of Getters and Setters

    # Create a request using the Adapter class and process the request using the Result class
    def display_result(self):
        # Create new request
        adapter = Adapter(self.get_data_topic())
        stateResult = adapter.execute_query(self.get_geographies())
        usResult = adapter.execute_query()
        censusRequest = {"stateResult": stateResult, "usResult": usResult}
        
        # submit request and process results
        result = Result()
        graph_type = result.get_graph_type(self.get_data_topic())
        results = result.get_result(censusRequest,graph_type,self.get_geographies())

        #display message
        if(self.__data_topic == "totalPop"):
            message = f'The state of {self.get_geographies()}' + \
                                f' has a population of {int(stateResult):,}.' + \
                                    f' Which is about { int(100*round(float(stateResult)/float(usResult), 2))}%' + \
                                        f' of the total population in the US'
        if(self.__data_topic == "percentPop"):
            message = f'Minors make up {round(stateResult, 2)}% of {self.get_geographies()}' + \
                        f's population'
        if(self.__data_topic == "medianAges"):
            message = f'The state of {self.get_geographies()}' + \
                        f' has a median age of: {stateResult}'
        if(self.__data_topic == "medianIncome"):
            message = f'The state of {self.get_geographies()}' + \
                        f' has a median household income of: ${int(stateResult):,}'
        if(self.__data_topic == "medianRent"):
            message = f'The state of {self.get_geographies()}' + \
                        f' has a median rent of: ${int(stateResult):,}'

        # JSON to store result
        output = {"htmlContent": results, "message": message}

        return output