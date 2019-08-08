# build stage
FROM node:8-slim AS build-stage
LABEL stage=site-builder

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:mainline-alpine as production-stage
#COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]