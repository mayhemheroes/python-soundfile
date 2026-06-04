# Build Stage
FROM python:3.11-slim

# Install dependencies
RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive apt-get install -y libsndfile1 && \
        rm -rf /var/lib/apt/lists/*

RUN pip install atheris

ADD . /src
WORKDIR /src
RUN pip install .
RUN pip install numpy

CMD ["/src/mayhem/fuzz_read.py", "/src/mayhem/testsuite"]
