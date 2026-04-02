from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

def rich_list(addresses):
    data = []
    for addr in addresses:
        bal = w3.from_wei(w3.eth.get_balance(addr), 'ether')
        data.append({"addr": addr, "eth": float(bal)})
    # 排序
    data = sorted(data, key=lambda x: x['eth'], reverse=True)
    print("=== 资产排行榜 ===")
    for i, item in enumerate(data):
        print(f"{i+1}. {item['addr']} | {item['eth']:.4f} ETH")

if __name__ == "__main__":
    rich_list(["0x000...", "0x000..."])
