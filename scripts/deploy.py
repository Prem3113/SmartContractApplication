from brownie import FundMe, config, network, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    mock_deploy,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3


def deploy_fundme():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        # if len(MockV3Aggregator) <= 1:
        # MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": account})
        # price_feed = mock_aggregator.address
        mock_deploy()
        price_feed = MockV3Aggregator[-1].address
        # print("mocks deployed.....")
        # print(f"this is length{len(MockV3Aggregator)}")
    fund_me = FundMe.deploy(
        price_feed,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fundme()
