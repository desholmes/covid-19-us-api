import os

PORT = os.environ.get("PORT")

if PORT is None:
    PORT = 8000

bind = f'0.0.0.0:{PORT}'
timeout = 120

if os.environ.get("DEBUG") == 1:
    loglevel = "debug"

    log_path = "/var/gunicorn_log"
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    accesslog = log_path + "/access.txt"
    errorlog = log_path + "/error.txt"
