#!/usr/bin/python3
"""
Flask Web Application for HBnB Filters

This script starts a Flask web application that provides an HTML
page for HBnB filters.

Attributes:
    app (Flask): The Flask application object.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    Renders the main HBnB filters HTML page.

    Returns:
        str: HTML page containing filters for States and Amenities.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """
    Closes the current SQLAlchemy session after each request.

    Args:
        exc: The exception raised during request processing, if any.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
