gunicorn -k flask_sockets.worker -b 0.0.0.0:7579 app:app
