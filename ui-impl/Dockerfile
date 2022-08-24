FROM python:3.7.3-slim
# We copy just the requirements.txt first to leverage Docker cache
WORKDIR /apps
COPY . /apps
RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python3" "./app.py" ]