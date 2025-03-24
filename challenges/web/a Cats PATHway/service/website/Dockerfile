FROM php:8.2-apache

WORKDIR /var/www/html

RUN apt-get update && apt-get install -y \
    libpng-dev \
    libonig-dev \
    libjpeg-dev \
    zip \
    curl \
    git \
    unzip

RUN docker-php-ext-install gd mbstring

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

RUN a2enmod rewrite

COPY composer.json composer.lock /var/www/html/
RUN composer install

COPY . /var/www/html

RUN mkdir /var/flag && \
    mv /var/www/html/flag.txt /var/flag/ && \
    chmod 700 /var/flag && \
    chown root:root /var/flag/flag.txt

USER root

RUN mv /var/www/html/list_cat /usr/bin/list_cat && \
    chown root /usr/bin/list_cat && \
    chmod 4555 /usr/bin/list_cat

# Set permissions for /var/www/html to read and write only for www-data
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 750 /var/www/html

# Expose port 80
EXPOSE 80

# Start Apache server
CMD ["apache2-foreground"]
