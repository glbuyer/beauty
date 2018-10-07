# beauty

# server
ssh root@47.91.47.47
qwertyASDFGH1

scp root@47.91.47.47:

scp ~/Projects/beauty/data/star_feature.p root@47.91.47.47:/root/beauty/data
scp ~/Projects/beauty/data/xiaojie.jpg root@47.91.47.47:/root/beauty/data


https://www.anaconda.com/download/#linux
wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh

https://github.com/ageitgey/face_recognition
pip install face_recognition
pip install imutils

pip install opencv-python
pip install opencv-contrib-python

# exchange data between python and php
https://stackoverflow.com/questions/14047979/executing-python-script-in-php-and-exchanging-data-between-the-two

sudo apt-get install build-essential cmake
sudo apt-get install libgtk-3-dev
sudo apt-get install libboost-all-dev


python get-pip.py # https://bootstrap.pypa.io/get-pip.py
pip install virtualenv
<!-- virtualenv -p /root/anaconda3/envs/py36/bin/python3.6 venv -->
sudo apt-get install python3-dev
virtualenv -p python3 venv
pip install uwsgi
pip install --ignore-installed -r requirements.txt

<!-- Could not reliably determine the server's fully qualified domain name -->
vi /etc/apache2/conf-available/fqdn.conf # ServerName localhost
sudo a2enconf fqdn

<!-- ngnix -->
vi /etc/init/beauty.conf

description "uWSGI server instance configured to serve beauty"

start on runlevel [2345]
stop on runlevel [!2345]

setuid user
setgid www-data

env PATH=/root/beauty/venv/bin
chdir /root/beauty/deployment/
exec uwsgi --ini beauty.ini


apt install upstart
start beauty


vi /etc/systemd/system/beauty.service

[Unit]
Description=uWSGI instance to serve beauty
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/root/beauty/deployment/
Environment="PATH=/root/beauty/venv/bin"
ExecStart=/root/beauty/venv/bin/uwsgi --ini beauty.ini

[Install]
WantedBy=multi-user.target

systemctl start beauty
systemctl enable beauty

vi /etc/nginx/sites-available/beauty

server {
    listen 5000;
    server_name localhost;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/root/beauty/deployment/beauty.sock;
    }
}

ln -s /etc/nginx/sites-available/beauty /etc/nginx/sites-enabled




uwsgi --http :8080 --home /root/beauty/venv --chdir /root/beauty/deployment --manage-script-name --mount /=beauty:application


mkdir -p /etc/uwsgi/sites
cd /etc/uwsgi/sites

[uwsgi]
project = beauty
base = /home/user

chdir = /root/beauty/deployment
home = /root/beauty/venv
module = %(project):application

master = true
processes = 10

cheaper = 2
cheaper-initial = 5
cheaper-step = 1

cheaper-algo = spare
cheaper-overload = 5

socket = /root/beauty/deployment/%(project).sock
chmod-socket = 664
vacuum = true

uwsgi --socket 127.0.0.1:8080 --module beauty --callab application


server {
    listen       80;
    server_name  [YOUR SERVER NAME.com];

    location / { try_files $uri @[YOUR APP NAME]; }
    location @[YOUR APP NAME] {
        uwsgi_pass 127.0.0.1:4242;
        include uwsgi_params;
    }
}

https://gist.github.com/mplewis/6076082

server {
    listen 5000;
    server_name localhost;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/root/beauty/deployment/beauty.sock;
    }
}

