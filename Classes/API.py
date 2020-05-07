from Classes.Request import Request

class Adapter:

    __requestType = ""

    def __init__(self, requestType):
        self.__requestType = requestType

    def execute_query(self, geographies=""):
        if(self.__requestType == "totalPop"):
            return self.__getPopulation(geographies)
        if(self.__requestType == "percentPop"):
            return self.__getPercentMinor(geographies)
        if(self.__requestType == "medianAges"):
            return self.__getMedianAge(geographies)
        if(self.__requestType == "medianIncome"):
            return self.__getMedianHouseholdIncome(geographies)
        if(self.__requestType == "medianRent"):
            return self.__getMedianRent(geographies)


    # RESPONSE METHODS FOR SINGLE US STATE
    # returns total population 
    def __getPopulation(self, state_abrv=""):  

        # get total population of state
        if(state_abrv != ""):
            # query string 
            query = "https://api.census.gov/data/2018/acs/acsse?get=K200104_001E,NAME&for=state:"

        # else get total population of US 
        else:
            query = "https://api.census.gov/data/2018/acs/acs1?get=B01003_001E,NAME&for=us:1"
        # get response
        return Request().convert_query(query, state_abrv)

    # returns median household income over past 12 months
    def __getMedianHouseholdIncome(self, state_abrv=""):
        # get median household income for a state
        if(state_abrv != ""):
            # query string 
            query = "https://api.census.gov/data/2018/acs/acsse?get=K201902_001E,NAME&for=state:"

        # else get median household income for the entire US
        else:
            query = "https://api.census.gov/data/2018/acs/acs1?get=B19013_001E,NAME&for=us:1"
        # get response
        return Request().convert_query(query, state_abrv)

    # returns median age
    def __getMedianAge(self, state_abrv=""):

        # get median age of state's residents
        if(state_abrv != ""):
            # query string 
            query = "https://api.census.gov/data/2018/acs/acsse?get=K200103_001E,NAME&for=state:"
        
        # else get median age of all US citizens
        else:
            query = "https://api.census.gov/data/2018/acs/acs1?get=B01002_001E,NAME&for=us:1"
        # get response
        return Request().convert_query(query, state_abrv)

    # returns median gross rent
    def __getMedianRent(self, state_abrv=""):

        # get median gross rent of state
        if(state_abrv != ""):
            # query string 
            query = "https://api.census.gov/data/2018/acs/acsse?get=K202511_001E,NAME&for=state:"

        # else get median gross rent of US
        else:
            query = "https://api.census.gov/data/2018/acs/acs1?get=B25064_001E,NAME&for=us:1"
        # get response
        return Request().convert_query(query, state_abrv)

    # return percent of population under 18 years old
    def __getPercentMinor(self, state_abrv=""):
        # get total number of minors in state
        if(state_abrv != ""):
            # query string 
            query = "https://api.census.gov/data/2018/acs/acsse?get=K200104_002E,NAME&for=state:"

        # else get total number of minors in US
        else:
            query = "https://api.census.gov/data/2018/acs/acs1?get=B09001_001E,NAME&for=us:1"
        # get response
        num_minors = float(Request().convert_query(query, state_abrv))

        # get total population
        total_pop = float(self.__getPopulation(state_abrv))

        # divide by total population and return as percent
        return ((num_minors / total_pop) * 100)