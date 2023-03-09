import json, datetime, requests


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise

        today = datetime.date.today()
        with open('ratios.json', 'r') as f:
            ratios = json.load(f)
        for ratio in ratios:
            if ratio["base_currency"] == self.base and ratio["target_currency"
] == self.target and ratio["date_fetched"] == str(today):
                return True
        return False

    def fetch_ratio(self):
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it


        link = f'https://api.exchangerate.host/convert?from={self.base}&to={self.target}'
        response = requests.get(link)
        date = response.json()
        exchange_rate = date['result']
        self.save_ratio(exchange_rate)
        return exchange_rate

    def save_ratio(self, ratio):
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)


        with open('ratios.json', 'r') as f:
            exchange_rates = json.load(f)
        in_file = False
        today = str(datetime.date.today())
        for i, exchange_rate in enumerate(exchange_rates):
            if exchange_rate["base_currency"] == self.base and exchange_rate["target_currency"] == self.target:
                exchange_rate["date_fetched"] = today
                exchange_rate["ratio"] = ratio
                in_file = True
        if not in_file:
            exchange_rates.append(
                {"base_currency": self.base, "target_currency": self.target, "date_fetched": today, "ratio": ratio})
        with open('ratios.json', 'w') as f:
            json.dump(exchange_rates, f)

    def get_matched_ratio_value(self):
        # Should read file and receive exchange rate for given base and target currency from that file


        if self.was_ratio_saved_today():
            with open('ratios.json', 'r') as f:
                exchange_rates = json.load(f)
            for exchange_rate in exchange_rates:
                if exchange_rate["base_currency"] == self.base and exchange_rate["target_currency"] == self.target:
                    return exchange_rate["ratio"]
        else:
            return self.fetch_ratio()
