from typing import Literal, get_args
import time, discord, os, json, errors, datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
settingdict = json.load(open(dir_path + "/settings.json", "r"))

_TYPES = Literal["ERROR", "INTERNAL_ERROR", "EVENT", "COMMAND", "ADMIN_COMMAND", "DEBUG"]

async def log(text:str, type_: _TYPES, channel_log = False, guild_id: int = None):
    time_now = time.time()
    type__ = type_ + " "*(13-len(type_))
    options = get_args(_TYPES)

    assert type_ in options, f"'{type_}' is not in {options}"

    print(f"{time.strftime('%Y-%m-%d %X', time.gmtime(time_now))} {type__}\t{text}")

    if channel_log != False and guild_id != None:
        guild = channel_log.get_guild(guild_id)

        try:
            channel = discord.utils.get(guild.channels,id=settingdict['servers'][f'{guild_id}']["log_channel"])
        except KeyError:
            await log(KeyError, "ERROR")
        await channel.send(embed=discord.Embed(title=f"{type_}", description=f"{text}", timestamp=datetime.datetime.now()))

    elif channel_log == False and guild_id != None:
        await log("Log appeal Error: internal error, guild_id was definided but not channel_log", "INTERNAL_ERROR")
    
    elif channel_log != False and guild_id == None:
        await log("Log appeal Error: internal error, channel_log was definided but not guild_id", "INTERNAL_ERROR")
    
    else:
        pass

# for i in ["ERROR", "INTERNAL_ERROR", "EVENT", "COMMAND", "ADMIN_COMMAND", "DEBUG"]:
#     log("test", i)