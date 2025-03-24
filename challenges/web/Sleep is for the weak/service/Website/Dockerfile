# Use an official PHP runtime as a parent image
FROM php:8.1-apache

# Set working directory
WORKDIR /var/www/html

ENV ADMIN_CREDS="lBcEXKFpQVivikx5vxGmCjpUsk3ROc7SCfd35LB00i4KXOctVAVC28sgagXpRlXf"
ENV SALT="lBcEXKFpQVivikx5vxGmCjpUsk3ROc7SCfd35LB00i4KXOctVAVC28sgagXpRlXf"
ENV ADMIN_URL="https://sleep-is-for-the-weak-dfb3551c-02e3-4ec8-9c77-47ad12acdab3-stealth-chall.ybn.sg/visit"
# Install SQLite3 and PHP SQLite extension
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev \
    && docker-php-ext-install pdo_sqlite

# Create private directory for database file
RUN mkdir -p /var/www/private

# Copy the current directory contents into the container at /var/www/html
COPY . /var/www/html

# Move users.db to the private directory
RUN mv /var/www/html/users.db /var/www/private/users.db

# Set permissions for the database file
RUN chmod -R 770 /var/www/private && chmod 660 /var/www/private/users.db && chown -R www-data:www-data /var/www/private

# Set PHP error reporting to Off
RUN echo "display_errors = Off" >> /usr/local/etc/php/php.ini

# Expose port 483 for the PHP server
EXPOSE 483

# Change Apache to listen on port 483
RUN sed -i 's/80/483/' /etc/apache2/ports.conf /etc/apache2/sites-available/000-default.conf

# Start Apache server
CMD ["apache2-foreground"]
