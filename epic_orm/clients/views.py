def list_all_clients(queryset):
    """ Renvoies le visuel en fonction du queryset client """
    if queryset == []:
        print('Aucun Client trouvé')
        return

    for row in queryset:
        print(f'ID: {row.id} | Nom: {row.complete_name} | Mail: {row.email} | Entreprise: {row.enterprise_name} | Téléphone: {row.phone} |' +
              f'Contact commercial: {row.contact_commercial}')


def get_info_filter_client(display_title):
    """ Choix du filtre à appliquer """
    if display_title is True:
        print('\n===============Modification d\'un client===============\n')
    else:
        print('\n===============Recherche d\'un client===============\n')
    print('\nMerci de renseigner le filter à appliquer (à l\'aide du numéro) :')
    print('1 - Recherche par ID')
    print('2 - Recherche par nom complet')
    print('3 - Recherche par email')

    while True:
        choice_filter = input('\nChoix : ')

        if choice_filter not in ["1", "2", "3"]:
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


def confirm_client(el):
    """ Confirmation du client choisi """
    print(f'ID: {el.id} | Nom: {el.complete_name} | Mail: {el.email} | Entreprise: {el.enterprise_name}\n')
    choice = input('Confirmez-vous ce choix ? (y pour oui, n pour non) ')

    if choice in ['y', 'yes', 'YES', 'oui', 'o', 'O', 'Y', 'OUI']:
        return True
    return False


def get_info_user(bCreate):
    if bCreate is True:
        print('\n===============Enregistrement d\'un nouvel client===============\n')
    else:
        print('\n===============Modification d\'un client===============\n')
    complete_name = input('Merci de renseigner le nom complet : ')
    email = input('\nMerci de renseigner le mail : ')
    phone = input('\nMerci de renseigner le téléphone : ')
    enterprise_name = input('\nMerci de renseigner le nom de l\'entreprise : ')

    return {'complete_name': complete_name, 'email': email,
            "phone": phone, "enterprise_name": enterprise_name}
