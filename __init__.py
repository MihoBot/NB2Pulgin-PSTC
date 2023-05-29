import random

from nonebot import on_keyword,on_notice
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.adapters.onebot.v11.event import GroupMessageEvent, PokeNotifyEvent
from nonebot.rule import KeywordsRule, to_me
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.matcher import Matcher

sleep = on_keyword('陪睡套餐',rule=KeywordsRule('陪睡套餐'))

can=['晚安啦小笨蛋','想占便宜？没门！进小黑屋罢！']
cant=['呜呜呜欺负人！','可恶，没法禁言你！']
@sleep.handle()
async def pstc(bot: Bot, event: GroupMessageEvent):
    try:
        await bot.set_group_ban(group_id=event.group_id, user_id=event.user_id, duration=3600)
        index=random.randint(0,len(can)-1)
        await sleep.send(MessageSegment.reply(event.message_id) + can[index])
    except:
        index=random.randint(0,len(cant)-1)
        await sleep.finish(MessageSegment.reply(event.message_id) + cant[index])


poke = on_notice(rule=to_me())

@poke.handle()
async def poke(matcher: Matcher, event: PokeNotifyEvent):
    time=random.randint(1,4)
    for i in range(time):
        await matcher.send(Message(f'[CQ:poke,qq='+ str(event.user_id) +']'))