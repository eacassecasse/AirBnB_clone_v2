# Configures a web server for deployment of web_static.

# Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

# Ensure Nginx is installed
package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
} ->

# Create necessary directories
file { '/data':
  ensure  => 'directory',
} ->

file { ['/data/web_static', '/data/web_static/releases', '/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => 'directory',
} ->

# Create index.html for test directory
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School Puppet\n",
} ->

# Create symbolic link to current release
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
} ->

# Set ownership of /data to ubuntu
exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}

# Create index.html and 404.html for default Nginx directory
file { ['/var/www', '/var/www/html']:
  ensure => 'directory',
} ->

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School Nginx\n",
} ->

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n",
} ->

# Configure default Nginx site with custom configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf,
} ->

# Restart Nginx
exec { 'nginx restart':
  path    => '/etc/init.d/',
  refreshonly => true,
}
