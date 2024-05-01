def get_info_create_user():
    print('\n===============Enregistrement d\'un nouvel utilisateur===============\n')
    # role_id = Column(Integer, ForeignKey("role.id"))
    employe_number = input('Merci de renseigner le numéro unique : ')
    name = input('\nMerci de renseigner le nom : ')
    email = input('\nMerci de renseigner le mail : ')
    password = input('\nMerci de renseigner le password : ')
    print('\nMerci de renseigner un rôle (à l\'aide du numéro) pour votre utilisateur :')
    print('1 -Equipe de Gestion')
    print('2 -Equipe Commerciale')
    print('3 -Equipe Support')

    while True:
        role = input('\nChoix : ')

        if not role in ["1", "2", "3"]:
            print('Merci d\'entrer une valeur correcte')
        else:
            print(f'Choix {role} enregistré')
            break

    return {'en': employe_number, 'name': name, "email": email, "password": password, "role":role}