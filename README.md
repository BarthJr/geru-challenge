# geru-challenge
[![Build Status](https://travis-ci.com/BarthJr/geru-challenge.svg?token=BWopAHdmwdFzLqXw7iyM&branch=master)](https://travis-ci.com/BarthJr/geru-challenge)

The goal is to create a RESTful API with Pyramid and consume it through the developed lib

More details about challenge: [GeruChallenge](https://gist.github.com/debonzi-geru/1042d85e2dcf5facfb1c0ff88e281f8d)


# Installation

1. Clone the repository
2. Change to the directory was created by the clone
3. Create virtualenv with Python 3.7
4. Activate virtualenv
4. Install the dependencies
5. Create database
6. Run the tests
7. Run the server

``` console
git clone git@github.com:BarthJr/geru-challenge.git
cd geru-challenge/quotes_api
python3 -m venv ./.venv
source .venv/bin/activate
pip install -e ".[testing]"
alembic upgrade head
pytest
pserve development.ini --reload
```

# Views
**View**|**URI Path**|**Description**
:--|:--|:--
Home|/|Displays landing page
Quotes|/quotes|Displays all quotes
Quote|/quotes/<0-18>|Displays specific quote
Random Quote|/quotes/random/|Displays random quote

# Endpoints RESTful
**HTTP Method**|**URI Path**|**Description**
:--|:--|:--
GET|/sessions|Returns all sessions
GET|/sessions/{uid}|Returns uid's by sessions
