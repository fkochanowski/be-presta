FROM prestashop/prestashop
COPY prestashop/. .
RUN chmod -R 777 prestashop/
