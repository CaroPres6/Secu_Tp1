from ..utils.auth import *
from ..utils.crypto_utils import *
from ..data import *




## avec salt impossible trouver password

# mettre cette fonction dans crypto_utils quand fini et
# faire appel fonction
def look_each_psw():
    users_db = load_csv('data/passwords_plain.csv')
    # mettre les psw dans liste or smtg...
    for usr in users_db:
        username = usr['username']
        for psw in list :
            if check_login(username, psw, users_db, mode = 'password_only'):
                print('Login réussi')
            else:
                print('Login échoué')