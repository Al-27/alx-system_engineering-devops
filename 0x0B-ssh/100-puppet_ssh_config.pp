#this is but a comment
file { '/etc/ssh':
  ensure => 'directory',
}
file{ "/etc/ssh/ssh_config":
  ensure  => 'present',
  content => 'HostName *\nIdentityFile ~/.ssh/school\nPasswordAuthentication no',
}
