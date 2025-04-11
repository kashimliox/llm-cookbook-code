lamp_review = """
我需要一盏漂亮的卧室灯，这款灯具有额外的储物功能，价格也不算太高。\
我很快就收到了它。在运输过程中，我们的灯绳断了，但是公司很乐意寄送了一个新的。\
几天后就收到了。这款灯很容易组装。我发现少了一个零件，于是联系了他们的客服，他们很快就给我寄来了缺失的零件！\
在我看来，Lumina 是一家非常关心顾客和产品的优秀公司！
"""



# # 1.1 情感倾向分析
from code.tool import get_completion
#
# prompt = f"""
# 以下用三个反引号分隔的产品评论的情感是什么？
#
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)



# prompt = f"""
# 以下用三个反引号分隔的产品评论的情感是什么？
#
# 用一个单词回答：「正面」或「负面」。
#
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)



# # 1.2 识别情感类型
# # 中文
# prompt = f"""
# 识别以下评论的作者表达的情感。包含不超过五个项目。将答案格式化为以逗号分隔的单词列表。
#
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)


# # 1.3 识别愤怒
# # 中文
# prompt = f"""
# 以下评论的作者是否表达了愤怒？评论用三个反引号分隔。给出是或否的答案。
#
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)



# #2.1 商品信息提取
# # 中文
# prompt = f"""
# 从评论文本中识别以下项目：
# - 评论者购买的物品
# - 制造该物品的公司
#
# 评论文本用三个反引号分隔。将你的响应格式化为以 “物品” 和 “品牌” 为键的 JSON 对象。
# 如果信息不存在，请使用 “未知” 作为值。
# 让你的回应尽可能简短。
#
# 评论文本: ```{lamp_review}```
# """
# response = get_completion(prompt)
# print(response)


# 2.2 综合情感推断和信息提取
# 中文
prompt = f"""
从评论文本中识别以下项目：
- 情绪（正面或负面）
- 审稿人是否表达了愤怒？（是或否）
- 评论者购买的物品
- 制造该物品的公司

评论用三个反引号分隔。将你的响应格式化为 JSON 对象，以 “情感倾向”、“是否生气”、“物品类型” 和 “品牌” 作为键。
如果信息不存在，请使用 “未知” 作为值。
让你的回应尽可能简短。
将 “是否生气” 值格式化为布尔值。

评论文本: ```{lamp_review}```
"""
response = get_completion(prompt)
print(response)



