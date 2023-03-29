FROM python:3.10

COPY src/app/requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

COPY src/app .

WORKDIR /src/app

CMD [ "python3", "run_test_groups.py"]