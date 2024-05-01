import users.controllers as uCtrl

def get_info_user(bCreate):
    if bCreate is True:
        print('\n===============Enregistrement d\'un nouvel utilisateur===============\n')
    else:
        print('\n===============Modification d\'un utilisateur===============\n')
    employe_number = input('Merci de renseigner le numéro unique : ')
    name = input('\nMerci de renseigner le nom : ')
    email = input('\nMerci de renseigner le mail : ')
    if bCreate is True:
        password = input('\nMerci de renseigner le password : ')
    print('\nMerci de renseigner un rôle (à l\'aide du numéro) pour votre utilisateur :')
    print('1 - Equipe de Gestion')
    print('2 - Equipe Commerciale')
    print('3 - Equipe Support')

    while True:
        role = input('\nChoix : ')

        if not role in ["1", "2", "3"]:
            print('Merci d\'entrer une valeur correcte')
        else:
            print(f'Choix {role} enregistré')
            break

    return {'en': employe_number, 'name': name, "email": email, "password": password if bCreate is True else None, "role":role}


def get_info_filter_user(bDel):
    if bDel is True:
        print('\n===============Suppression d\'un utilisateur===============\n')
    else:
        print('\n===============Modiciation d\'un utilisateur===============\n')
    print('\nMerci de renseigner le filter à appliquer (à l\'aide du numéro) :')
    print('1 - Recherche par ID')
    print('2 - Recherche par numéro employé')
    print('3 - Recherche par email')

    while True:
        choice_filter = input('\nChoix : ')

        if not choice_filter in ["1", "2", "3"]:
            print('Merci d\'entrer une valeur correcte')
        else:
            print(f'Choix {choice_filter} enregistré')
            break
    
    if choice_filter == '1':
        param = input('Merci de renseigner l\'identifiant souhaité : ')
    if choice_filter == '2':
        param = input('Merci de renseigner le numéro souhaité : ')
    if choice_filter == '3':
        param = input('Merci de renseigner le mail souhaité : ')

    return {'param': param, 'choice': choice_filter}


def list_all_users(queryset):
    if queryset == []:
        print('Aucun utilisateur trouvé')
        return
    
    for row in queryset:
        print(f'ID: {row.id} | Numéro employé: {row.employe_number} | Nom: {row.nom} | EMail: {row.email} | Rôle: {row.role}')

def confirm_user(user):
    print(f'ID: {user.id} | Numéro employé: {user.employe_number} | Nom: {user.nom} | EMail: {user.email} | Rôle: {user.role}\n')
    choice = input('Confirmez-vous ce choix ? (y pour oui, n pour non) ')

    if choice in ['y', 'yes', 'YES', 'oui', 'o', 'O', 'Y', 'OUI']:
        return True
    return False