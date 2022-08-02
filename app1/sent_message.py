import requests

BOT_TOKEN = "5388672945:AAGH_7J0Nc1IKOQC79O_tjw05djEbP44lfA"
MAIN_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?"
ADMIN_CHAT_ID = 1330068715
DEFAULT_MESSAGE = {
    "chat_id" : ADMIN_CHAT_ID,
    "text" : "blank",
}

generate_url = lambda x: "&".join([f"{k}={v}" for k,v in x.items()])
message_tg = 'Yangi xabar:\n\n Ism: {}\n Email: {}\n Tel: {}\n Xabar: {}'


def send_message(message = "blank"):

    full_message = message.replace(' ', '+')
    DEFAULT_MESSAGE["text"] = full_message

    if len(full_message) > 4096:
        for x in range(0, len(full_message), 4096):
            DEFAULT_MESSAGE["text"] = full_message[x:x+4096]
            
            success = requests.get(
                url=MAIN_URL+generate_url(DEFAULT_MESSAGE)
            )
            
    else: success = requests.get( url=MAIN_URL+generate_url(DEFAULT_MESSAGE))

    return success.status_code == 200



if __name__ == "__main__":
    print(send_message(message="Salom akasi"))