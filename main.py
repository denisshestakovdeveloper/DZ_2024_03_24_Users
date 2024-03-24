#Регистрация пользователей
#Хранение данных - файл Users.txt - список пользователей. {Имя пользователя}.txt - данные пользователя

class User:
    def __init__(self, userName, userPsw):
        self._userName = userName
        self._userPsw = userPsw

    def WriteUser(self):
        with open(f'{self._userName}.txt', 'w') as user:
            user.write(f'psw:{self._userPsw}')

class Users:
    def __init__(self):
        self._usersFileName = 'users.txt'
        try:
            with open(self._usersFileName,'r') as file:
                self._usersList = list(map(lambda x: x.replace('\n',''),file.readlines()))
                print(self._usersList)
        except:
            self._usersList = list()

    def addUser(self, userName: str, userPsw: str) -> bool:

        if not userName in self._usersList:
            user = User(userName, userPsw)
            user.WriteUser()

            self._usersList.append(userName)
            with open(self._usersFileName,'w') as file:
                file.writelines(f"{line}\n" for line in self._usersList)
        else:
            print('Такой пользователь уже существует!')

users = Users()

userName = input('Введите имя пользователя: ')
userPsw = input('Введите пароль: ')

users.addUser(userName, userPsw)
