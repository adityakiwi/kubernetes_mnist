# Install Python
FROM pytorch/pytorch:latest
RUN pip install flask

LABEL Aditya Dixit "ad5157@nyu.edu"

# Set up a working folder and install the pre-reqs
RUN mkdir /home/user
USER root

COPY test.py .

# Run training and predictions
CMD python3 test.py

