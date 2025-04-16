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
            {'role': 'system', 'content': 'You are a helpful assistant.'},  # role 后面可以考虑使用传入角色
            {'role': 'user', 'content': prompt}
        ]
    )

    # print(completion)
    return completion.choices[0].message.content


def make_html(response):
    positions = find_all_occurrences(response, "```")
    if len(positions) > 1:
        response = response[positions[0]:positions[1]]
    response = response.split("```")[1]
    response = response.replace("html", "<html>")
    response = response.replace("<table>", "<table border=1>")
    response = response + "</html>"
    file = open("test.html", "w", encoding="utf-8")
    file.write(response)
    file.close()

    # 打开当前目录下的index.html文件
    url = file.name
    # 调用系统默认的打开html文件的方式，如果设置为记事本，则会用记事本打开T_T
    webbrowser.open(url)

# 生成markdown文件
def make_markdown(response):
    file = open("test.md", "w", encoding="utf-8")
    file.write(response)
    file.close()

    # 打开当前目录下的index.html文件
    url = file.name
    # 调用系统默认的打开html文件的方式，如果设置为记事本，则会用记事本打开T_T
    webbrowser.open(url)

# 查找字符串中所有指定子字符串的起始位置
def find_all_occurrences(text, substring):
    """
    查找字符串中所有指定子字符串的起始位置。

    该函数通过遍历文本，使用字符串的find方法定位子字符串的每个出现位置，并记录下来。
    当不再找到子字符串时，函数停止搜索并返回所有记录的位置。

    参数:
    text (str): 要搜索的文本。
    substring (str): 要查找的子字符串。

    返回:
    list: 包含所有找到的子字符串起始位置的列表。
    """
    positions = []  # 初始化一个空列表，用于存储子字符串的起始位置
    start = 0  # 初始化起始位置为0，从文本的开头开始查找

    while True:
        # 使用find方法从指定的起始位置开始查找子字符串
        start = text.find(substring, start)
        if start == -1:  # 如果找不到子字符串，find方法返回-1，跳出循环
            break
        positions.append(start)  # 找到子字符串，将其起始位置添加到列表中
        start += len(substring)  # 移动到下一个位置继续查找，避免重复查找已找到的子字符串

    return positions  # 返回所有找到的子字符串起始位置的列表



def get_completion_with_temperature(prompt, temperature):
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=get_openai_key(),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-max",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},  # role 后面可以考虑使用传入角色
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


def get_completion_from_messages_with_max_tokens(messages, model="qwen-max",
                                                 temperature=0, max_tokens=500):
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=get_openai_key(),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-max",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
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


def make_file(response, file_type="text"):
    if file_type == "text":
        file = open("test.txt", "w", encoding="utf-8")
    if file_type == "html":
        file = open("test.html", "w", encoding="utf-8")
    if file_type == "markdown":
        file = open("test.md", "w", encoding="utf-8")
    else:
        file = open("test.txt", "w", encoding="utf-8")
    file.write(response)
    file.close()

    # 打开当前目录下的index.html文件
    url = file.name
    # 调用系统默认的打开html文件的方式，如果设置为记事本，则会用记事本打开T_T
    webbrowser.open(url)


def get_completion_and_token_count(messages,
                                   model="qwen-max",
                                   temperature=0,
                                   max_tokens=500):
    """
    使用 OpenAI 的 GPT-3 模型生成聊天回复，并返回生成的回复内容以及使用的 token 数量。

    参数:
    messages: 聊天消息列表。
    model: 使用的模型名称。默认为"gpt-3.5-turbo"。
    temperature: 控制生成回复的随机性。值越大，生成的回复越随机。默认为 0。
    max_tokens: 生成回复的最大 token 数量。默认为 500。

    返回:
    content: 生成的回复内容。
    token_dict: 包含'prompt_tokens'、'completion_tokens'和'total_tokens'的字典，分别表示提示的 token 数量、生成的回复的 token 数量和总的 token 数量。
    """
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=get_openai_key(),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    # print(response)
    # print(response.choices[0].message)
    content = response.choices[0].message.content

    token_dict = {
        'prompt_tokens': response.usage.prompt_tokens,
        'completion_tokens': response.usage.completion_tokens,
        'total_tokens': response.usage.total_tokens,
    }

    return content, token_dict
