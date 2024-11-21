FROM python:3.6.5-alpine3.7

# Set the working directory to /app and copy current dir
WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt


# Run hello_world.py when the container launches
CMD ["pytest","app_register/tests/"]