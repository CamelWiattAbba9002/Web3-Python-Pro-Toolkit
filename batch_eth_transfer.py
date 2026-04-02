from web3 import Web3

# 配置RPC和钱包
w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
YOUR_PRIVATE_KEY = "你的私钥"
SENDER_ADDR = "你的钱包地址"

def batch_send_eth(to_addresses, amount_eth):
    amount_wei = w3.to_wei(amount_eth, 'ether')
    nonce = w3.eth.get_transaction_count(SENDER_ADDR)
    
    for i, addr in enumerate(to_addresses):
        if not w3.is_address(addr):
            continue
        # 构建交易
        tx = {
            'from': SENDER_ADDR,
            'to': addr,
            'value': amount_wei,
            'gas': 21000,
            'gasPrice': w3.eth.gas_price,
            'nonce': nonce + i,
            'chainId': 1
        }
        # 签名发送
        signed = w3.eth.account.sign_transaction(tx, YOUR_PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
        print(f"转账成功 {i+1} | 哈希: {tx_hash.hex()}")

if __name__ == "__main__":
    receivers = ["0x...地址1", "0x...地址2"]
    batch_send_eth(receivers, 0.001)
