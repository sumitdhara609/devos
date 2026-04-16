import csv
from collections import defaultdict
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

DATA_FILE = "data.txt"


def export_to_csv():
    try:
        with open(DATA_FILE, "r") as f, open("report.csv", "w", newline="") as out:
            writer = csv.writer(out)
            writer.writerow(["Problem", "Difficulty", "Time", "Status", "Date", "Hour"])

            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 6:
                    writer.writerow(parts)

        print("✅ Data exported to report.csv")

    except:
        print("❌ Error exporting data")


def plot_weekly_graph():
    today = datetime.today()
    last_7_days = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]

    daily_count = defaultdict(int)

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

        dates = list(reversed(last_7_days))
        values = [daily_count[d] for d in dates]

        plt.figure()
        plt.plot(dates, values, marker='o')
        plt.title("Weekly Coding Activity")
        plt.xlabel("Date")
        plt.ylabel("Problems Solved")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

    except:
        print("❌ Error generating graph")