from otg_gql_api import OtgGqlApi, NotOkStatus
from otg_gql_api import NotOkStatus
import sys
from time import sleep

class GeckoScanner:

    _max_rows = 2000000

    _human_chromosome_to_base_pairs = {
        '1': 248956422,
        '2': 242193529,
        '3': 198295559,
        '4': 190214555,
        '5': 181538259,
        '6': 170805979,
        '7': 159345973,
        '8': 145138636,
        '9': 138394717,
        '10': 133797422,
        '11': 135086622,
        '12': 133275309,
        '13': 114364328,
        '14': 107043718,
        '15': 101991189,
        '16': 90338345,
        '17': 83257441,
        '18': 80373285,
        '19': 58617616,
        '20': 64444167,
        '21': 46709983,
        '22': 50818468,
        'x': 156040895,
        'y': 57227415,
    }

    def __init__(self, api_url):
        self.api = OtgGqlApi(api_url)

    def scan_all_gecko(self):
        for chr, bps in self._human_chromosome_to_base_pairs.items():
            start = 0
            while start < bps:
                end = start + self._max_rows
                if end > bps:
                    end = bps
                trial = 1
                while True:
                    try:
                        gecko = self.api.query_gecko(chromosome=chr, start=start, end=end)
                        break
                    except NotOkStatus as e:
                        print('{}: {}'.format(trial, e), file=sys.stderr)
                        if trial > 10:
                            raise e
                        else:
                            sleep(30)
                            trial += 1
                yield gecko
                start = end + 1
