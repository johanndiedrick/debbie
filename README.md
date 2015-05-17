# debbie!

a friend to let you know if an artwork is on view at the met


with the help of @jedahan's scrapi.org


### Installation Notes

`virtualenv env`

`source env/bin/activate`

`pip install -r requirements.txt`

Rename `debbie_globals_sample.py` and fill out your mailer credentials, as well as test email to receive notifications:

`mv debbie_globals_sample.py debbie_globals.py`

Then give it a go with:

`python debbie.py`
