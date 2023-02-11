import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6247758046:AAH3LjNStKjqFWNSLYlvE3WNFHShlQArVnk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJABu8PuUIVokl1gxNbhx8Qb5meG70oc3E9_K7TR7I0RYR_O_5MiV7ZBsYTZA8Y0O--YwoKLDqcz9M6UDHe_OyZi7AMiIPBnAnMdHdiiF52vyp-q-lVZnP3lb97gPEFxGIj4hVWF-z0Gw6VUa3C2Dr17MajoxOJzR2q2oXkTaQGmnB__NEeqscI_Pi43uMg1VMyNkZeQyDagvu9F8RsJOOEsELD3YJLAHZ6viMZmQUKMnpN9HYBKkPvoEUiSjeLq7kntjpX-LnmgDlIrGiPCrEbvHZFiy_-w33kLeQ5NWkCDrf_RiYo2VtNfTermPg3lhu2KKslP91a7OuVCwVuLBY1LgSw=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Devilian_Songs_Bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5381881866")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True" #optional
