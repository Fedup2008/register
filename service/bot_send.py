import requests
from datetime import datetime
import urllib.parse

kwargs = {
    'first_name': 'Abubakr',
    'last_name': 'Abdumalikov',
    'username': 'qwer',
    'email': 'updown744@gmail.com'
}

message = f"""
<b>🕒 {datetime.now().strftime('%d/%m/%y  %H:%M:%S')}</b>\n
<b>👤 Foydalanuvchi Ma'lumotlari:</b>\n
📛 <b>Ism:</b> {kwargs['first_name']}\n
🆔 <b>Familiya:</b> {kwargs['last_name']}\n
💻 <b>Username:</b> {kwargs['username']}\n
📧 <b>Email:</b> {kwargs['email']}
"""
encoded_message = urllib.parse.quote(message)
def send_msg(**kwargs):
    token = "7159794122:AAFZY8Tkd9Mcx8ZXdVFKDoYRv2nnJbw1rtg"  # bot token

    user_id = "1555717309"  # user id
    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text={encoded_message}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())
