
from pybovespa.bovespa import *
from pybovespa.stock import *

bovespa = Bovespa()
stock = bovespa.query("PETR3")
print(stock.cod, stock.name, stock.last)

sys.path.append(/usr/bin/env)


# doesn't work yet
