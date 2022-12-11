from brownie import accounts , config , network, Contract , interface

from web3 import Web3

decimal = 18
init_value = 2000000000

fork_local_environment = ["mainnet-fork" , "mainnet-fork-dev"]
local_enviroment = ["development" , "ganache-local"]


def get_account(index = None , id = None):

    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in local_enviroment or network.show_active() in fork_local_environment:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])