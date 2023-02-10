from rich.table import Table

table_transfers = Table(title="Transfers")

table_transfers.add_column("Date", justify="right", style="cyan", no_wrap=True)
table_transfers.add_column(
    "Amount Debited", justify="right", style="magenta", no_wrap=True
)
table_transfers.add_column(
    "Debit Currency", justify="right", style="cyan", no_wrap=True
)
table_transfers.add_column("Direction", justify="right", style="magenta", no_wrap=True)
table_transfers.add_column("Spot Rate", justify="right", style="cyan", no_wrap=True)
table_transfers.add_column(
    "Source / Destination", justify="right", style="magenta", no_wrap=True
)
