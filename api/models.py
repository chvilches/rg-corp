from django.db import models

CURRENCY_CHOICES = [('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('Tether', 'Tether'), ('XRP', 'XRP'),
                    ('Bitcoin Cash', 'Bitcoin Cash'), ('Chainlink', 'Chainlink'), ('Polkadot', 'Polkadot'),
                    ('Litecoin', 'Litecoin'), ('Crypto.com Coin', 'Crypto.com Coin'), ('Bitcoin SV', 'Bitcoin SV'),
                    ('EOS', 'EOS'), ('Binance Coin', 'Binance Coin'), ('Cardano', 'Cardano'), ('TRON', 'TRON'),
                    ('Tezos', 'Tezos'), ('USD Coin', 'USD Coin'), ('Stellar', 'Stellar'), ('Monero', 'Monero'),
                    ('Neo', 'Neo'), ('UNUS SED LEO', 'UNUS SED LEO'), ('NEM', 'NEM'), ('Cosmos', 'Cosmos'),
                    ('Huobi Token', 'Huobi Token'), ('IOTA', 'IOTA'), ('Aave', 'Aave'), ('VeChain', 'VeChain'),
                    ('yearn.finance', 'yearn.finance'), ('Dash', 'Dash'), ('UMA', 'UMA'),
                    ('Ethereum Classic', 'Ethereum Classic'), ('Zcash', 'Zcash'), ('OMG Network', 'OMG Network'),
                    ('Maker', 'Maker'), ('Dai', 'Dai'), ('Ontology', 'Ontology'), ('Compound', 'Compound'),
                    ('Synthetix Network Token', 'Synthetix Network Token'), ('Celo', 'Celo'),
                    ('HedgeTrade', 'HedgeTrade'), ('TrueUSD', 'TrueUSD'), ('Algorand', 'Algorand'),
                    ('Dogecoin', 'Dogecoin'), ('Basic Attention Token', 'Basic Attention Token'), ('THETA', 'THETA'),
                    ('BitTorrent', 'BitTorrent'), ('FTX Token', 'FTX Token'), ('0x', '0x'), ('DigiByte', 'DigiByte'),
                    ('OKB', 'OKB'), ('Kusama', 'Kusama'), ('Elrond ERD', 'Elrond ERD'),
                    ('Energy Web Token', 'Energy Web Token'), ('Ren', 'Ren'), ('Paxos Standard', 'Paxos Standard'),
                    ('Hyperion', 'Hyperion'), ('Waves', 'Waves'), ('ICON', 'ICON'), ('Kyber Network', 'Kyber Network'),
                    ('Flexacoin', 'Flexacoin'), ('Qtum', 'Qtum'), ('Loopring', 'Loopring'),
                    ('Binance USD', 'Binance USD'), ('Hedera Hashgraph', 'Hedera Hashgraph'),
                    ('Band Protocol', 'Band Protocol'), ('Augur', 'Augur'), ('Lisk', 'Lisk'), ('Elrond', 'Elrond'),
                    ('Decred', 'Decred'), ('Zilliqa', 'Zilliqa'), ('Arweave', 'Arweave'), ('Ampleforth', 'Ampleforth'),
                    ('Bitcoin Gold', 'Bitcoin Gold'), ('BitShares', 'BitShares'), ('HUSD', 'HUSD'),
                    ('Aragon', 'Aragon'), ('DFI.Money', 'DFI.Money'), ('Siacoin', 'Siacoin'), ('ZB Token', 'ZB Token'),
                    ('Balancer', 'Balancer'), ('Terra', 'Terra'), ('Enjin Coin', 'Enjin Coin'),
                    ('CyberVein', 'CyberVein'), ('Swipe', 'Swipe'), ('Numeraire', 'Numeraire'),
                    ('Ravencoin', 'Ravencoin'), ('Ocean Protocol', 'Ocean Protocol'), ('Decentraland', 'Decentraland'),
                    ('Reserve Rights', 'Reserve Rights'), ('Bitcoin Diamond', 'Bitcoin Diamond'), ('Nano', 'Nano'),
                    ('SushiSwap', 'SushiSwap'), ('Serum', 'Serum'), ('Golem', 'Golem'),
                    ('Nervos Network', 'Nervos Network'), ('Status', 'Status'), ('Storj', 'Storj'),
                    ('MonaCoin', 'MonaCoin'), ('DxChain Token', 'DxChain Token'), ('THORChain', 'THORChain'),
                    ('Bytom', 'Bytom')
                    ]


class Scraper(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=50, choices=CURRENCY_CHOICES)
    frequency = models.IntegerField(default=0)


class ScraperValues(models.Model):
    scraper = models.ForeignKey(Scraper, on_delete=models.CASCADE, related_name='values')
    value = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
