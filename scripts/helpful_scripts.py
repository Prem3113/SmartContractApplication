from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "local-ganache"]
FORKED_BLOCKCHAIN_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev2"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_BLOCKCHAIN_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def mock_deploy():
    print(f"the active network is {network.show_active()}")
    if (len(MockV3Aggregator)) <= 1:
        MockV3Aggregator.deploy(18, Web3.toWei(2, "ether"), {"from": get_account()})
    print("mocks deployed......")
