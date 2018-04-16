# vi /etc/apache2/ports.conf
# Listen 3000

# vi /etc/hosts
# 127.0.0.1       search.com

# sudo cp search.com.conf /etc/apache2/sites-available

# sudo mkdir -p /var/www/search.com/logs
# sudo chown -R www-data:www-data /var/www/search.com

sudo cp -r . /var/www/search.com

# a2ensite search.com.conf
# service apache2 reload

# optional
# systemctl status apache2.service
# apachectl stop
# service apache2 start

# celery mac
# /usr/local/sbin/rabbitmqctl status
# /usr/local/sbin/rabbitmq-server start
# celery worker -A utils.celery --loglevel=info --logfile=celery.log



