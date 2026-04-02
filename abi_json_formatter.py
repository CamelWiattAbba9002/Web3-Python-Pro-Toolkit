import json

def format_abi(abi_str):
    try:
        abi = json.loads(abi_str)
        pretty = json.dumps(abi, indent=2)
        print("格式化ABI:")
        print(pretty)
        return pretty
    except:
        print("ABI格式错误")

if __name__ == "__main__":
    format_abi('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}]}]')
