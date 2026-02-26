FROM php:8.2-apache

# Copy application files into the container
COPY . /var/www/html/

# Fix permissions for the webserver user
RUN chown -R www-data:www-data /var/www/html \
 && find /var/www/html -type f -exec chmod 644 {} \; \
 && find /var/www/html -type d -exec chmod 755 {} \;

EXPOSE 80
