heroku buildpacks:clear
heroku buildpacks:add --index heroku/python
web gunicorn -w 4 -b 0.0.0.0:$PORT -k gevent main:app

heroku ps:scale web=1
worker: python main.py
