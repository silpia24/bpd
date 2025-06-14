from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello! <br>'

@app.route("/contact")
def contact():
    return '<h1>Contact page</h1>'

# penyingkatan route
@app.route("/profile", defaults={"_route": "home", "user": "admin"})
@app.route("/profile/<user>", defaults={"_route": "profile"})
def profile(user, _route):
    if _route == "home":
        return '<h1>PROFILE HOME</h1>'
    elif _route == "profile":
        return '<h1>HI %s</h1>' % user
    

@app.route("/login")
def login():
    return app.send_static_file('login.html')
    
app.run(debug=True)
