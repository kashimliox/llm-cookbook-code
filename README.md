# llm-cookbook-code

基于[LLM Cookbook](https://datawhalechina.github.io/llm-cookbook)的代码实现


目前code.tool是基于阿里千问Max实现，其他公司请替换成对应的api接口,
示例代码中的
```python
from tool import get_completion
```
请自行全文替换为
```python
from code.tool import get_completion
```

.env文件的DASHSCOPE_API_KEY为所使用的千问max的API_KEY，请自行配置
