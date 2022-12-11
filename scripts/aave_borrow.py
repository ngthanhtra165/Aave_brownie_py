
from brownie import accounts , network, config , interface
from scripts.helpful_scripts import get_account
from .get_weth import get_weth
import web3

amount = web3.Web3.toWei(0.01 , "ether")
def main():

    account = get_account()

    erc20_address = config['networks'][network.show_active()]['weth_token']
    
    # if network.show_active() in ["mainnet-fork"]:
    #     get_weth()
    print(account)
    # address
    # ABI
    lending_pool = get_lending_pool()
    print(lending_pool)
    #Approve sending out ERC20 tokens

    approve_erc20(amount, lending_pool.address , erc20_address , account)

    print(f"Deposit {amount} wei ")

    tx = lending_pool.deposit(erc20_address , amount , account.address , 0 , {"from" : account})
    #tx.wait(1)
    print("Deposited !!")

def approve_erc20(amount , spender , erc20_address , account):
    #ABI
    #address
    print("Approving ERC20 token")
    erc20_contract = interface.IERC20(erc20_address)
    tx = erc20_contract.approve(spender , amount , {"from" : account })
    #tx.wait(1)
    print("Approved")



def get_lending_pool():
    #abi

    lending_pool_provider_address = interface.ILendingPoolAddressesProvider(
        config['networks'][network.show_active()]['lending_pool_provider'])
    

    #address
    lending_pool_address = lending_pool_provider_address.getLendingPool()

    print(f'the address for lending_pool is {lending_pool_address}')
    lending_pool = interface.ILendingPool(lending_pool_address)

    return lending_pool