from web3 import Web3

ERC20_ABI = '[{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

def erc20_airdrop(token_addr, sender_key, recipients, amount):
    sender = w3.eth.account.from_key(sender_key).address
    contract = w3.eth.contract(address=token_addr, abi=ERC20_ABI)
    nonce = w3.eth.get_transaction_count(sender)
    
    for to in recipients:
        tx = contract.functions.transfer(to, w3.to_wei(amount, 'ether')).build_transaction({
            'from': sender, 'nonce': nonce, 'gas': 100000, 'gasPrice': w3.eth.gas_price
        })
        signed = w3.eth.account.sign_transaction(tx, sender_key)
        w3.eth.send_raw_transaction(signed.rawTransaction)
        nonce += 1
    print("空投完成")

if __name__ == "__main__":
    erc20_airdrop("代币合约", "你的私钥", ["地址1", "地址2"], 10)
