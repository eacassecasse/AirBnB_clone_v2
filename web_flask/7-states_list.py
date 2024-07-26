#!/usr/bin/python3

from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    States_list Route Function

    Renders an HTML page displaying a list of all State objects in DBStorage.

    Attributes:
        strict_slashes (bool): Whether to enforce trailing slashes on the route URL.

    Returns:
        str: HTML page with a list of states sorted by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


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
