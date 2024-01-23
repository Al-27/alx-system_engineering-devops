#this is but a comment
file{ '~/.ssh/ssh_config':
  ensure  => 'present',
  mode    => '0744'
}

file_line{ 'ssh_config':
  ensure  => 'present',
  path    => '~/.ssh/ssh_config',
  line    => ['HostName *','IdentityFile ~/.ssh/school','PasswordAuthentication no']  
}
