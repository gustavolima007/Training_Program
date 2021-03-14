from yahooquery import Ticker

abev = Ticker('ABEV3.SA')
abev.history(period='60d',  interval = "30m")

print(abev())