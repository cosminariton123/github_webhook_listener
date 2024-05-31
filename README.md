# GitHub webhook server listener

The default behaveiour is to call ACTION function provided in config_info_that_shouldnt_appear_on_git.py when a pull request has been merged and closed on master/main and X-Hub-Signature-256 passes.  
It ignores requests that lack X-Hub-Signature-256 header or that have a non-passing X-Hub-Signature-256.
It ignores pushes straight to master.

## Single threaded behaviour

The HTTP server will serve indefinetly on a single thread, processing requests at the time of arrival.  
While the server is processing the request, new requests may timeout as there doesn't exist a queue for requests
and no other threads are spawned.

## How to use the framework

### Configuration files

Edit config.py file or create and edit config_info_that_shouldnt_appear_on_git.py as per your liking.  
Be warned that only "utf-8" ENCODING was tested.  
Be warned that only the default CONTROOLERS_FOLDER_PATH was tested. You should definetly copy **init**.py to the new directory.

PORT should be a number.  
SSID should be a string with the Wifi name. Set it to a random or empty string if not used on a Raspberry Pi Pico W.  
WLAN_KEY should be a string with the Wifi password. Set it to a random or empty string if not used on a Raspberry Pi Pico W.  
PRODUCTION should be a boolean True | False.  
SECRET_TOKEN should be the secret string from GitHub->Settings->Webhooks->//your_webhook//->Secret as a Python string  
ACTION should be a function that YOU define. It will be called everytime a pull request is merged and closed on master/main assuming that the main thread is not busy.

#### Examples Raspberry Pi Pico W

PORT = 1234  
SSID = "MyAwesomeWify"  
WLAN_KEY = "mySecureWifiPassword"  
PRODUCTION = False

SECRET_TOKEN = "mySecureGitHubSecretToken"

#### Examples non Raspberry Pi Pico W

PORT = 1234  
SSID = ""  
WLAN_KEY = ""  
PRODUCTION = False

def ACTION():  
{TAB}print("Hello World, a pull request has been merged and closed on master/main")

### Controllers

Create controller files or edit the existing ones in controllers directory.  
The structure and implementations should be simillar to the examples provided in controllers directory.
