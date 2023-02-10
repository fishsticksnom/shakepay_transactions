from rich.table import Table

table_cashout = Table(title="Cashout")

table_cashout.add_column("Date", justify="right", style="cyan", no_wrap=True)
table_cashout.add_column("Amount", justify="right", style="magenta", no_wrap=True)
table_cashout.add_column("Debit Currency", justify="right", style="cyan", no_wrap=True)
table_cashout.add_column("Direction", justify="right", style="magenta", no_wrap=True)
table_cashout.add_column("Destination", justify="right", style="cyan", no_wrap=True)
