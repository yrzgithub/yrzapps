from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    print(request.)
    return render_template('home.html')

@app.route("/os")
def os():
    request["name"]
    return "<html></html>"

app.run(debug=True)