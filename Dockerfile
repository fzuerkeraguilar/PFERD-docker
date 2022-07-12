FROM python:latest
RUN apt-get update && apt-get install cron -y
RUN pip install --upgrade git+https://github.com/Garmelon/PFERD@latest
RUN pip install python-crontab
RUN mkdir -p /pferd/working-dir
COPY main.py /pferd/main.py
CMD ["python", "/pferd/main.py"]