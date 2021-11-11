from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = "2033131007:AAETs-hoi7fGQAfJxUc6de6TKKLuGFc3nnk"  # Забираем значение типа str
ADMINS = [422738909]  # Тут у нас будет список из админов
IP = "localhost"  # Тоже str, но для айпи адреса хоста

