#this is but a comment
file_line{'no pass':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no'
}
file_line{'id':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/school'

}
