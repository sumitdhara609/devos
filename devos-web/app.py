from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Database Model
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    problem = db.Column(db.String(200), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    time_taken = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Session {self.problem}>"


# Home Route
@app.route("/")
def home():
    sessions = Session.query.order_by(Session.created_at.desc()).all()

    total_sessions = len(sessions)
    total_time = sum(session.time_taken for session in sessions)

    avg_time = round(total_time / total_sessions, 1) if total_sessions > 0 else 0

    easy = sum(1 for session in sessions if session.difficulty == "Easy")
    medium = sum(1 for session in sessions if session.difficulty == "Medium")
    hard = sum(1 for session in sessions if session.difficulty == "Hard")

    # A = Achievement Score
    a_score = min(total_sessions * 5, 100)

    return render_template(
        "index.html",
        sessions=sessions,
        total_sessions=total_sessions,
        total_time=total_time,
        avg_time=avg_time,
        easy=easy,
        medium=medium,
        hard=hard,
        a_score=a_score
    )


# Add Session Route
@app.route("/add", methods=["POST"])
def add():
    problem = request.form.get("problem", "").strip()
    difficulty = request.form.get("difficulty", "").strip()
    time_taken = request.form.get("time_taken", "").strip()

    if not problem or not difficulty or not time_taken.isdigit():
        return redirect(url_for("home"))

    new_session = Session(
        problem=problem,
        difficulty=difficulty,
        time_taken=int(time_taken)
    )

    db.session.add(new_session)
    db.session.commit()

    return redirect(url_for("home"))

@app.route("/chart")
def chart():
    sessions = Session.query.all()

    easy = sum(1 for s in sessions if s.difficulty == "Easy")
    medium = sum(1 for s in sessions if s.difficulty == "Medium")
    hard = sum(1 for s in sessions if s.difficulty == "Hard")

    labels = ["Easy", "Medium", "Hard"]
    values = [easy, medium, hard]

    plt.figure(figsize=(7,5))
    plt.bar(labels, values)
    plt.title("DevOS A-Analytics Difficulty Breakdown")
    plt.xlabel("Difficulty")
    plt.ylabel("Solved Count")

    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format="png")
    img.seek(0)
    plt.close()

    return send_file(img, mimetype="image/png")
# Run App
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)