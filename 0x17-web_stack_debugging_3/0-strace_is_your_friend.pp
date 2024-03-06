# Fixes Apache 500 error

exec { 'php Not parsed':
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}
