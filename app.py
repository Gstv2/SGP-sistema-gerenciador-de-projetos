from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/kanban")
def kanban():
    return render_template("kanban.html")

@app.route('/backlog')
def backlog():
    return render_template("backlog.html")

@app.route('/member')
def member():
    return render_template("member.html")

if __name__ == '__main__':
    app.run(debug=True)
