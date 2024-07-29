#!/usr/bin/python3
"""
Flask Web Application for State Information

This script starts a Flask web application that provides HTML
pages with information about State objects.

Attributes:
    app (Flask): The Flask application object.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Renders an HTML page displaying a list of all states.

    Returns:
        str: HTML page with a list of states sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Renders an HTML page displaying information about the state with
    the given <id>.

    Args:
        id (str): The ID of the state to display.

    Returns:
        str: HTML page with information about the state if it exists,
             otherwise a blank page.
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


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
