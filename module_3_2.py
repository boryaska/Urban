def send_email(message, recipient, *, sender = "university.help@gmail.com"):

    def valid_correct(mail):
        if mail.find('@') == -1 or not (mail.endswith('.com') or mail.endswith('.net') or mail.endswith('.ru')):
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
            return False
        return True

    def send():
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
            return False
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            return False
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
            return False
        
    check = valid_correct(recipient)
    if check:
        check = valid_correct(sender)
    if check:
        send()

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')        


