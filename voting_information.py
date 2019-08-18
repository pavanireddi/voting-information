'''
File name   : voting_information.py
Version     : 1.0
Description : Implements APIs to fetch data from SCB database &
              analyze the data to get county with maximum voting
              participation in a given parliamentary election
Copyrights  : LearningWell
'''

import requests, json, codecs, sys

class VotingInformation:
    """
    VotingInformation class shall implement APIs to
        a. Fetch information from SCB database using SCB APIs
        b. Analyze on fetched information to get county with maximum voting
           participation in a given parliamentary election
    """

    def __init__(self, url, json_query):
        self.url = url
        self.json_query = json_query
        # mapping of counties and county codes
        self.counties_codes = {}
        # mapping of voting information according to voting year
        self.voting_information = {}

    def vi_fetch_voting_info_from_scb(self):
        """
        Fetch voting information from SCB database

        1. Gets county names & codes using HTTP 'GET' request
        2. Gets complete voting information available in SCB databse using
           HTTP 'POST' request. json_query is the filter applied on url to
           get required voting information

           json_query must state response format as json
        
        In Params: url, json_query

        Out Params: counties_codes, voting_information
        """

        # map counties and county codes using 'GET' request
        response = requests.get(self.url)
        if response.status_code == requests.codes.ok:
            try:
                data = json.loads(response.text)
                for code, county in zip(data['variables'][0]['values'], \
                    data['variables'][0]['valueTexts']):
                    self.counties_codes[code] = county
                # self.vi_log_msg(self.counties_codes)
            except Exception as e:
                self.vi_log_msg('CRITICAL_ERROR : ', str(e), '. Exiting!!')
                sys.exit()
        else:
            self.vi_log_msg('"GET" request failed. Received error code:', \
                response.status_code)

        # 'POST' required query (json query) to SCB url & get relevant info
        # json_query must state response format as json
        response = requests.post(self.url, json=self.json_query)
        if response.status_code == requests.codes.ok:
            try:
                json_response_obj = json.loads(codecs.encode(response.text, \
                    'utf-8'))

                # json_response_obj['data'] is in below format
                # {"key":[county_code, voting_year],"values":\
                #                               [voting_percentage]}
                # Eg: {"key":["01L","1973"],"values":["90.0"]}
                for voting_data in json_response_obj['data']:
                    county_code = voting_data['key'][0]
                    voting_year = int(voting_data['key'][1])
                    voting_percentage = voting_data['values'][0]
                    # voting_percentage not available
                    if voting_percentage == '..':
                        voting_percentage = 0.0
                    else:
                        voting_percentage = float(voting_percentage)
                    # get county name from county code
                    county_name = self.counties_codes[county_code]
                    
                    # map voting information with voting year & county, i.e,
                    # voting_information[voting_year][county] = \
                    #                               voting_percentage
                    # Eg: voting_information[1973]['Stockholm county council'] \
                    #                               = 90.0
                    if voting_year not in self.voting_information.keys():
                        self.voting_information[voting_year] = {}
                    self.voting_information[voting_year][county_name] = \
                        voting_percentage
            except Exception as e:
                self.vi_log_msg('CRITICAL_ERROR : ', str(e), '. Exiting!!')
                sys.exit()
        else:
            self.vi_log_msg('"POST" request failed. Received error code:', \
                response.status_code)

    def vi_get_county_with_max_voting(self):
        """
        Get information on 'County' with 'maximum voting participation'
        for a given voting year from SCB voting information

        Fetches voting information from SCB using VotingInformation
        API (vi_fetch_voting_info_from_scb)
        
        In Params: voting_information

        Out Params: None
        """

        # fetch voting information from SCB database
        self.vi_fetch_voting_info_from_scb()
        for voting_year, voting_data in self.voting_information.items():
            max_percent = 0.0
            county_with_max_percent = ''
            for county, percentage in voting_data.items():
                if percentage > max_percent:
                    max_percent = percentage
                    county_with_max_percent = county
            self.vi_log_msg(voting_year, county_with_max_percent, max_percent)

    def vi_log_msg(self, *argv):
        """
        Utility to log messages

        In Params: Print information - Variable in length

        Out Params: None
        """

        for msg in argv:
            print(f'{msg}', end=' ')
        # to log the next message on new line, end print with 'new line'
        print('')

'''
How to use:

url = \
    'http://api.scb.se/OV0104/v1/doris/en/ssd/START/ME/ME0104/ME0104D/ME0104T5'
json_query = {
  "query": [],
  "response": {
    "format": "json"
  }
}

voting_info = VotingInformation(url, json_query)
voting_info.vi_get_county_with_max_voting()
'''