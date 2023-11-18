FROM node:18-alpine

COPY . /opt/code
WORKDIR /opt/code

RUN npm install

CMD [ "/bin/sh", "-c", "npm start" ]