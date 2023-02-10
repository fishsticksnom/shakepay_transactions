from rich.table import Table

table_shakes = Table(title="Shakes")

table_shakes.add_column("Date", justify="right", style="cyan", no_wrap=True)
table_shakes.add_column(
    "Amount Credited", justify="right", style="magenta", no_wrap=True
)
table_shakes.add_column(
    "Credited Currency", justify="right", style="cyan", no_wrap=True
)
table_shakes.add_column("Direction", justify="right", style="magenta", no_wrap=True)
table_shakes.add_column("Spot Rate", justify="right", style="cyan", no_wrap=True)
