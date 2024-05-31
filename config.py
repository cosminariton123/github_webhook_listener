from config_info_that_shouldnt_appear_on_git import PORT, SSID, WLAN_KEY, SECRET_TOKEN

PORT = PORT
SSID = SSID
WLAN_KEY = WLAN_KEY
ENCODING = 'utf-8'
CONTROOLERS_FOLDER_PATH = "controllers"
PRODUCTION = False  #If set to False, it will send the stacktrace as body alongside 500 InternalServerError

def _action():
    print("Hello World, a pull request has been merged and closed on master/main")

ACTION = _action
SECRET_TOKEN = SECRET_TOKEN
