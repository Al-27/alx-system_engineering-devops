#this is but a comment
file{ "${facts['home']}/.ssh/ssh_config":
  ensure  => 'present',
  content => 'HostName *\nIdentityFile ~/.ssh/school\nPasswordAuthentication no',
}
