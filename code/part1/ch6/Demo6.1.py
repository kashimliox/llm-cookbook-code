from code.tool import get_completion


# # 1.1 翻译为西班牙语
# prompt = f"""
# 将以下中文翻译成西班牙语: \
# ```您好，我想订购一个搅拌机。```
# """
# response = get_completion(prompt)
# print(response)


# # 1.2 识别语种
# prompt = f"""
# 请告诉我以下文本是什么语种:
# ```Combien coûte le lampadaire?```
# """
# response = get_completion(prompt)
# print(response)


# # 1.3 多语种翻译
# prompt = f"""
# 请将以下文本分别翻译成中文、英文、法语和西班牙语:
# ```I want to order a basketball.```
# """
# response = get_completion(prompt)
# print(response)


# # 1.4 同时进行语气转换
# prompt = f"""
# 请将以下文本翻译成中文，分别展示成正式与非正式两种语气:
# ```Would you like to order a pillow?```
# """
# response = get_completion(prompt)
# print(response)


# 1.5 通用翻译器
user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                             # My screen is flashing
]
import time
for issue in user_messages:
    time.sleep(20)
    prompt = f"告诉我以下文本是什么语种，直接输出语种，如法语，无需输出标点符号: ```{issue}```"
    lang = get_completion(prompt)
    print(f"原始消息 ({lang}): {issue}\n")

    prompt = f"""
    将以下消息分别翻译成英文和中文，并写成
    中文翻译：xxx
    英文翻译：yyy
    的格式：
    ```{issue}```
    """
    response = get_completion(prompt)
    print(response, "\n=========================================")
