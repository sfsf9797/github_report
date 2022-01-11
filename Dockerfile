# set base image (host OS)
FROM python:3.9

WORKDIR /app
# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local  directory to the working directory
COPY ./ .