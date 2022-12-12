# Install Python
FROM python:3.7

# Set up a working folder and install the pre-reqs
WORKDIR /mnist
ADD mnist /mnist
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Run training and predictions
CMD ["python", "./main.py"]