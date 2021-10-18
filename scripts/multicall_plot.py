#call the last 50 rounds in chainlink
#plot it 

import brownie
from brownie import Contract,interface,multicall,config,network
from datetime import datetime
import matplotlib.pyplot as plt

def main():
    price_feed = Contract.from_abi(
        "feed",
        config["networks"]["mainnet"]["sol_usd"],
        interface.AggregatorV3Interface.abi,
    )
    latest_round = price_feed.latestRoundData()[0]
    decimals = price_feed.decimals()

    round_ids = []
    answers = []
    time_stamps = []
    brownie.multicall(address=config["networks"]["mainnet"]["multicall2"])
    with brownie.multicall:
        for round_id in range(latest_round, latest_round - 50, -1):
            round_data = price_feed.getRoundData(round_id)
            round_ids.append(round_data[0])
            answers.append(round_data[1] / 10 ** decimals)
            time_stamps.append(datetime.fromtimestamp(round_data[3]))

    plt.plot(time_stamps, answers)
    plt.show()