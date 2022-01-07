FROM alpine
COPY prestashop/. prestashop/.
RUN chmod -R 777 prestashop/
