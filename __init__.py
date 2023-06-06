# -*- coding: utf-8 -*-
import random
import yaml

from nonebot import on_keyword,on_notice
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.event import GroupMessageEvent, PokeNotifyEvent
from nonebot.rule import KeywordsRule, to_me
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.matcher import Matcher
from nonebot.log import logger
from pathlib import *

MainPath = Path("Config")
CPath=Path.joinpath(MainPath, "PSTC")

if not MainPath.is_dir():
    MainPath.mkdir()
if not CPath.is_dir():
    CPath.mkdir()

    PConfig = {
    "WhiteList":[],
    "WLMsg": [],
    "CanMsg": [],
    "CantMsg": [],
    }

    with open('./Config/PSTC/config.yml', 'w', encoding='GB2312') as f:
        yaml.dump(data=PConfig, stream=f, allow_unicode=True)
        logger.success("陪睡套餐Config文件创建成功，请按需调整配置项，路径:.Config/PSTC")

sleep = on_keyword('陪睡套餐',rule=KeywordsRule('陪睡套餐'))

@sleep.handle()
async def pstc(bot: Bot, event: GroupMessageEvent):
    with open('./Config/PSTC/config.yml', 'r', encoding='GB2312') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        WL=result['WhiteList']
        can=result['CanMsg']
        cant=result['CantMsg']
        WLMsg=result['WLMsg']

    if len(WL)==0:
        WLControl=False
    else:
        checktime=len(WL)
        for i in range(checktime):
            if str(event.user_id) in WL[i]:
                WLControl=True
                break
            else:
                WLControl=False
    
    if WLControl==True:
        if len(WLMsg)==0:
            msg="我不想陪你睡！"
        else:
            msg=WLMsg[random.randint(0,len(WLMsg)-1)]
        await sleep.send(MessageSegment.reply(event.message_id) + msg)
    else:
        try:
            await bot.set_group_ban(group_id=event.group_id, user_id=event.user_id, duration=3600)
            if len(can)==0:
                msg="晚安"
            else:
                msg=can[random.randint(0,len(can)-1)]
            await sleep.send(MessageSegment.reply(event.message_id) + msg)
        except:
            if len(cant)==0:
                msg="欺负我没法禁言你！"
            else:
                msg=cant[random.randint(0,len(cant)-1)]
            await sleep.send(MessageSegment.reply(event.message_id) + msg)
   
poke = on_notice(rule=to_me())

@poke.handle()
async def poke(matcher: Matcher, event: PokeNotifyEvent):
    if event.user_id==1186848360:
        pass
    else:
        time=random.randint(1,4)
        for i in range(time):
            await matcher.send(Message(f'[CQ:poke,qq='+ str(event.user_id) +']'))