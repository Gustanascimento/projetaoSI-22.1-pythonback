import json
import re
import time

import requests


class DuckDuckSearch(object):
    def __init__(self):
        self.keywords = ''

    def get_token(self):

        url = 'https://duckduckgo.com/'
        params = {'q': self.keywords}

        print('Getting DuckDuckGo Token')

        res = requests.post(url, data=params)
        # searchObj = re.search(r'vqd=([\d-]+)\&', res.text, re.M|re.I)

        if searchObj := re.search(r'vqd=([\d-]+)\&', res.text, re.M | re.I):
            print(f'Token: {searchObj.group(0)}')
            return searchObj.group(1)

        print('Token Parsing Failed !')
        return -1

    def get_results(self, keywords):
        self.keywords = keywords

        token = self.get_token()

        headers = {
            'authority': 'duckduckgo.com',
            'accept': 'application/json, text/javascript, */* q=0.01',
            'sec-fetch-dest': 'empty',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'referer': 'https://duckduckgo.com/',
            'accept-language': 'en-US,enq=0.9',
        }

        params = {
            'l': 'us-en',
            'o': 'json',
            'q': self.keywords,
            'vqd': token,
            'f': ',,,',
            'p': '1',
            'v7exp': 'a',
        }

        print(f'Requesting "{keywords}"')

        while True:

            attempt = 1

            try:
                res = requests.get(
                    'https://duckduckgo.com/i.js',
                    headers=headers,
                    params=params,
                )
                data = json.loads(res.text)
                break
            except ValueError as e:
                if attempt == 4:
                    print('Failed to request results, connection closed.')
                    raise e

                print(
                    f"Attempt {attempt}.\nFailed to request '{keywords}' with error {e}. Trying again in 5 secs..."
                )
                time.sleep(5)
                attempt += 1
                continue

        print('Success!')
        return data['results'][0]['thumbnail']


if __name__ == '__main__':
    searcher = DuckDuckSearch()
    url = searcher.get_results('Abacate')
    print(url)
