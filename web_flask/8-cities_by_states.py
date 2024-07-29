#!/usr/bin/python3
"""
Flask Web Application for Cities by States

This script starts a Flask web application that provides an HTML
page with a list of all states and their related cities.

Attributes:
    app (Flask): The Flask application object.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Renders an HTML page displaying a list of all states and their related
    cities.

    Returns:
        str: HTML page with a list of states and their cities sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


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
