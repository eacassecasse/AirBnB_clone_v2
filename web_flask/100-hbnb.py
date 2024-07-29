#!/usr/bin/python3
"""
Flask Web Application for HBnB

This script starts a Flask web application that provides the HBnB home page.

Attributes:
    app (Flask): The Flask application object.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Renders the main HBnB home page.

    Returns:
        str: HTML page containing HBnB home page with filters for States,
             Amenities, and Places.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


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
