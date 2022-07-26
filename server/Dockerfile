FROM python:latest

RUN pip install --upgrade pip

ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install flask && \
    pip install pandas && \
    pip install waitress



ADD server.py /server/
ADD main.py /server/
ADD add_data.py /server/
ADD table_data.html /server/

WORKDIR /server

