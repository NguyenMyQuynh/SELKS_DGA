FROM ubuntu:20.04

RUN apt update

RUN apt install -y python3
RUN apt install -y pip
RUN apt install -y curl

RUN pip install numpy
RUN pip install tensorflow
RUN pip install flask
RUN pip install flask_restful

RUN mkdir PredictDGA
COPY trained_model_7_2_1.h5 PredictDGA/trained_model_7_2_1.h5
COPY API.py PredictDGA/API.py
COPY predictDGA_API.py PredictDGA/predictDGA_API.py

WORKDIR PredictDGA
RUN chmod +x API.py

CMD ["python3", "API.py"]
