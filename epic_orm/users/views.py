def get_info_create_user():
    print('Enregistrement d\'un nouvel utilisateur :')
    # role_id = Column(Integer, ForeignKey("role.id"))
    employe_number = input('Merci de renseigner le numéro unique : ')
    name = input('\nMerci de renseigner le nom : ')
    email = input('\nMerci de renseigner le mail : ')
    password = input('\nMerci de renseigner le password : ')