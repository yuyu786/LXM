#ignore this file

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],
                              [Button.url("DEV", url="t.me/SourcePleaseOfficial")]])
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("Update", url="t.me/SourcePleaseOfficial")]])
    
