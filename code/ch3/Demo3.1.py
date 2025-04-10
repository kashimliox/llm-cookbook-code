# 示例：产品说明书
fact_sheet_chair = """
概述

    美丽的中世纪风格办公家具系列的一部分，包括文件柜、办公桌、书柜、会议桌等。
    多种外壳颜色和底座涂层可选。
    可选塑料前后靠背装饰（SWC-100）或10种面料和6种皮革的全面装饰（SWC-110）。
    底座涂层选项为：不锈钢、哑光黑色、光泽白色或铬。
    椅子可带或不带扶手。
    适用于家庭或商业场所。
    符合合同使用资格。

结构

    五个轮子的塑料涂层铝底座。
    气动椅子调节，方便升降。

尺寸

    宽度53厘米|20.87英寸
    深度51厘米|20.08英寸
    高度80厘米|31.50英寸
    座椅高度44厘米|17.32英寸
    座椅深度41厘米|16.14英寸

选项

    软地板或硬地板滚轮选项。
    两种座椅泡沫密度可选：中等（1.8磅/立方英尺）或高（2.8磅/立方英尺）。
    无扶手或8个位置PU扶手。

材料
外壳底座滑动件

    改性尼龙PA6/PA66涂层的铸铝。
    外壳厚度：10毫米。
    座椅
    HD36泡沫

原产国

    意大利
"""



from code.tool import get_completion

# # Prompt ：基于说明书创建营销描述
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的营销描述。
#
# 根据```标记的技术说明书中提供的信息，编写一个产品描述。
#
# 技术说明: ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)



# # 优化后的 Prompt，要求生成描述不多于 50 词
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。
#
# 根据```标记的技术说明书中提供的信息，编写一个产品描述。
#
# 使用最多50个汉字。
#
# 技术规格：```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)
#
#
# # 由于中文需要分词，此处直接计算整体长度
# print("\r\n",len(response))


# # 优化后的 Prompt，说明面向对象，应具有什么性质且侧重于什么方面
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。
#
# 根据```标记的技术说明书中提供的信息，编写一个产品描述。
#
# 该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。
#
# 使用最多50个单词。
#
# 技术规格： ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)










# prompt = f"""
# 请输出Eminem的《Rap God》的歌词。
# """
# response = get_completion(prompt)
# print(response)


# # 优化后的 Prompt，说明面向对象，应具有什么性质且侧重于什么方面
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。
#
# 根据```标记的技术说明书中提供的信息，编写一个产品描述。
#
# 该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。
#
# 使用最多50个单词。
#
# 技术规格： ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)















# # 更进一步
# prompt = f"""
# 您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。
#
# 根据```标记的技术说明书中提供的信息，编写一个产品描述。
#
# 该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。
#
# 在描述末尾，包括技术规格中所有7个字符的产品ID。
#
# 使用最多50个单词。
#
# 技术规格： ```{fact_sheet_chair}```
# """
# response = get_completion(prompt)
# print(response)


# 要求它抽取信息并组织成表格，并指定表格的列、表名和格式
prompt = f"""
您的任务是帮助营销团队基于技术说明书创建一个产品的零售网站描述。

根据```标记的技术说明书中提供的信息，编写一个产品描述。

该描述面向家具零售商，因此应具有技术性质，并侧重于产品的材料构造。

在描述末尾，包括技术规格中每个7个字符的产品ID。

在描述之后，包括一个表格，提供产品的尺寸。表格应该有两列。第一列包括尺寸的名称。第二列只包括英寸的测量值。

给表格命名为“产品尺寸”。

将所有内容格式化为可用于网站的HTML格式。将描述放在<div>元素中。

技术规格：```{fact_sheet_chair}```
"""

response = get_completion(prompt)

response=response.replace("```html","<html>")
response=response.split("```")[0]
response=response+"</html>"

print(response)
# 表格是以 HTML 格式呈现的，加载出来


# display(HTML(response))

file = open("test.html", "w",encoding="utf-8")
file.write(response)
file.close()
import webbrowser

# 打开当前目录下的index.html文件
url = file.name
# 调用系统默认的打开html文件的方式，如果设置为记事本，则会用记事本打开T_T
webbrowser.open(url)