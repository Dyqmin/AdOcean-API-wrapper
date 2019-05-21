import requests
import xml.etree.ElementTree as ET
import json

class AdOcean:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.base_url = 'https://api.adocean.pl/json'
        self.session = requests.session()
        self.payload = {
            'login': self.login,
            'passwd': self.password
        }
        self.sessionID = self.open_session(self.payload)

        if self.sessionID is None:
            raise ValueError('Wrong login or password.')

    @staticmethod
    def open_session(data):
        try:
            r = requests.post('https://api.adocean.pl/xml/OpenSession.php', data=data)
            root = ET.fromstring(r.text)
            if root[0].text == 'OK':
                api_key = root[1].text
                return api_key
        except Exception as e:
            return 'Got error: {}'.format(e)

    # Shows advertiser's name based on provided campaign
    def show_advertiser(self, campaign_id):
        r = requests.get(
            'https://api.adocean.pl/xml/GetCampaignInfo.php?sessionID={}&campaignID={}'.format(self.api_key,
                                                                                                campaign_id))
        root = ET.fromstring(r.text)
        return root.find('advertiserName').text

    # Returns a list of all campaigns
    def get_campaigns_list(self, advertiser_name):
        r = requests.get('https://api.adocean.pl/xml/GetCampaignsList.php?sessionID={}'.format(self.api_key))
        root = ET.fromstring(r.text)
        ids_root = root.find('campaigns')
        ids = []
        for campaign in ids_root.findall('campaign'):
            cmp_id = campaign.find('id').text
            adv_name = self.show_advertiser(cmp_id)
            if adv_name == advertiser_name:
                ids.append(adv_name)
        return ids

    def get(self, source):
        url = '{base_url}/{source}.php?sessionID={sessionID}'.format(base_url=self.base_url,source=source,sessionID=self.sessionID)
        response = requests.get(url)
        return response

    def _pre(self, )

c = AdOcean("MEC_ddonoch", "W777c444!@#")

print(c.sessionID)
print(c.get('GetCampaignsList').json())


"""

<?xml version="1.0"?><OpenSession>
<status>OK</status>
<sessionID>y636319a686727c5</sessionID>
</OpenSession>

"""

