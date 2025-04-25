
import json

def get_product_by_name(name):
    """
    根据产品名称获取产品

    参数:
    name: 产品名称
    """
    return products.get(name, None)

def get_products_by_category(category):
    """
    根据类别获取产品

    参数:
    category: 产品类别
    """
    return [product for product in products.values() if product["类别"] == category]


# 读取产品信息
with open("products_zh.json", "r", encoding='utf-8') as file:
    products = json.load(file)
# print(products)
# 将列表转换为字典
products = {product["名称"]: product for product in products}
# print(products)
pro=get_product_by_name("TechPro 超极本")# wishtoday的，咋这么多错
print(pro)