from web3 import Web3
import csv

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

def export_tx_history(address, save_path="tx_history.csv"):
    tx_list = []
    # 获取交易（简化版）
    block = w3.eth.block_number
    with open(save_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['区块高度', '交易哈希', '时间戳'])
        writer.writerow([block, "0x" + "0"*64, w3.eth.get_block(block)['timestamp']])
    print(f"交易记录已导出到 {save_path}")

if __name__ == "__main__":
    export_tx_history("0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
 
