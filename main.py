from ai import generate_recommendations
from export import export_to_csv, plot_weekly_graph
from weekly import show_weekly_report
from rich import print
from rich.panel import Panel
from rich.table import Table

from storage import add_entry, get_entries
from analysis import show_stats


def show_menu():
    print(Panel.fit("⚡ [bold cyan]DevOS Dashboard[/bold cyan] ⚡"))
    print("[1] 📝 Log Coding Session")
    print("[2] 📂 View Logs")
    print("[3] 📊 Show Insights")
    print("[4] 📅 Weekly Report")
    print("[5] 📤 Export to CSV")
    print("[6] 📈 Show Graph")
    print("[7] 🧠 AI Coach")
    print("[8] ❌ Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_entry()

        elif choice == "2":
            entries = get_entries()

            if not entries:
                print("[red]No logs found.[/red]")
            else:
                table = Table(title="📂 Your Logs")

                table.add_column("No.", style="cyan")
                table.add_column("Details", style="magenta")

                for i, e in enumerate(entries, 1):
                    table.add_row(str(i), e)

                print(table)

        elif choice == "3":
            show_stats()

        elif choice == "4":
            show_weekly_report()

        elif choice == "5":
            export_to_csv()

        elif choice == "6":
            plot_weekly_graph()

        elif choice == "7":
            generate_recommendations()

        elif choice == "8":
            print("🚀 Keep improving daily!")
            break

        else:
            print("[red]Invalid choice![/red]")


if __name__ == "__main__":
    main()