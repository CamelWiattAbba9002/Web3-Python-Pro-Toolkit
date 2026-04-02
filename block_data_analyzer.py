from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

def analyze_block(block_num="latest"):
    block = w3.eth.get_block(block_num, full_transactions=False)
    print(f"区块高度: {block.number}")
    print(f"交易数量: {len(block.transactions)}")
    print(f"区块时间: {block.timestamp}")
    print(f"区块大小: {block.size} bytes")

if __name__ == "__main__":
    analyze_block()
