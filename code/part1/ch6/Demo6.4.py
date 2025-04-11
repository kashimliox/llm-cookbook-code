# 四、拼写及语法纠正
from code import get_completion

text = [
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for spelling abilitty"  # spelling
]

import time

# for i in range(len(text)):
#     time.sleep(20)
#     prompt = f"""请校对并更正以下文本，注意纠正文本保持原始语种，无需输出原始文本。
#     如果您没有发现任何错误，请说“未发现错误”。
#
#     例如：
#     输入：I are happy.
#     输出：I am happy.
#     ```{text[i]}```"""
#     response = get_completion(prompt)
#     print(i, response)




text2 = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt = f"校对并更正以下商品评论，不要输出你的评论：```{text2}```"
response = get_completion(prompt)
print(response)

import code.tool as tool

from redlines import Redlines
from IPython.display import display, Markdown

diff = Redlines(text2,response)
# display(Markdown(diff.output_markdown))

tool.make_markdown(diff.output_markdown)