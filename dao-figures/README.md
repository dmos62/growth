# dao-figures

This script parses all DAO transactions to produce quantitative reports of the Bisq DAO: per cycle, per month, per day, and all-time.

## Requirements

Python 3 (tested on 3.6.9)

_IMPORTANT: Python 2 will appear to work, but the resulting numbers will be INCORRECT._

## Instructions

Before you run the script, make sure to do the following:

* Set the full path to your `btc_mainnet/db/json/tx` directory in `settings.env`
* Start Bisq with `--dumpBlockchainData=true`

Then run `python3 parse-txs.py`.