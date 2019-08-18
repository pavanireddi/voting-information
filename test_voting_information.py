'''
File name   : test_voting_information.py
Version     : 1.0
Description : Test scenarios for voting_information.py
Copyrights  : LearningWell
'''

import voting_information as vi

scb_api_url = \
  'http://api.scb.se/OV0104/v1/doris/en/ssd/START/ME/ME0104/ME0104D/ME0104T5'

# Test scenario 01:
# SCB voting filter to get complete voting data
json_query_1 = {
  "query": [],
  "response": {
    "format": "json"
  }
}

# Test scenario 02:
# SCB voting filter to get partial voting data with selected counties & years
json_query_2 = {
  "query": [
    {
      "code": "Region",
      "selection": {
        "filter": "item",
        "values": [
          "04L",
          "05L"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": [
          "1998",
          "2002",
          "2006"
        ]
      }
    }
  ],
  "response": {
    "format": "json"
  }
}

# Test scenario 03:
# SCB voting filter to get partial voting data with one county & one year
json_query_3 = {
  "query": [
    {
      "code": "Region",
      "selection": {
        "filter": "item",
        "values": [
          "07L"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": [
          "1998"
        ]
      }
    }
  ],
  "response": {
    "format": "json"
  }
}

print('\n##### Test scenario 1: #####')
voting_info_1 = vi.VotingInformation(scb_api_url, json_query_1)
voting_info_1.vi_get_county_with_max_voting()
print('\n##### Test scenario 2: #####')
voting_info_2 = vi.VotingInformation(scb_api_url, json_query_2)
voting_info_2.vi_get_county_with_max_voting()
print('\n##### Test scenario 3: #####')
voting_info_3 = vi.VotingInformation(scb_api_url, json_query_3)
voting_info_3.vi_get_county_with_max_voting()