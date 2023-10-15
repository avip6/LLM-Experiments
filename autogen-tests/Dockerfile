FROM python:3.11
WORKDIR /app
COPY . /app
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/
CMD [ "python3", "-u", "app.py" ]