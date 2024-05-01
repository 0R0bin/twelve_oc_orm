import config_app.auth_controller as cAC

def add_roles():
    print('Ajout des rôles suivants dans la base de donneés :')
    print('\n1 - Gestion')
    print('2 - Commercial')
    print('3 - Support')

def add_first_user():
    print('\nCréation de l\'utilisateur admin, informations :')
    print('\nNom: Admin')
    print('Numéro employé: 123456789')
    print('Email: admin@admin.fr')
    print('Mot de passe: 123test456')
    print('Rôle: Gestion')

def check_perm(accepted_items):
    user = cAC.read_jwt_user_info()
    if user == 400:
        cAC.del_jwt()
        print('Merci de vous reconnecter. Jeton expiré')
        return False

    if user == 401:
        print('Merci de vous connecter.')
        return False

    if user is None:
        print('Une erreur est survenue')
        return False

    if not user['role'] in accepted_items:
        print('Vous n\'avez pas les droits nécessaires')
        return False
    
    return True