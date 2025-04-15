# 中文
from code.tool import get_completion_from_messages
# # 1.2 友好的聊天机器人
# messages =  [
# {'role':'system', 'content':'你是个友好的聊天机器人。'},
# {'role':'user', 'content':'Hi, 我是Isa。'}  ]
# response = get_completion_from_messages(messages, temperature=1)
# print(response)


# # 中文
# messages =  [
# {'role':'system', 'content':'你是个友好的聊天机器人。'},
# {'role':'user', 'content':'好，你能提醒我，我的名字是什么吗？'}  ]
# response = get_completion_from_messages(messages, temperature=1)
# print(response)



# 中文
messages =  [  
{'role':'system', 'content':'你是个友好的聊天机器人。'},
{'role':'user', 'content':'Hi, 我是Isa'},
{'role':'assistant', 'content': "Hi Isa! 很高兴认识你。今天有什么可以帮到你的吗?"},
{'role':'user', 'content':'是的，你可以提醒我, 我的名字是什么?'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)
