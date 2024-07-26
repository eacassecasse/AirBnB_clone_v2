# Web Flask

This folder contains a collection of Flask web applications developed for various purposes.

## Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)

## Description

Each Flask web application in this folder serves a specific purpose, ranging from displaying lists of objects to 
providing interactive user interfaces. Below is a brief overview of each application:

1. **0-hello_route**: Flask web application that displays "Hello HBNB!" when accessing the root URL ("/").

2. **1-hbnb_route**: Flask web application that displays "HBNB" when accessing the root URL ("/hbnb").

3. **2-c_route**: Flask web application with a route ("/c/<text>") that converts the given text to a URL-friendly format.

4. **3-python_route**: Flask web application with a route ("/python/<text>") that displays a message with the specified text.

5. **4-number_route**: Flask web application with a route ("/number/<int:n>") that displays 'n is a number' only if n is an integer.

6. **5-number_template**: Flask web application with a route ("/number_template/<int:n>") that displays an HTML page containing the provided number.

7. **6-number_odd_or_even**: Flask web application with a route ("/number_odd_or_even/<int:n>") that displays whether a number is odd or even.

8. **7-states_list**: Flask web application with a route ("/states_list") that displays a list of all State objects.

9. **8-cities_by_states**: Flask web application with a route ("/cities_by_states") that displays a list of all states and related cities.

10. **9-states**: Flask web application with routes ("/states" and "/states/<id>") that display information about states.

11. **10-hbnb_filters**: Flask web application with a route ("/hbnb_filters") that displays the main HBnB filters HTML page.

12. **100-hbnb**: Flask web application with a route ("/hbnb") that renders the main HBnB home page with filters.

## Installation

To run these Flask applications, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/eacassecasse/AirBnB_clone_v2.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd AirBnB_clone_v2
    ```

## Usage

Each Flask application can be run individually by executing its corresponding Python script. 
For example, to run the "0-hello_route" application:

```bash
python3 -m web_flask.0-hello_route
