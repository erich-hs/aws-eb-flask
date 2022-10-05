from flask import Flask
from flask import jsonify

# Flask application
application = Flask(__name__)

# Hello World rout
@application.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return "Continuous Delivery Demo!\n"


# Accepting a variable parameter and returning as a json object
@application.route("/echo/<name>")
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
