import csv
from rich import print
from rich.console import Console

from tables.table_funding import table_funding
from tables.table_cashout import table_cashout
from tables.table_shakes import table_shakes
from tables.table_btc_purchase import table_btc_purchase
from tables.table_referals import table_referals
from tables.table_transfers import table_transfers


def main():
    with open("transactions_summary.csv", newline="") as csvfile:
        taxesreader = csv.reader(csvfile, delimiter=",", quotechar="|")

        # Fiat
        fiat_funding = fiat_cashout = 0

        # Shakes
        number_of_shakes = 0
        btc_shaked = float(0)

        # Transfers
        crypto_transfers = 0

        # Referals
        referals = dlls_made_in_referals = 0

        # Crypto purchase trough the year
        btc_bought_year = ether_bought_year = float(0)

        for row in taxesreader:
            if "fiat funding" in row[0]:
                dlls = float(row[4])
                fiat_funding = fiat_funding + dlls
                table_funding.add_row(row[1], row[4], row[5], row[7], row[9])
            elif "fiat cashout" in row[0]:
                dlls = float(row[2])
                fiat_cashout = fiat_cashout + dlls
                table_cashout.add_row(row[1], row[2], row[3], row[7], row[9])
            elif "shakingsats" in row[0]:
                number_of_shakes = number_of_shakes + 1
                btc_shaked = btc_shaked + float(row[4])
                table_shakes.add_row(row[1], row[4], row[5], row[7], row[8])
            elif "crypto cashout" in row[0]:
                crypto_transfers = crypto_transfers + 1
                table_transfers.add_row(row[1], row[2], row[3], row[7], row[8], row[9])
            elif "other" in row[0]:
                dlls = float(row[4])
                dlls_made_in_referals = dlls_made_in_referals + dlls
                referals = referals + 1
                table_referals.add_row(row[1], row[4], row[5], row[7])
            elif "purchase/sale" in row[0]:
                if "BTC" in row[5]:
                    btc_bought_year = btc_bought_year + float(row[4])
                    table_btc_purchase.add_row(
                        row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                    )
                elif "ETH" in row[5]:
                    ether_bought_year = ether_bought_year + float(row[4])

        # total_earnings = fiat_cashout - fiat_funding

        console = Console()

        console.print(table_funding)
        print("Fiat Founding: " + str(fiat_funding), "\n")

        console.print(table_cashout)
        print("Fiat Cash Out: " + str(fiat_cashout), "\n")

        console.print(table_btc_purchase)
        print(
            "Amount of Bitcoin bought through the year: " + " " + str(btc_bought_year)
        )
        print(
            "Amount of Ether bough through the year: " + "  " + str(ether_bought_year),
            "\n",
        )

        console.print(table_transfers)
        print("Amount of crypto transfers: " + str(crypto_transfers), "\n")

        console.print(table_shakes)
        print("Amount of shakes: " + str(number_of_shakes))
        print("Amount of BTC made in shakes:   " + str(btc_shaked), "\n")

        console.print(table_referals)
        print("Referals: " + str(referals))
        print(
            "Amount of money made on referals or bonus: "
            + "$"
            + str(dlls_made_in_referals),
            "\n",
        )


if __name__ == "__main__":
    main()
