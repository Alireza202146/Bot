#نویسنده : @YourAnone_One 
import requests
import telebot
import json
import time 
from telebot import types
token = "5862480424:AAG5iBS6q_yQF5nUMxfB8YNhgOOWknlVOHo" #توکن رباتتون
bot = telebot.TeleBot(token)




ch = types.InlineKeyboardButton(text='YourAnonOne',url="t.me/YourAnone_One")
cookies = {
    '_ga': 'GA1.1.868853150.1686571031',
    'uid': '0ab9d21b837ac3f8',
    'clickAds': '53',
    'pushNotification': '92',
    'pushPage': '19',
    'XSRF-TOKEN': 'eyJpdiI6Ikoydk1rOUVmMExPOGF1WUMxWTNpTnc9PSIsInZhbHVlIjoiSE5VU0lSOTZnQnRhTGdDeE1cL3dIcDJmcmhWbm5IdU9wN3VNbytJck9DSjlVU2xqVkhPRUJuR21pS1JIUjRWSWRnYzZLXC8xXC9lNVJubWtOVlRHcjd1TFwvYU5sZFBCMkN6Y0pjZHNRWXJzMkYwcVE1aDMyR0xrb2x3SHlBU3ptbHZLIiwibWFjIjoiYzNjYjNhNWE4NGFlNzhmMTNlMTJiNGIxNDNmMDVjYThjZGUzZGU4ZjExMTEwN2QzNjgwNWE0OTNlNzE1ZDc1YyJ9',
    'aig_session': 'eyJpdiI6IlFPaGc0UnY2bjNIWmxKeTBIbDVjXC9BPT0iLCJ2YWx1ZSI6IktVck9mTWF5UDdxY3RFXC9WeW5kR0ZTOTM5U3RjalBaSnlSd05mUlhkanN2NStldDhaSWtFXC9IeXFlbFFFNHNrS09VS3J4V2NDVWVpd0lncFljWEhJMGlERWpHSGZ4bWZGQTN5RVF0Mm9jT0NhR0xnRGFEaEs5eTRLSFlCd01OckkiLCJtYWMiOiIwNDEzNDBkNTc2NTRkMTkxODc2ZmUxZTIzOGQ0ODU1MWZmYWQyM2NmNGQ3MGQwZGU0OWUyMjEzMmRhOGU2ODAyIn0%3D',
    '_ga_2S9JP0SPEL': 'GS1.1.1686741984.2.1.1686742384.0.0.0',
}

headers = {
    'authority': 'storiesig.info',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-none-match': 'W/"376-nN5i4Qu/s4Ex/bnNvBcI5Wa+U3U"',
    'referer': 'https://storiesig.info/en/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-token': 'null',
    'x-xsrf-token': 'eyJpdiI6Ikoydk1rOUVmMExPOGF1WUMxWTNpTnc9PSIsInZhbHVlIjoiSE5VU0lSOTZnQnRhTGdDeE1cL3dIcDJmcmhWbm5IdU9wN3VNbytJck9DSjlVU2xqVkhPRUJuR21pS1JIUjRWSWRnYzZLXC8xXC9lNVJubWtOVlRHcjd1TFwvYU5sZFBCMkN6Y0pjZHNRWXJzMkYwcVE1aDMyR0xrb2x3SHlBU3ptbHZLIiwibWFjIjoiYzNjYjNhNWE4NGFlNzhmMTNlMTJiNGIxNDNmMDVjYThjZGUzZGU4ZjExMTEwN2QzNjgwNWE0OTNlNzE1ZDc1YyJ9',
}

@bot.message_handler(commands=["start"])
def start(message):
	b = types.InlineKeyboardMarkup()
	b.add(ch)
	name = message.from_user.first_name
	bot.reply_to(message,f'🤖 سلام {name}\n\n🔎یوزرنیم پیج را وارد کنید:',reply_markup=b)

@bot.message_handler(func=lambda m:True)
def url(message):
	profile = types.InlineKeyboardButton(text="YourAnonOne",url="t.me/YourAnone_One")
	inn = types.InlineKeyboardMarkup()
	inn.add(profile)
	msgg = bot.send_message(message.chat.id, "*🔎 در حال دریافت اطلاعات ..*",parse_mode="markdown")
	time.sleep(1)
	bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
	try:
		url = requests.get(f'https://storiesig.info/api/ig/profile/{message.text}', cookies=cookies, headers=headers)
		data = json.loads(url.content)
		id = data['result']['id']
		user = data['result']['username']
		bio = data['result']['biography']
		name = data['result']['full_name']
		mn = data['result']['edge_owner_to_timeline_media']['count']
		followed = data['result']['edge_followed_by']['count']
		follow = data['result']['edge_follow']['count']
		img = data['result']['profile_pic_url']
		bot.send_photo(message.chat.id,img)
		text = f'''
🔎 نام کاربری : {user}
🔎 اسم : {name}
🔎 بیوگرافی : {bio}
🔎 پست ها : {mn}
🔎 فالوور ها : {followed}
🔎 فالووینگ ها : {follow}
'''	
		bot.send_message(message.chat.id,text,reply_markup=inn)
	except:
		bot.reply_to(message,'error')
		
print('Bot Is Run ..')
bot.infinity_polling()
