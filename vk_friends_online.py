import vk
import vk.exceptions
import getpass


APP_ID = 6149601


def get_user_login():
    user_login = input('Login or e-mail: ')
    return user_login


def get_user_password():
    user_password = getpass.getpass('Password: ')
    return user_password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    list_id_friends_online = api.friends.getOnline()
    friends_online = api.users.get(user_ids=list_id_friends_online)
    return friends_online


def output_friends_to_console(friends_online):
    print('\n Online friends: \n')
    for friend_number, friend in enumerate(friends_online):
        print(str(friend_number + 1) + '. ' +
              friend['first_name'] + ' ' +
              friend['last_name'])
        print('------------------------')


if __name__ == '__main__':
    login = get_user_login()
    try:
        password = get_user_password()
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        print('Invalid login or password')
