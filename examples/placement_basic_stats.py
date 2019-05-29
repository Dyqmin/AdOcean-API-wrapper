from adocean_api import AdOcean
import json

# Create instance with user data
api = AdOcean("login", "password")

# Open API session
api.open_session()

# Get stats by GetBasicStats from campaign with ID 1 and indicators: impressions, clicks and ctr
stats = api.get(
    'GetBasicStats', {
        'campaignID': '1',
        'statNames': 'allemissions,allclicks,ctr',
        'domainName': 'Placement'}
)

# Convert text to json object
stats = json.loads(stats)

# Our stats are in 'statistics' list of response object 
placement_stats = stats['GetBasicStats']['statistics']

for placement in placement_stats:
    print('[{}] Clicks: {}, Impressions: {}, CTR: {}'.format(
        placement['placementID'],
        placement['allemissions'],
        placement['allclicks'],
        placement['ctr']))

# Close API session
api.close_session()
