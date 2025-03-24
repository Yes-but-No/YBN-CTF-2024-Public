FROM php:7.4-apache

COPY ./src/ /var/www/html/
COPY ./flag.txt /flag.txt
RUN chown www-data:www-data /flag.txt && \
    chmod 400 /flag.txt

EXPOSE 80
