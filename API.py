import requests
import json

# dictionary of state abbreviations to FIPS code
state_codes = {
    'WA': '53', 'DE': '10', 'DC': '11', 'WI': '55', 'WV': '54', 'HI': '15',
    'FL': '12', 'WY': '56', 'PR': '72', 'NJ': '34', 'NM': '35', 'TX': '48',
    'LA': '22', 'NC': '37', 'ND': '38', 'NE': '31', 'TN': '47', 'NY': '36',
    'PA': '42', 'AK': '02', 'NV': '32', 'NH': '33', 'VA': '51', 'CO': '08',
    'CA': '06', 'AL': '01', 'AR': '05', 'VT': '50', 'IL': '17', 'GA': '13',
    'IN': '18', 'IA': '19', 'MA': '25', 'AZ': '04', 'ID': '16', 'CT': '09',
    'ME': '23', 'MD': '24', 'OK': '40', 'OH': '39', 'UT': '49', 'MO': '29',
    'MN': '27', 'MI': '26', 'RI': '44', 'KS': '20', 'MT': '30', 'MS': '28',
    'SC': '45', 'KY': '21', 'OR': '41', 'SD': '46'
}

# API key 
API_key = "&key=6491ef100a886e21ea48b5a454db83a6b2af5a57"

# universal function to return single stat when given query string and state abbreviation
def getResponse(query_string, state_abrv):
    # get FIPS code from state abbreviation, append to query
    state_id = state_codes[state_abrv]
    query_string += state_id
    # append to key to query
    query_string += API_key
    # get response based on query
    response = requests.get(query_string)
    # convert response to list
    data = response.json()
    # return queried statistic 
    return data[1][0]

# returns total population 
def getPopulation(state_abrv):  
    # query string 
    query = "https://api.census.gov/data/2018/acs/acsse?get=K200104_001E,NAME&for=state:"
    # get response
    return getResponse(query, state_abrv)

# returns median household income over past 12 months
def getMedianHouseholdIncome(state_abrv):
    # query string 
    query = "https://api.census.gov/data/2018/acs/acsse?get=K201902_001E,NAME&for=state:"
    # get response
    return getResponse(query, state_abrv)

# returns median age
def getMedianAge(state_abrv):
    # query string 
    query = "https://api.census.gov/data/2018/acs/acsse?get=K200103_001E,NAME&for=state:"
    # get response
    return getResponse(query, state_abrv)

# returns median gross rent
def getMedianRent(state_abrv):
    # query string 
    query = "https://api.census.gov/data/2018/acs/acsse?get=K202511_001E,NAME&for=state:"
    # get response
    return getResponse(query, state_abrv)

# return percent of population under 18 years old
def getPercentMinor(state_abrv):
    # get total number of minors
    # query string 
    query = "https://api.census.gov/data/2018/acs/acsse?get=K200104_002E,NAME&for=state:"
    # get response
    num_minors = float(getResponse(query, state_abrv))

    # get total population
    total_pop = float(getPopulation(state_abrv))

    # divide by total population and return
    return ((num_minors / total_pop) * 100)
