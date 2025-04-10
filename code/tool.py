import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI


def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.environ['DASHSCOPE_API_KEY']



def get_completion(prompt):
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=get_openai_key(),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-max",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt}
        ]
    )

    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content

