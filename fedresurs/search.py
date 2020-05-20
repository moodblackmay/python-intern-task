import requests
import json
import re

company_info_api = 'https://fedresurs.ru/backend/companies/publications'
company_info_url = 'https://fedresurs.ru/company/{}'

message_info_api = 'https://fedresurs.ru/backend/sfactmessages/{}'
message_info_url = 'https://fedresurs.ru/sfactmessage/{}'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'content-type': 'application/json',
    'referer': '',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'cookie': 'fedresurscookie=302a76b05a600de38a1747cdbc1ff9b7'
}

payload = {
    'bankruptMessageType': None,
    'bankruptMessageTypeGroupId': None,
    'endDate': None,
    'guid': '',
    'legalCaseId': None,
    'messageNumber': None,
    'pageSize': 0,
    'searchAmReport': True,
    'searchFirmBankruptMessage': True,
    'searchFirmBankruptMessageWithoutLegalCase': False,
    'searchSfactsMessage': True,
    'searchSroAmMessage': True,
    'searchTradeOrgMessage': True,
    'sfactMessageType': None,
    'sfactsMessageTypeGroupId': None,
    'startDate': None,
    'startRowIndex': 0,
}


def make_post_req(page_size):
    payload['pageSize'] = int(page_size)

    response = requests.post(company_info_api, data=json.dumps(payload), headers=headers)
    response.close()
    if response.status_code == 500:
        return None, None
    page_data = response.json()['pageData']
    found = response.json()['found']

    return page_data, int(found)


def get_company_guid(page_data):
    pattern = re.compile('банкрот[а-я]+')
    guids = []

    for data in page_data:
        title = data['title'].lower()
        guid = data['guid']
        result = re.findall(pattern, title)
        if result:
            guids.append(guid)
    return guids


def get_message_info(guids):
    info = []

    for guid in guids:
        message_url = message_info_url.format(guid)
        headers['referer'] = message_url

        response = requests.get(url=message_info_api.format(guid), headers=headers)
        response.close()

        date = response.json()['datePublish']
        text = response.json()['content']['text']

        message_info = {
            'url': message_url,
            'guid': guid,
            'datePublish': date,
            'text': text,
        }

        info.append(message_info)

    return info


def get_info(company_guid):
    company_url = company_info_url.format(company_guid)

    headers['referer'] = company_url
    payload['guid'] = company_guid

    # Find max found field
    page_data, found = make_post_req(5)
    if page_data is None:
        return "Company Not Found"
    page_data, _ = make_post_req(found)

    guids = get_company_guid(page_data)
    info = get_message_info(guids)

    return info
