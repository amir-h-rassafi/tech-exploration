from web3 import Web3
import yaml

with open('config.yml') as file:
    eth_url = yaml.safe_load(file)['hooks']['eth']


web3 = Web3(Web3.HTTPProvider(eth_url))

print(web3.is_connected())

print(web3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e'))