FROM prestashop/prestashop
COPY prestashop/. .

RUN a2enmod ssl
RUN chmod -R 777 .
