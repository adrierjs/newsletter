from scr.functions.gmail.integrationGmail import sendEmailNews
from dotenv import load_dotenv
from scr.functions.template.readHTML import read_html_file
from functions.newsAPI.dataFormatingNews import listNews
from scr.functions.newsAPI.integrationDataBaseNewsAPI import list_emails
import os

load_dotenv()
PASSWORD = os.getenv('PASSWORD')
sender_email = 'dadosclimaticos.uepb@gmail.com'
sender_password = PASSWORD
template = read_html_file('functions/template/template.html')
list_emails = ['adrierj@gmail.com']
sendEmailNews(listNews, list_emails, sender_email, sender_password, template)

