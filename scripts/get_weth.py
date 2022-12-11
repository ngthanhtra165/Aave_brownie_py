
from brownie import accounts , config , network , interface
from scripts.helpful_scripts import get_account

def get_weth():
    # mint weth token by depositing ETH

    # ABI
    # address
    accounts = get_account()

    #print(type(accounts))
    #print(type(accounts.address))
    print(f"the account : {accounts}")
    print(config['networks'][network.show_active()]['weth_token'])
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )

    tx = weth.deposit({'from': accounts , 'value': 1 * 10**18 })

    print("Deposited 1 ether !!")

    
def main():
    get_weth()