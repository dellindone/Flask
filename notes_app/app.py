from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import CSRFProtect
from models import db, Note

app = Flask(__name__)
app.secret_key = "mysecretkey"  # Required for flash messages
csrf = CSRFProtect(app) 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
# Create tables
with app.app_context():
    db.create_all()

@app.route("/")
def view_notes():
    notes = Note.query.all()
    return render_template("view_notes.html", notes = notes)

@app.route("/add_note", methods=["POST"])
def add_note():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if title and content:
            new_note = Note(title = title, content = content)
            db.session.add(new_note)
            db.session.commit()
    return redirect(url_for("view_notes"))

@app.route("/edit_note/<int:id>", methods=["GET", "POST"])
def edit_notes(id):
    note = Note.query.get_or_404(id)
    if request.method == "POST":
        note.title = request.form["title"]
        note.content = request.form["content"]
        db.session.commit()
        return redirect(url_for("view_notes"))
    return render_template("edit.html", note=note)
    

@app.route("/delete_note/<int:id>")
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for("view_notes"))

if __name__ == "__main__":
    app.run(debug = True)