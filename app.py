from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if user == USERNAME and pwd == PASSWORD:
            return redirect("https://www.youtube.com")
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
