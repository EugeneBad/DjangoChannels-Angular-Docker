FROM python:latest
COPY . /var/www
EXPOSE 8000
WORKDIR /var/www
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

