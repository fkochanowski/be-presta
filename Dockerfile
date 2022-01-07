FROM alpine
COPY prestashop/. .
RUN chmod -R 777 .
