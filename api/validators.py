import json

CURRENCIES = [
    'Bitcoin', 'Ethereum', 'Tether', 'XRP', 'Bitcoin Cash', 'Chainlink', 'Polkadot', 'Litecoin',
    'Crypto.com Coin', 'Bitcoin SV', 'EOS', 'Binance Coin', 'Cardano', 'TRON', 'Tezos', 'USD Coin', 'Stellar',
    'Monero', 'Neo', 'UNUS SED LEO', 'NEM', 'Cosmos', 'Huobi Token', 'IOTA', 'Aave', 'VeChain',
    'yearn.finance', 'Dash', 'UMA', 'Ethereum Classic', 'Zcash', 'OMG Network', 'Maker', 'Dai', 'Ontology',
    'Compound', 'Synthetix Network Token', 'Celo', 'HedgeTrade', 'TrueUSD', 'Algorand', 'Dogecoin',
    'Basic Attention Token', 'THETA', 'BitTorrent', 'FTX Token', '0x', 'DigiByte', 'OKB', 'Kusama',
    'Elrond ERD', 'Energy Web Token', 'Ren', 'Paxos Standard', 'Hyperion', 'Waves', 'ICON', 'Kyber Network',
    'Flexacoin', 'Qtum', 'Loopring', 'Binance USD', 'Hedera Hashgraph', 'Band Protocol', 'Augur', 'Lisk',
    'Elrond', 'Decred', 'Zilliqa', 'Arweave', 'Ampleforth', 'Bitcoin Gold', 'BitShares', 'HUSD', 'Aragon',
    'DFI.Money', 'Siacoin', 'ZB Token', 'Balancer', 'Terra', 'Enjin Coin', 'CyberVein', 'Swipe', 'Numeraire',
    'Ravencoin', 'Ocean Protocol', 'Decentraland', 'Reserve Rights', 'Bitcoin Diamond', 'Nano', 'SushiSwap',
    'Serum', 'Golem', 'Nervos Network', 'Status', 'Storj', 'MonaCoin', 'DxChain Token', 'THORChain', 'Bytom'
]


def currency_serializer(q) -> json:
    value = q.values.last()

    return {
        "id"              : q.id,
        "created_at"      : q.create_at,
        "currency"        : q.currency,
        "frequency"       : q.frequency,
        "value"           : value.value,
        "value_updated_at": value.create_at,
    }


def get_valid_data(method, body) -> (json, bool):

    try:
        data = json.loads(body.decode())
        if method == 'POST':

            currency: str = data['currency']

            if currency not in CURRENCIES:
                return {"error": "Invalid currency, see https://coinmarketcap.com"}, False

            frequency: int = data['frequency']
            if frequency < 1:
                return {"error": "Invalid frequency"}, False

        if method == 'PUT':
            id: int = data['id']
            frequency: int = data['frequency']
            if id < 1 or frequency < 1:
                return {"error": "Min value is 0"}, False

        if method == 'DELETE':
            id: int = data['id']
            if id < 1:
                return {"error": "Invalid id"}, False

    except:
        return {"error": "Invalid data"}, False

    return data, True
