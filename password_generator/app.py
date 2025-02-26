from flask import Flask, request, render_template, redirect, url_for
from logics import password_generator
app = Flask(__name__)
app.register_blueprint(password_generator.generate_password, prefix_url="/generate_password")

@app.route("/", methods=["GET"])
def index():
    # lower = request.args.get("lowercaseCheck", "off")
    # upper = request.args.get("uppercaseCheck", "off")
    # number = request.args.get("numbersCheck", "off")
    # special = request.args.get("specialCheck", "off")

    password = password_generator.generate_random_password()
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug = True)
