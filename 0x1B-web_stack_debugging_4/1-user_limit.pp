# Grant the user holberton permission to log in and access files seamlessly.

# Enhance the hard file limit for the Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# Amplify the soft file limit for the Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
