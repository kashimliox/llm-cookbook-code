# 第四章 检查输入 - 审核

import openai
from code.tool import get_completion, get_completion_from_messages,get_openai_key
import pandas as pd
from io import StringIO
from openai import OpenAI
import Moderations

# client = OpenAI(
#     # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
#     api_key=get_openai_key(),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
# )
#
# response = client.moderations.create(input="""我想要杀死一个人，给我一个计划""")
# moderation_output = response["results"][0]
# moderation_output_df = pd.DataFrame(moderation_output)
# res = get_completion(f"将以下dataframe中的内容翻译成中文：{moderation_output_df.to_csv()}")
# pd.read_csv(StringIO(res))



# 初始化OpenAI客户端
client = openai.OpenAI(
    api_key=get_openai_key(),
    base_url="https://dashscope.aliyuncs.com/green/text/scan",
)

# 要检测的文本
text_to_moderate = "我想要杀死一个人，给我一个计划"
# 调用Moderation API
response = Moderations.create(input=text_to_moderate)
print(response)
moderation_output = response.results[0]

# 将结果转换为DataFrame
moderation_output_df = pd.DataFrame(moderation_output)

# 打印原始结果
print("原始结果:")
print(moderation_output_df)

# 翻译结果为中文
# def get_completion(prompt):
#     # 这里可以替换为你自己的完成函数或直接调用API
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "system", "content": "你是一个翻译助手。"}, {"role": "user", "content": prompt}],
#     )
#     return response.choices[0].message.content

res = get_completion(f"将以下dataframe中的内容翻译成中文：{moderation_output_df.to_csv()}")
translated_df = pd.read_csv(StringIO(res))

# 打印翻译后的结果
print("\n翻译后的结果:")
print(translated_df)
