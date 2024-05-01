def list_all_clients(queryset):
    if queryset == []:
        print('Aucun évènement trouvé')
        return
    
    for row in queryset:
        print(f'- ID: {row.id} | ID Unique: {row.unique_id} | Client: {row.client} | Total: {row.total_amount} | Restant : {row.total_amount_left}' +
              f'Signé: {row.statut_signed}')


def get_info_contract(bCreate):
    """ Récupères les informations du contrat à créer"""
    if bCreate is True:
        print('\n===============Enregistrement d\'un nouveau contrat===============\n')
    else:
        print('\n===============Modification d\'un contrat===============\n')
    unique_id = input('Merci de renseigner l\'identifiant unique : ')
    total_amount = input('\nMerci de renseigner le montant total : ')
    total_amount_left = input('\nMerci de renseigner (ou non) le reste à payer : ')

    return {'unique_id': unique_id, 'total_amount': total_amount, "total_amount_left": total_amount_left}

def get_info_filter_contract():
    print('\n===============Recherce d\'un contrat===============\n')
    print('\nMerci de renseigner le filter à appliquer (à l\'aide du numéro) :')
    print('1 - Recherche par ID')
    print('2 - Recherche par identifiant unique')

    while True:
        choice_filter = input('\nChoix : ')

        if not choice_filter in ["1", "2"]:
            print('Merci d\'entrer une valeur correcte')
        else:
            print(f'Choix {choice_filter} enregistré')
            break
    
    if choice_filter == '1':
        param = input('Merci de renseigner l\'identifiant souhaité : ')
    if choice_filter == '2':
        param = input('Merci de renseigner l\'identifiant unique souhaité : ')

    return {'param': param, 'choice': choice_filter}

def confirm_contract(el):
    print(f'ID: {el.id} | UniqueID: {el.unique_id} | Total: {el.total_amount} | Reste: {el.total_amount_left}\n')
    choice = input('Confirmez-vous ce choix ? (y pour oui, n pour non) ')

    if choice in ['y', 'yes', 'YES', 'oui', 'o', 'O', 'Y', 'OUI']:
        return True
    return False