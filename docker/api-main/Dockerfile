FROM python:3.8.3
# WORKDIR /api-main
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN export SECRET_KEY=$(openssl rand -hex 32)
RUN git clone https://github.com/vishnubob/wait-for-it && chmod +x ./wait-for-it/wait-for-it.sh
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt