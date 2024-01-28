#this is but a comment
file{ '/home/.ssh/ssh_config':
  ensure  => 'present',
  content => 'HostName *\nIdentityFile ~/.ssh/school\nPasswordAuthentication no'
}
