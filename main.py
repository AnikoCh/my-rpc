import rpc
import time
from time import mktime

print("Discord Rich Presence")
client_id = '1044518339915022389'  # Your application's client ID as a string. (This isn't a real client ID)

time.sleep(1)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "Please trust me",  # anything you like
            "details": "Nah bro im not suspicious guy",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Jett",  # anything you like
                "small_image": "default",  # must match the image key
                "large_text": "Jett Pussy",  # anything you like
                "large_image": "default"  # must match the image key
            },
            "buttons": [
                {"label": "Press the pussy", "url": "https://www.google.com"},
            ]
        }
    try:
        rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
        print("RPC connection successful.")
        rpc_obj.set_activity(activity)
        time.sleep(900)
    except:
        print("Failed to set activity, trying again in 5 seconds")
        time.sleep(5)
