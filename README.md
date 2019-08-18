# voting-information

This is an assignment from LearningWell, Sweden, as part of the recruitment process

## Implements APIs to
    a. Fetch voting information from SCB database using SCB APIs
    b. Analyze on fetched voting information & get county with maximum voting
       participation in a given parliamentary election

# Installation:
    python 3.7.3
    requirements.txt

# Usage:
SCB API URL for getting voting information along with filter info as 'json query' with response format as 'json'

## VotingInformation:
    1. VotingInformation class requires two input arguments - url & json_query
    2. Create an object of VotingInformation
    3. Use vi_get_county_with_max_voting() to get the county with maximum
       voting participation in parliamentay elections

## Testing:
    1. test_voting_information.py explains on how to test this VotingInformation
    2. Few scenarios are listed to test voting_information.py
       (vi_get_county_with_max_voting API

# License:
    LearningWell, Sweden
