import os
from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")  # Make sure this file exists in templates/

# About page
@app.route("/about")
def about():
    return render_template("about.html")  # Create this file in templates/

# Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")  # Create this file in templates/

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)  # debug=True helps see errors
