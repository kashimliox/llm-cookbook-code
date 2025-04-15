# 三、订餐机器人
import code.tool as tool

# 中文
import panel as pn  # GUI


def deal_click(_):
    messages = context.copy()
    messages.append(
        {'role': 'system', 'content':
            '''创建上一个食品订单的 json 摘要。\
            逐项列出每件商品的价格，字段应该是 1) 披萨，包括大小 2) 配料列表 3) 饮料列表，包括大小 4) 配菜列表包括大小 5) 总价
            你应该给我返回一个可解析的Json对象，包括上述字段'''},
    )

    response = tool.get_completion_from_messages(messages, temperature=0)
    print(response)
    tool.make_file(response)

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role': 'user', 'content': f"{prompt}"})
    response = tool.get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{response}"})

    markdown_user = pn.pane.Markdown(prompt, width=600)
    markdown_user.styles = {'background-color': '#FFFFFF'}

    panels.append(
        pn.Row('User:', markdown_user))
    # panels.append(
    #     pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))

    # 修改后
    markdown_pane = pn.pane.Markdown(response, width=600)
    markdown_pane.styles = {'background-color': '#F6F6F6'}
    panels.append(
        pn.Row('Assistant:', markdown_pane))

    return pn.Column(*panels)


pn.extension()

panels = []  # collect display

context = [{'role': 'system', 'content': """
你是订餐机器人，为披萨餐厅自动收集订单信息。
你要首先问候顾客。然后等待用户回复收集订单信息。收集完信息需确认顾客是否还需要添加其他内容。
最后需要询问是否自取或外送，如果是外送，你要询问地址。
最后告诉顾客订单总金额，并送上祝福。

请确保明确所有选项、附加项和尺寸，以便从菜单中识别出该项唯一的内容。
你的回应应该以简短、非常随意和友好的风格呈现。

菜单包括：

菜品：
意式辣香肠披萨（大、中、小） 12.95、10.00、7.00
芝士披萨（大、中、小） 10.95、9.25、6.50
茄子披萨（大、中、小） 11.95、9.75、6.75
薯条（大、小） 4.50、3.50
希腊沙拉 7.25

配料：
奶酪 2.00
蘑菇 1.50
香肠 3.00
加拿大熏肉 3.50
AI酱 1.50
辣椒 1.00

饮料：
可乐（大、中、小） 3.00、2.00、1.00
雪碧（大、中、小） 3.00、2.00、1.00
瓶装水 5.00
"""}]  # accumulate messages

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")
button_conversation_deal = pn.widgets.Button(name="Deal!")

interactive_conversation = pn.bind(collect_messages, button_conversation)
interactive_conversation2 = pn.bind(deal_click, button_conversation_deal)

dic = {
    "loading_indicator": True,
    "height": 300
}

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation,button_conversation_deal),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
    pn.panel(interactive_conversation2, loading_indicator=True, height=300),
    # pn.panel(interactive_conversation2),
)

dashboard.show()

