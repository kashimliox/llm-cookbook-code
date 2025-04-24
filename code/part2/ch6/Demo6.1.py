# 处理输入-链式

# 一、 提取产品和类别
from code.tool import get_completion_from_messages

delimiter = "####"

system_message = f"""
您将获得客户服务查询。
客户服务查询将使用{delimiter}字符作为分隔符。
请仅输出一个可解析的Python列表，列表每一个元素是一个JSON对象，每个对象具有以下格式：
'category': <包括以下几个类别：Computers and Laptops、Smartphones and Accessories、Televisions and Home Theater Systems、Gaming Consoles and Accessories、Audio Equipment、Cameras and Camcorders>,
以及
'products': <必须是下面的允许产品列表中找到的产品列表>

类别和产品必须在客户服务查询中找到。
如果提到了某个产品，它必须与允许产品列表中的正确类别关联。
如果未找到任何产品或类别，则输出一个空列表。
除了列表外，不要输出其他任何信息！

允许的产品：

Computers and Laptops category:
TechPro Ultrabook
BlueWave Gaming Laptop
PowerLite Convertible
TechPro Desktop
BlueWave Chromebook

Smartphones and Accessories category:
SmartX ProPhone
MobiTech PowerCase
SmartX MiniPhone
MobiTech Wireless Charger
SmartX EarBuds

Televisions and Home Theater Systems category:
CineView 4K TV
SoundMax Home Theater
CineView 8K TV
SoundMax Soundbar
CineView OLED TV

Gaming Consoles and Accessories category:
GameSphere X
ProGamer Controller
GameSphere Y
ProGamer Racing Wheel
GameSphere VR Headset

Audio Equipment category:
AudioPhonic Noise-Canceling Headphones
WaveSound Bluetooth Speaker
AudioPhonic True Wireless Earbuds
WaveSound Soundbar
AudioPhonic Turntable

Cameras and Camcorders category:
FotoSnap DSLR Camera
ActionCam 4K
FotoSnap Mirrorless Camera
ZoomMaster Camcorder
FotoSnap Instant Camera

只输出对象列表，不包含其他内容。
"""

# user_message_1 = f"""
#  请告诉我关于 smartx pro phone 和 the fotosnap camera 的信息。
#  另外，请告诉我关于你们的tvs的情况。 """
#
# messages = [{'role': 'system', 'content': system_message},
#             {'role': 'user', 'content': f"{delimiter}{user_message_1}{delimiter}"}]
#
# category_and_product_response_1 = get_completion_from_messages(messages)
#
# print(category_and_product_response_1)


# user_message_2 = f"""我的路由器不工作了"""
# messages =  [{'role':'system','content': system_message},
#              {'role':'user','content': f"{delimiter}{user_message_2}{delimiter}"}]
# response = get_completion_from_messages(messages)
# print(response)




user_message_1 = f"""
 请告诉我关于所有产品类别的信息。请以严格的json格式返回 """

messages = [{'role': 'system', 'content': system_message},
            {'role': 'user', 'content': f"{delimiter}{user_message_1}{delimiter}"}]

category_and_product_response_1 = get_completion_from_messages(messages)
print(category_and_product_response_1)
