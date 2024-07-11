# Poll World
It's the [Django Polls tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/) with some nice frontend from Bootstrap and some HTMX for interactivity.

## How it works
You can create Questions which have Choices. These are then published to the index of the website. Each Choice starts with 0 votes, and users can vote on the Choices to increase the vote count.

## Installation / running
This was developed with Python 3.11 and Django 4.2 but will very likely work with higher versions. 

After optionally creating a virtual environment, run `pip install -r requirements.txt` in the base directory. After that, run `python3/py manage.py runserver` and check `127.0.0.1:8000`.

## Details
The database is committed with this repo so somebody cloning it doesn't have to burden themselves with making some dummy questions/choices to try out the application.

The `admin` account has the password `asdfasdf`.