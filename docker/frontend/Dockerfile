FROM node:14.5.0
WORKDIR /frontend
ENV PATH /frontend/node_modules/.bin:$PATH
COPY package.json /frontend/package.json
RUN npm install
RUN npm install @vue/cli@3.7.0 -g
