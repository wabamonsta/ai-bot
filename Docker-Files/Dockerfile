FROM  python:3.11.2-slim-buster
ARG PROJECT_NAME
ARG OPENAI_API_KEY
RUN apt-get update -y \
  && apt-get install -y\
  python3 
RUN mkdir -p /var/www/html/${PROJECT_NAME}
WORKDIR /var/www/html/${PROJECT_NAME}
#RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
COPY ./requirements.txt .
COPY ./.env-default .env-default
RUN touch .env && echo "OPENAI_API_KEY='${OPENAI_API_KEY}'\n">>.env
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#ENV PYTHONUNBUFFERED 1
EXPOSE 7860:7860
CMD ["python","./app.py"]