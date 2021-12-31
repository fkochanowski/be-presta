FROM prestashop/prestashop
USER root
COPY prestashop/. .
RUN chmod -R 777 /var/www/html/app/logs 
RUN find /var/www/html/ -type d -exec chmod 755 {} \; 
RUN find /var/www/html/ -type f -exec chmod 644 {} \;
