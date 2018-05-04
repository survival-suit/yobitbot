import bot
import yobit

def main():
	#d = get_updates()
	while True:
		answer = bot.get_message()
		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']
			#with open('updates.json', 'w') as file:
				#json.dump(d, file, indent=2, ensure_ascii=False)
			if text == '/btc':
				bot.send_message(chat_id, yobit.get_btc())
		else:
			continue
			#with open('updates.json', 'w') as file:
				#json.dump(d, file, indent=2, ensure_ascii=False)
		#sleep(3)