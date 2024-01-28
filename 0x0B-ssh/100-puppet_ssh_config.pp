#this is but a comment
file{ "/etc/ssh/ssh_config":
  ensure  => 'present',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => 'HostName *\nIdentityFile ~/.ssh/school\nPasswordAuthentication no',
}
