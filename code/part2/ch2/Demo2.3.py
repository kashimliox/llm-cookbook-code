# 三、Helper function 辅助函数 (提问范式)


from code.tool import get_completion_from_messages_with_max_tokens
from code.tool import get_completion_and_token_count

# messages =  [
# {'role':'system',
#  'content':'你是一个助理， 并以 Seuss 苏斯博士的风格作出回答。'},
# {'role':'user',
#  'content':'就快乐的小鲸鱼为主题给我写一首短诗'},
# ]
# response = get_completion_from_messages(messages, temperature=1)
# print(response)


# # 长度控制
# messages =  [
# {'role':'system',
#  'content':'你的所有答复只能是一句话'},
# {'role':'user',
#  'content':'写一个关于快乐的小鲸鱼的故事'},
# ]
# response = get_completion_from_messages_with_max_tokens(messages, temperature =1)
# print(response)

messages =  [
{'role':'system',
 'content':'你是一个助理， 并以 Seuss 苏斯博士的风格作出回答。'},
{'role':'user',
 'content':'就快乐的小鲸鱼为主题给我写一首短诗'},
]
response, token_dict = get_completion_and_token_count(messages)
print(response)
print(token_dict)
