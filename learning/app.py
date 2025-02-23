from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_wtf import CSRFProtect

import json

app = Flask(__name__)
app.secret_key = 'aditya'
csrf = CSRFProtect(app) 

@app.route("/")
def task():
    tasks = session.get("tasks", [])
    return render_template("index.html", tasks = tasks, )

@app.route("/add", methods = ["POST"])
def add_task():
    task = request.form.get("task")
    details = request.form.get("value")

    if task:
        tasks = session.get("tasks", [])
        tasks.append({
            "id": task,
            "detail": details
        })
        session["tasks"] = tasks
        flash(f"{task} Task Added successfully!", "success")
    return redirect(url_for("task"))

@app.route("/delete/<int:value>")
def delete_task(value):
    tasks = session.get("tasks", [])
    print(tasks)
    if 0 <= value < len(tasks):
        id = tasks[value].get("id")
        tasks.pop(value)
        session["tasks"] = tasks
        flash(f"{id} Task Deleted successfully!", "success")
    else:
        flash("No Task to delete")
    return redirect(url_for("task"))

@app.route("/clear")
def clear():
    tasks = session.get("tasks", {})
    if tasks:
        session.clear()
        flash("Session Cleared successfully!", "success")
    else:
        flash("No Data to clear Session!", "success")
    return redirect(url_for("task"))

if __name__ == "__main__":
    app.run(port=5001, debug = True)
