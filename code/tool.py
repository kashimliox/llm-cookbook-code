import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

import webbrowser

def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.environ['DASHSCOPE_API_KEY']

def get_openai_key_gpt():
    _ = load_dotenv(find_dotenv())
    return os.environ['OPENAI_API_KEY']




def get_completion(prompt):
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=get_openai_key(),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-max",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},#role 后面可以考虑使用传入角色
            {'role': 'user', 'content': prompt}
        ]
    )

    # print(completion)
    return completion.choices[0].message.content


def make_html(response):
    positions=find_all_occurrences(response,"```")
    if len(positions)>1:
        response = response[positions[0]:positions[1]]
    response = response.split("```")[1]
    response = response.replace("html", "<html>")
    response = response.replace( "<table>","<table border=1>")
    response = response + "</html>"
    file = open("test.html", "w", encoding="utf-8")
    file.write(response)
    file.close()

    # 打开当前目录下的index.html文件
    url = file.name
    # 调用系统默认的打开html文件的方式，如果设置为记事本，则会用记事本打开T_T
    webbrowser.open(url)


def make_markdown(response):
    file = open("test.md", "w", encoding="utf-8")
    file.write(response)
    file.close()

    # 打开当前目录下的index.html文件
    url = file.name
    # 调用系统默认的打开html文件的方式，如果设置为记事本，则会用记事本打开T_T
    webbrowser.open(url)

def find_all_occurrences(text, substring):
    positions = []
    start = 0

    while True:
        start = text.find(substring, start)
        if start == -1:
            break
        positions.append(start)
        start += len(substring)  # 移动到下一个位置继续查找

    return positions




def get_completion_with_temperature(prompt,temperature):
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=get_openai_key(),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-max",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},#role 后面可以考虑使用传入角色
            {'role': 'user', 'content': prompt}
        ],
        temperature=temperature
    )

    # print(completion)
    return completion.choices[0].message.content



def get_completion_from_messages(messages, model="qwen-max",
temperature=0):
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=get_openai_key(),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-max",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=messages,
        temperature=temperature,
    )

    # print(completion)
    return completion.choices[0].message.content


# def get_completion_from_messages_gpt(messages, model="gpt-3.5-turbo",
# temperature=0):
#     openai = OpenAI(
#         # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
#         api_key=get_openai_key(),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
#         base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
#     )
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=temperature, # 控制模型输出的随机程度
#     )
# #     print(str(response.choices[0].message))
#     return response.choices[0].message["content"]