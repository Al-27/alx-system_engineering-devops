#this is but a comment
file{ "${facts['home']}/.ssh/ssh_config":
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => 'HostName *\nIdentityFile ~/.ssh/school\nPasswordAuthentication no',
}
