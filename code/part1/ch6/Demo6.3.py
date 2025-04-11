import code.tool  as tool

data_json = { "resturant employees" :[
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}
prompt = f"""
将以下Python字典从JSON转换为HTML表格，保留表格标题和列名,只输出html元素：{data_json}
"""
response = tool.get_completion(prompt)
print(response)



# display(HTML(response))

tool.make_html(response)
