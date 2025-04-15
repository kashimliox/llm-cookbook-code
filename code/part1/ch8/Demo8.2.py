# 中文
from code.tool import get_completion_from_messages

messages =  [
{'role':'system', 'content':'你是个友好的聊天机器人。'},
{'role':'user', 'content':'Hi, 我是Isa。'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
