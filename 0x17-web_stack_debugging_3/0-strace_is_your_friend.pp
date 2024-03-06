# Puppet manifest to fix bad `phpp` extensions to `php` in wp-settings.php

file { '/path/to/wp-settings.php':
  ensure  => file,
  content => template('path/to/wp-settings.php.erb'),
  notify  => Exec['fix_phpp_extension'],
}

exec { 'fix_phpp_extension':
  command     => "/bin/sed -i 's/phpp/php/g' /path/to/wp-settings.php",
  refreshonly => true,
  subscribe   => File['/path/to/wp-settings.php'],
}
