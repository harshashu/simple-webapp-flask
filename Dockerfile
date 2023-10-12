FROM python
COPY . /opt/app-code
RUN pip install flask
RUN pip install flask-mysql
ENTRYPOINT FLASK_APP=/opt/app-code/app.py flask run --host=0.0.0.0
