from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

def simulate_deploy_gas(bytecode_size_kb):
    gas_per_byte = 200
    total_gas = bytecode_size_kb * 1024 * gas_per_byte
    gas_price_gwei = 20
    cost_eth = w3.from_wei(total_gas * gas_price_gwei * 10**9, 'ether')
    print(f"合约大小: {bytecode_size_kb} KB")
    print(f"预估Gas: {total_gas}")
    print(f"预估成本: {cost_eth:.6f} ETH")

if __name__ == "__main__":
    simulate_deploy_gas(10)
