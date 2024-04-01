import json
import os
from client_services import rec_audio, recognize, play_res

play_res("You are in the installation setup of arduino assistant. Firstly What is your name ?")
name_audio = rec_audio()
name = recognize(name_audio)

data = {"name":name}

if not os.path.exists("account_info.json"):
    with open("account_info.json","w") as f:
        json.dump(data,f)
else:
    os.system("python arduino-assistant.py")



