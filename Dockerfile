FROM prestashop/prestashop
USER root
COPY prestashop/. .
RUN find /var/www/html/ -type d -exec chmod 755 {} \; 
RUN find /var/www/html/ -type f -exec chmod 644 {} \;
RUN chmod -R 777 /var/www/html/app/cache /var/www/html/app/logs
