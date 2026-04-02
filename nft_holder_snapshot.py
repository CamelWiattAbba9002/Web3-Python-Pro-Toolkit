from web3 import Web3

# NFT合约ABI（Transfer事件）
ABI = '[{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":true,"name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"}]'
w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

def snapshot_nft_holders(contract_addr, start_block, end_block):
    contract = w3.eth.contract(address=contract_addr, abi=ABI)
    holders = {}
    
    events = contract.events.Transfer.get_logs(fromBlock=start_block, toBlock=end_block)
    for event in events:
        to = event.args.to
        holders[to] = holders.get(to, 0) + 1

    print(f"持仓地址数量: {len(holders)}")
    for addr, count in holders.items():
        print(f"{addr} : 持有 {count} 个")
    return holders

if __name__ == "__main__":
    snapshot_nft_holders("0xBC4CA0EdA7647A8aB7C2061c2E118A18a9324d24", 20000000, "latest")
