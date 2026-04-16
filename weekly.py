from datetime import datetime, timedelta
from collections import defaultdict
from rich import print
from rich.panel import Panel

DATA_FILE = "data.txt"


def show_weekly_report():
    today = datetime.today()
    last_7_days = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]

    daily_count = defaultdict(int)
    total = 0

    try:
        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")

                if len(parts) != 6:
                    continue

                _, _, _, status, date, _ = parts

                if status.lower() != "solved":
                    continue

                if date in last_7_days:
                    daily_count[date] += 1
                    total += 1

        print(Panel.fit("📅 [bold cyan]Weekly Report[/bold cyan]"))

        print(f"[bold yellow]Total Solved (Last 7 Days):[/bold yellow] {total}\n")

        print("[bold]Daily Breakdown:[/bold]")
        print("-" * 40)

        for d in reversed(last_7_days):
            count = daily_count[d]
            bar = "█" * count
            print(f"{d} : {bar} ({count})")

        # 🔥 Insight
        print("\n🧠 [bold]Weekly Insight[/bold]")
        print("-" * 40)

        if total == 0:
            print("⚠️ No activity this week. Start solving!")
        elif total < 5:
            print("⚠️ Low consistency. Try solving daily.")
        elif total < 15:
            print("👍 Good effort. Keep pushing!")
        else:
            print("🔥 Excellent consistency! You're on fire!")

    except FileNotFoundError:
        print("[red]No data found.[/red]")