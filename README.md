# SoldPriceMap

INTRODUCTION

This full-stack project entailed building an application that collects and
parses data on the price and xy-coordinates of sold houses. This data can be found at:
"https://raw.github.com/landtechnologies/technical-challenge/master/sold-price-data.txt".

STACK JUSTIFICATION

This project was built on a Python 3.7 backend, and using the Django (version 2.2)
web framework to handle security, URL routing and static file rendering. If this
solution were to be expanded in future, this framework also allows flexibility
by handling database migrations and providing an admin panel.

Vanilla HTML, CSS, JavaScript, and jQuery were used on the front-end for displaying the app.
These were selected for now for more rapid, lightweight development than a
'heavier' solution such as React.JS or Angular.

CONSTRAINTS

This exercise suggested spending no more than two hours on this project. As a
result, there were a few things I would have done differently if given more time.
First being the separation of my settings.py file into development settings
and production settings, which is paramount for internal security, especially
when using version control systems like GitHub. Other constraints included
programming language: Python was used mainly for fast development.
This allowed more time to focus on building a user-friendly front-end,
since this interface is the one that users would be interacting with.

THE FINAL PRODUCT

You can have a little play around with the final app which is deployed on Python anywhere at the URL "http://nicostombros.pythonanywhere.com/"
