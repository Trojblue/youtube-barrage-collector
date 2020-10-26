import emoji
from barrage import *

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def format_out_msg(out_msg: str) -> str:
    """如果out_msg包含表情或者emoji, 不发送
    """
    # 去掉emoji
    no_emoji = emoji.demojize(out_msg).encode(
        'utf-8').decode('utf-8', 'ignore')

    # 有频道表情, 舍弃
    if ":" in no_emoji:
        return ''

    # 包含非字母, 舍弃
    # if not isEnglish(no_emoji):
    #     return ''

    return no_emoji

def has_same_message(d:dict, msg:str) -> bool:
    """检查相同str是否已有
    已有, 返回True
    没有, 添加msg, 返回False
    """
    msg_lower = msg.lower()
    if msg_lower in d.keys():
        return True
    else:
        d[msg_lower] = msg_lower
        return False

def write_to_txt(downloader:chat_downloader, out_file, chat_messages):
    """替换原线的写入txt功能
    各种长度限制直接这里实现了
    """
    d = {}
    f = open(out_file, 'w', encoding='utf-8')
    num_of_messages = 0  # reset count

    for message in chat_messages:
        if ('ticker_duration' not in message):  # needed for duplicates

            msg_to_print = downloader.message_to_string(message)

            if not msg_to_print:  # 空的, 不写入文件
                continue

            elif not isEnglish(msg_to_print):   # 非英语, 不写入文件
                continue

            elif not has_same_message(d, msg_to_print):  # 只写入不重复的
                num_of_messages += 1
                print(msg_to_print, file=f)

    f.close()



if __name__ == '__main__':
    d = {}

    print(has_same_message(d, "test"))
    print(has_same_message(d, "test"))
    print(has_same_message(d, "TEst"))
    print(d)
    # print(has_same_message(d, "test1"))
    # print(has_same_message(d, "test2"))
    # print(has_same_message(d, "test2"))


