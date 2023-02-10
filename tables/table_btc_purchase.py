from rich.table import Table

table_btc_purchase = Table(title="Bitcoin purchases")

table_btc_purchase.add_column("Date", justify="right", style="cyan", no_wrap=True)
table_btc_purchase.add_column(
    "Amount Debited", justify="right", style="magenta", no_wrap=True
)
table_btc_purchase.add_column(
    "Debit Currency", justify="right", style="cyan", no_wrap=True
)
table_btc_purchase.add_column(
    "Amount Credited", justify="right", style="magenta", no_wrap=True
)
table_btc_purchase.add_column(
    "Credit Currency", justify="right", style="cyan", no_wrap=True
)
table_btc_purchase.add_column(
    "Sell Rate", justify="right", style="magenta", no_wrap=True
)
table_btc_purchase.add_column("Direction", justify="right", style="cyan", no_wrap=True)
