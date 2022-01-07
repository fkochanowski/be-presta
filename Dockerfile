FROM scratch
COPY prestashop/. .
RUN chmod -R 777 .
