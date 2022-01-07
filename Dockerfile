FROM scratch
COPY prestashop/. .
RUN chmodd -R 777 .
