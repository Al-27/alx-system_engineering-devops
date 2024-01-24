#this is but a comment
file{ '~/.ssh/ssh_config':
  ensure  => 'present',
  content => 'HostName *\nIdentityFile ~/.ssh/school\nPasswordAuthentication no'
}
