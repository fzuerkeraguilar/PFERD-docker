FROM python:latest
RUN "pip install --upgrade git+https://github.com/Garmelon/PFERD@latest"
RUN "pip install python-crontab"
RUN mkdir 