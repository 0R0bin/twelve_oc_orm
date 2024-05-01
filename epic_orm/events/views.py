def list_all_events(queryset):
    if queryset == []:
        print('Aucun évènement trouvé')
        return

    for row in queryset:
        print(f'- ID: {row.id} | Nom: {row.nom} | Date Début: {row.date_start} | Date Fin: {row.date_end}' +
              f'Localisation: {row.location} | Attendus: {row.attendees} | Notes : {row.notes} | Contrat : {row.contract}'
              + f'Support: {row.support} | Client: {row.client}\n')


def get_info_event(bCreate):
    if bCreate is True:
        print('\n===============Enregistrement d\'un nouvel évènement===============')
    else:
        print('\n===============Modification d\'un évènement===============')
    name = input('\nMerci de renseigner le nom : ')
    print('Les dates sont au format YYYY-MM-DD, exemple : 2024-05-01')
    print('Vous pouvez ajouter l\'heure exemple : 2024-05-01 08:00:00')
    date_start = input('Merci de renseigner la date de début : ')
    date_end = input('Merci de renseigner la date de fin : ')
    location = input('Merci de renseigner l\'adresse complète : ')
    attendees = input('Merci de renseigner le nombre de participants : ')
    notes = input('Merci d\'indiquer (ou non) des notes : ')

    return {'name': name, "date_start": date_start, "date_end": date_end, "location": location, 'attendees': attendees, 'notes': notes}


def get_info_filter_event(bDel):
    if bDel is True:
        print('\n===============Suppression d\'un évènement===============\n')
    else:
        print('\n===============Modiciation d\'un évènement===============\n')
    print('\nMerci de renseigner le filter à appliquer (à l\'aide du numéro) :')
    print('1 - Recherche par ID')
    print('2 - Recherche par nom')

    while True:
        choice_filter = input('\nChoix : ')

        if choice_filter not in ["1", "2"]:
            print('Merci d\'entrer une valeur correcte')
        else:
            print(f'Choix {choice_filter} enregistré')
            break

    if choice_filter == '1':
        param = input('Merci de renseigner l\'identifiant souhaité : ')
    if choice_filter == '2':
        param = input('Merci de renseigner le nom souhaité : ')

    return {'param': param, 'choice': choice_filter}


def confirm_event(event):
    print(f'ID: {event.id} | Nom: {event.nom} | Position: {event.location} | Notes: {event.notes}\n')
    choice = input('Confirmez-vous ce choix ? (y pour oui, n pour non) ')

    if choice in ['y', 'yes', 'YES', 'oui', 'o', 'O', 'Y', 'OUI']:
        return True
    return False


def choice_user_to_add():
    print('Merci de choisir l\'identifiant d\'un membre du support')
    choice = input('Confirmez-vous ce choix ? (y pour oui, n pour non) ')

    if choice in ['y', 'yes', 'YES', 'oui', 'o', 'O', 'Y', 'OUI']:
        return True
    return False
