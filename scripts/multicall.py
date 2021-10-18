#call the last 50 rounds in chainlink
import brownie
from brownie import Contract,interface,multicall


def main():
    price_feed=Contract.from_abi("feed","0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419",interface.AggregatorV3Interface.abi)
    rounds=[]
    latest_rounds=price_feed.latestRoundData()[0]
    brownie.multicall(address="0x5ba1e12693dc8f9c48aad8770482f4739beed696")
    with multicall:
        for round_id in range(latest_rounds,latest_rounds-50,-1):
            round_data=price_feed.getRoundData(round_id)
            rounds.append(round_data)
    print(rounds)