#This is a Comment
exec { 'pkill "killmenow"':
  path    => ['/usr/bin', '/usr/sbin']
}
