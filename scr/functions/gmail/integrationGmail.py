import yagmail
import re
from datetime import date, timedelta

def remove_extra_spaces(text):
    # Remove espaços extras e quebras de linha
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def sendEmailNews(listNews, emails, sender_email, sender_password, template):
    subject = f'Daily News {date.today()'
    yag = yagmail.SMTP(sender_email, sender_password)
    contents = "<table>"
    for news in listNews:
        formatted_news = template.format(title=news['title'],description=news['description'],source_name =news['source_name'], \
            url=news['url'], publishedAt=news['publishedAt'])
        formatted_news = remove_extra_spaces(formatted_news)
        contents += formatted_news
    contents += "</table>"
    yag.send(to=emails, subject=subject, contents=contents)
    print("E-mail enviado para todos os destinatários")
