import requests

# The Request class converts a query into an HTML get request
class Request:

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

    # Converts a query into a HTML request and gets the results
    def convert_query(self, query, state_abrv=""):

        # append state id if looking at state data
        if(state_abrv != ""):
            # get FIPS code from state abbreviation, append to query
            state_id = self.state_codes[state_abrv]
            query += state_id
            
        # append key to query
        query += self.API_key

        # get response based on query
        response = requests.get(query)
        # convert response to list
        data = response.json()

        # return queried statistic 
        request = data[1][0]

        # return request results
        return request