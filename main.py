#Подключил лог, 

import smtplib
import os

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

email_from = "alexey.belyaev01@yandex.ru"
email_to = "alexey.belyaev01@yandex.ru"
subject = "Важно!"

message = """\
From: %email_from%
To: %email_to%
Subject:%subject%
Content-Type: text/plain; charset="UTF-8";
%text%
"""

friend_name = "Александр"
my_name = "Алексей"
website = "dvmn.org"

text = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""

text = text.replace("%my_name%",my_name).replace("%website%",website).replace("%friend_name%",friend_name)

message = message.replace("%email_from%", email_from).replace("%email_to%", email_to).replace("%text%", text).replace("%subject%", subject)

text = text.encode("UTF-8")
message = message.encode("UTF-8")

server.login(login, password)
server.sendmail(email_from, email_to, message)
server.quit()

print(text)
print(repr(message))
