DATA_FILE = "data.txt"


def generate_recommendations():
    easy = medium = hard = 0
    total_time = 0
    total = 0

    try:
        with open(DATA_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")

                if len(parts) != 6:
                    continue

                _, difficulty, time_taken, status, _, _ = parts

                if status.lower() != "solved":
                    continue

                total += 1
                total_time += int(time_taken)

                if difficulty == "Easy":
                    easy += 1
                elif difficulty == "Medium":
                    medium += 1
                elif difficulty == "Hard":
                    hard += 1

        print("\n🧠 AI Coach Recommendations")
        print("-" * 40)

        if total == 0:
            print("Start solving problems to get insights.")
            return

        # 🎯 Weakness Detection
        difficulty_map = {
            "Easy": easy,
            "Medium": medium,
            "Hard": hard
        }

        weakest = min(difficulty_map, key=difficulty_map.get)
        strongest = max(difficulty_map, key=difficulty_map.get)

        print(f"📌 Strongest Area: {strongest}")
        print(f"⚠️ Weakest Area: {weakest}")

        # 🧠 Strategy Suggestions
        if weakest == "Easy":
            print("👉 Focus on basics. Strengthen fundamentals.")
        elif weakest == "Medium":
            print("👉 Practice Medium problems daily.")
        elif weakest == "Hard":
            print("👉 Start solving Hard problems consistently.")

        # ⏱ Speed Suggestion
        avg_time = total_time / total

        if avg_time > 45:
            print("⏱ You are very slow. Revise concepts.")
        elif avg_time > 30:
            print("⚠️ Work on speed optimization.")
        else:
            print("🔥 Your solving speed is strong.")

        # 📈 Growth Suggestion
        if total < 20:
            print("📈 Increase volume. Solve more problems.")
        elif total < 50:
            print("👍 Good progress. Stay consistent.")
        else:
            print("🚀 You're in top league. Keep pushing!")

    except:
        print("Error generating recommendations.")