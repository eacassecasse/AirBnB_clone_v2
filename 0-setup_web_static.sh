#!/usr/bin/env bash
# Script to set up a web server for deployment of web_static.

# Update package index and install nginx
apt-get update
apt-get install -y nginx

# Create necessary directories and a simple index.html file
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link to the current release
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership and group for the /data directory
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Configure nginx server block
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://google.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# Restart nginx service to apply changes
service nginx restart
