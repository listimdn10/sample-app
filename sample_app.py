# Add to this file for the sample app lab
from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
<<<<<<< HEAD
    sample.run(host="0.0.0.0", port=5050)
=======
    sample.run(host="0.0.0.0", port=8080)
>>>>>>> 13021bf31a51f850e72d59c8858e94855aa3b306
