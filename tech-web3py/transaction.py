from web3 import Web3

#Ganache(Truffle Suite)

url = 'http://localhost:7545'

web3 = Web3(Web3.HTTPProvider(url))

print(web3.is_connected())

ac1 = "0xD539938dffc37f093c14EB61782982e02d125a3a"
ac2 = "0x8d2f3aE25Aa56ea218E8196D9616eC2860FAf7dA"

ac1_pk = "0xd5c09c66681ff907ebe8a99e9fb80ef1384bfaa58fe414c466435cbc366b9010"

#get the nonce
nonce = web3.eth.get_transaction_count(ac1)
#build transaction
tx = {
    'nonce':nonce,
    'to': ac2,
    'value': web3.to_wei(1.5 , 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei')
}
print(tx)
#sign transaction
signed_tx = web3.eth.account.sign_transaction(tx, ac1_pk)
print(signed_tx)
#send transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
#get transaction hash
print(tx_hash)