def get_info_create_user():
    print('\n===============Enregistrement d\'un nouvel utilisateur===============\n')
    # role_id = Column(Integer, ForeignKey("role.id"))
    employe_number = input('Merci de renseigner le numéro unique : ')
    name = input('\nMerci de renseigner le nom : ')
    email = input('\nMerci de renseigner le mail : ')
    password = input('\nMerci de renseigner le password : ')
    print('')

    return {'en': employe_number, 'name': name, "email": email, "password": password}