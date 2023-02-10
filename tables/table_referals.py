from rich.table import Table

table_referals = Table(title="Referals")

table_referals.add_column("Date", justify="right", style="cyan", no_wrap=True)
table_referals.add_column(
    "Amount Credited", justify="right", style="magenta", no_wrap=True
)
table_referals.add_column(
    "Credited Currency", justify="right", style="cyan", no_wrap=True
)
table_referals.add_column("Direction", justify="right", style="magenta", no_wrap=True)
