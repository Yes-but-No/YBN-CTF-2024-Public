from secrets import randbelow

from flask import Flask, render_template, request, session

app = Flask(__name__)

with open(".secret_key", "rb") as f:
    app.config["SECRET_KEY"] = f.read().strip()


@app.route("/", methods=["GET", "POST"])
def index():
    if "score" not in session:
        session["score"] = 0
    if "next_guess" not in session:
        session["next_guess"] = str(randbelow(100) + 1)

    if request.method == "GET":
        return render_template("index.html", score=session["score"])
    elif request.method == "POST":
        guess = request.form["guess"]
        if guess == session["next_guess"]:
            session["score"] += 1
            if session["score"] == 10:
                return render_template(
                    "index.html",
                    score=session["score"],
                    flag="YBN24{D0nT_pUT_$3CR3Ts_IN_53S$1ON_coOk1Es_a2650f92c6893e5bb6437}",
                )
            else:
                session["next_guess"] = str(randbelow(100) + 1)
                return render_template("index.html", score=session["score"])
        else:
            session["next_guess"] = str(randbelow(100) + 1)
            session["score"] = 0
            return render_template("index.html", incorrect=True, score=0)
