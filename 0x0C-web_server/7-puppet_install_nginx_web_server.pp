# Puppet manifest containing commands to automatically configure an Ubuntu machine

package { 'nginx':
  ensure => installed,
}

file_line {'install':
  ensure        => 'present',
  path          => '/etc/nginx/sites-enabled/default',
  insert_after  => 'listen 80 default_server;',
  line          => 'rewrite ^/redirect_me https://www.github.com/josephorokpo permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
