# sudo apt-get update
# sudo apt-get install apache2

# sudo apt-get install libapache2-mod-wsgi
# sudo a2enmod wsgi

# vi /etc/apache2/ports.conf
# Listen 3000

# vi /etc/hosts
# 127.0.0.1       beauty.com

# sudo cp beauty.com.conf /etc/apache2/sites-available

# sudo mkdir -p /var/www/beauty.com/logs
# sudo chown -R www-data:www-data /var/www/beauty.com

sudo cp -r . /var/www/beauty.com

# a2ensite beauty.com.conf
# service apache2 reload

# optional
# systemctl status apache2.service
# apachectl stop
# service apache2 start

# service apache2 status
# /etc/init.d/apache2 start
# /etc/init.d/apache2 reload



