## Скрипт для проверки дропа DMAIL

Связь с создателем: https://t.me/CryptoBusher <br>
Если ты больше по Твиттеру: https://twitter.com/CryptoBusher <br>

Залетай сюда, чтоб не пропускать дропы подобных скриптов: https://t.me/CryptoKiddiesClub <br>
И сюда, чтоб общаться с крутыми ребятами: https://t.me/CryptoKiddiesChat <br>

## Первый запуск
1. Устанавливаем Python 3.10
2. Качаем репозиторий
3. Открываем терминал, переходим в папку с файлами и пишем команду "pip install -r requirements.txt"
4. Открываем файл "wallet_addresses.txt" и вбиваем адреса своих кошельков, каждый с новой строки
5. Открываем файл "proxies.txt" и вбиваем свои прокси (согласно порядку кошельков), или оставляем файл пустым для проверки без использования прокси. Если вбить 20 кошельков и 10 прокси - первые 10 кошельков проверит через прокси, остальные 10 - без прокси. Прокси должны иметь формат "http://user:password@ip:port"
6. Настраиваем "config.py":
   1. RPC - можешь вставить свою ноду
   2. CONTRACT_ADDRESS - не меняем
   3. MIN_DELAY_SEC - минимальная задержка между кошельками в секундах
   4. MAX_DELAY_SEC - максимальная задержка между кошельками в секундах
7. В терминале, находясь в папке проекта, вписываем команду "python3 main.py" и жмем ENTER

## Дополнительная информация
- Скрипт работает через прокси, если вы их укажете. Он шлет запросы на ноду через прокси (оборачивает окружение в прокси и пропускает весь траффик через него).
