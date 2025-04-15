import panel as pn


# def greet(name="World"):
#     return f"hellow {name}!"
#
#
# greeting = pn.interact(greet)


def greeting(text="World"):
    print("Hello {}".format(text))


greeting = pn.interact(greeting, text="IPython Widgets")
greeting.show()
