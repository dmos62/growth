import sys
import os
import json
import copy

cycleResults = {}

settingsFile = 'settings.env'
pathError = 'Error finding DAO tx files...did you put the right path in ' + settingsFile + '? You must specify the full path (no tilde).'

resultTemplate = {
    'IRREGULAR': {
        'count': 0,
        'feeSum': 0
    },
    'UNVERIFIED': {
        'count': 0,
        'feeSum': 0
    },
    'INVALID': {
        'count': 0,
        'feeSum': 0
    },
    'GENESIS': {
        'count': 0,
        'feeSum': 0
    },
    'TRANSFER_BSQ': {
        'count': 0,
        'feeSum': 0
    },
    'PAY_TRADE_FEE': {
        'count': 0,
        'feeSum': 0
    },
    'PROPOSAL': {
        'count': 0,
        'feeSum': 0
    },
    'COMPENSATION_REQUEST': {
        'count': 0,
        'feeSum': 0
    },
    'REIMBURSEMENT_REQUEST': {
        'count': 0,
        'feeSum': 0
    },
    'BLIND_VOTE': {
        'count': 0,
        'feeSum': 0
    },
    'VOTE_REVEAL': {
        'count': 0,
        'feeSum': 0
    },
    'LOCKUP': {
        'count': 0,
        'feeSum': 0
    },
    'UNLOCK': {
        'count': 0,
        'feeSum': 0
    },
    'ASSET_LISTING_FEE': {
        'count': 0,
        'feeSum': 0
    },
    'PROOF_OF_BURN': {
        'count': 0,
        'feeSum': 0
    },
    'TOTAL': {
        'count': 0,
        'feeSum': 0
    }
}

### helper functions

def findCycle( height ):

    daoGenesisBlock = 571747 - 1 # first block was 571747, but first cycle was 1 block shorter
    cycleLength = 4680

    cycleEnd = daoGenesisBlock + cycleLength
    cycle = 1

    while( cycleEnd < height ):
        cycle += 1
        cycleEnd = daoGenesisBlock + ( cycleLength * cycle )

    return cycle

### set environment

try:
    with open( settingsFile, 'r' ) as settings:
        daoTxPath = settings.read().split( '=' )[1].splitlines()[0]
except:
    print( pathError )
    sys.exit()

### iterate through dao transactions directory

cycleResults = { 'ALL-TIME': copy.deepcopy( resultTemplate ) }    

try:
    for filename in os.listdir( daoTxPath ):
        
        with open( daoTxPath + filename, 'r' ) as daoTx:
            daoTxDict = json.loads( daoTx.read() )

        txCycle = findCycle( daoTxDict[ 'blockHeight' ] )

        if( txCycle not in cycleResults ):
            cycleResults[ txCycle ] = copy.deepcopy( resultTemplate )
        
        burntFee = daoTxDict[ 'burntFee' ] / 100

        cycleResults[ txCycle ][ daoTxDict[ 'txType' ] ][ 'count' ] += 1
        cycleResults[ txCycle ][ daoTxDict[ 'txType' ] ][ 'feeSum' ] += burntFee

        cycleResults[ txCycle ][ 'TOTAL' ][ 'count' ] += 1
        cycleResults[ txCycle ][ 'TOTAL' ][ 'feeSum' ] += burntFee

        cycleResults[ 'ALL-TIME' ][ daoTxDict[ 'txType' ] ][ 'count' ] += 1
        cycleResults[ 'ALL-TIME' ][ daoTxDict[ 'txType' ] ][ 'feeSum' ] += burntFee

        cycleResults[ 'ALL-TIME' ][ 'TOTAL' ][ 'count' ] += 1
        cycleResults[ 'ALL-TIME' ][ 'TOTAL' ][ 'feeSum' ] += burntFee

except IOError:
    print( pathError )
    sys.exit()

### print results

print( json.dumps( cycleResults, indent=4 ) )
