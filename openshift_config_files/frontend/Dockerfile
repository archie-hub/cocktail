FROM nginx:1.17
COPY nginx.conf /etc/nginx/nginx.conf
COPY webpage/* /usr/share/nginx/html/
EXPOSE 8080:8080
CMD ["nginx", "-g", "daemon off;"]

