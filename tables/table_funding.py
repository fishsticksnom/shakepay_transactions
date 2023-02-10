from rich.table import Table

table_funding = Table(title="Funding")

table_funding.add_column("Date", justify="right", style="cyan", no_wrap=True)
table_funding.add_column("Amount", justify="right", style="magenta", no_wrap=True)
table_funding.add_column("Amount", justify="right", style="cyan", no_wrap=True)
table_funding.add_column("Direction", justify="right", style="magenta", no_wrap=True)
table_funding.add_column("Destination", justify="right", style="cyan", no_wrap=True)
