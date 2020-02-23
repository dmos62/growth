# dao-figures

This script parses all DAO transactions to produce quantitative reports of the Bisq DAO, per-cycle and all-time.

## Requirements

Python 2

## Instructions

Before you run the script, make sure to do the following:

* Set the full path to your `btc_mainnet/db/json/tx` directory in `settings.env`
* Start Bisq with `--dumpBlockchainData=true`

Then run `python parse-txs.py`.