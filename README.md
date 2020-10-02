# Python RSI Momentum Trading Strategy Backtest with Zipline and Pyfolio

Use the RSI signal to drive algorithm buying and selling decisions. When the RSI is over 70, a stock is considered overbought and is sold. On the other hand, when the RSI is below 30, a stock is considered oversold and is bought.
Here is additional information from [Investorpedia](https://www.investopedia.com/terms/r/rsi.asp).

## Create and set-up a new virtual environment in Conda

Download and install [Anaconda](https://www.anaconda.com/products/individual)

Create a new environment in your conda navidagor or terminal and use Python version 3.5 given dependencies.

`$ conda create -n env_zipline python=3.5`

Activate the new environment.

`$ conda activate env_zipline`

## Install the packages we need to run the strategy, backtest, and analyze the results

Install the Zipline backtesting library from [Quantopian](https://github.com/quantopian/zipline).

`$ conda install -c Quantopian zipline`

Install interactive Python shell and a Jupyter kernel to work with Python code in Jupyter notebooks and other interactive frontends.

`$ conda install -c anaconda ipykernel`

Install the [Python wrapper](https://github.com/mrjbq7/ta-lib) for [TA-Lib](https://www.ta-lib.org/)

`$ pip install TA-Lib`

Install [Pyfolio](https://github.com/quantopian/pyfolio), see [documentation here](https://www.quantopian.com/docs/api-reference/pyfolio-api-reference) for more information.

`pip install pyfolio`

## Get the stock pricing data necessary for the algo strategy

Obtain a free API key from [Quandl](https://www.quandl.com/)

Set an environmental variable in your terminal with your API key.

`$ export QUANDL_API_KEY='your API key here'`

Ingest the [Quandl Wiki Prices data](https://www.quandl.com/databases/WIKIP/data) into Zipline

`$ zipline ingest -b quandl`


## Running the backtest

Run the below code in your terminal, check the [Zipline Documentation](https://www.zipline.io/index.html) for additional information.

`$ zipline run -f backtest.py --start 2014-1-1 --end 2018-1-1 -o perf.pickle --no-benchmark --capital-base 20000 --bundle quandl`