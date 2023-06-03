# JSON 标准

## 基础

**语法规则**

- 键值对存储数据;
- 逗号分隔数据;
- 花括号存储对象;
- 方括号存储数组;

**键值对**

```json
// 键和值都需要双引号
{ "name": "Bill Gates" }
```

**JSON 值**

```json
// 字符串
{ "name":"Bill" }
// 数字
{ "age":30 }
// JSON 对象
{
"employee":{ "name":"Bill Gates", "age":62, "city":"Seattle" }
}
// 数组
{
  "sites": [
    { "name": "菜鸟教程", "url": "www.runoob.com" },
    { "name": "google", "url": "www.google.com" },
    { "name": "微博", "url": "www.weibo.com" }
  ]
}
// 布尔值
{ "sale":true }
// null
{ "middlename":null }
```

**嵌套**

```json
// 对象嵌套对象
myObj =  {
   "name":"Bill Gates",
   "age":62,
   "cars": {
	  "car1":"Porsche",
	  "car2":"BMW",
	  "car3":"Volvo"
   }
}
// 数组嵌套对象
myObj =  {
   "name":"Bill Gates",
   "age":62,
   "cars": [
	  { "name":"Porsche",  "models":[ "911", "Taycan" ] },
	  { "name":"BMW", "models":[ "M5", "M3", "X5" ] },
	  { "name":"Volvo", "models":[ "XC60", "V60" ] }
   ]
}
```
