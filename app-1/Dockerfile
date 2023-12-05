FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8000
# Define environment variable
ENV FLASK_APP=app.py
#Flask app was always defaulting to port 5000 when being run from docker
ENV FLASK_RUN_PORT=8000
CMD ["flask", "run", "--host=0.0.0.0"]