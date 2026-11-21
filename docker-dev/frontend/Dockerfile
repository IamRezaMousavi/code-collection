FROM node:26-alpine3.23 AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:1.31.9-alpine3.24

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /var/www/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
