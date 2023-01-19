from app import app, render_template

# Roteando links/paginas


@app.route("/")
# Funções
def main():
    return render_template("main.html")


@app.route("/user/<userName>")
def user(userName):
    return render_template("user.html", userName=userName)
