FROM scratch
USER root
COPY prestashop/. .
RUN find /var/www/html/ -type d -exec chmod 777 {} \; 
RUN find /var/www/html/ -type f -exec chmod 777 {} \;

