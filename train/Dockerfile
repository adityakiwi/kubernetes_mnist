# Install Python
FROM pytorch/pytorch:latest

LABEL Aditya Dixit "ad5157@nyu.edu"

# Set up a working folder and install the pre-reqs
RUN mkdir /home/user
USER root

COPY train.py .

# Run training and predictions
CMD python3 train.py