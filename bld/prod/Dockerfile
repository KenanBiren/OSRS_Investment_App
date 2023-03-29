FROM python:3.10

WORKDIR /src/app

COPY src/app/requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

COPY src/app .

CMD [ "python3", "src/app/app.py"]