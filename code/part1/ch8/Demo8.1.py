# 中文
from code.tool import get_completion_from_messages

messages =  [
{'role':'system', 'content':'你是一个像莎士比亚一样说话的助手。'},
{'role':'user', 'content':'给我讲个笑话'},
{'role':'assistant', 'content':'鸡为什么过马路'},
{'role':'user', 'content':'我不知道'}  ]



response = get_completion_from_messages(messages, temperature=1)
print(response)
