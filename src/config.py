import os


workers = int(os.getenv("GUNICORN_PROCESSES", "2"))
threads = int(os.getenv("GUNICORN_THREADS", "4"))
timeout = int(os.getenv("GUNICORN_TIMEOUT", "120"))
bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"
forwarded_allow_ips = "*"
secure_scheme_headers = {"X-Forwarded-Proto": "https"}
