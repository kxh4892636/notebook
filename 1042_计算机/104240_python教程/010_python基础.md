---
id: 290892f2-2a4f-4754-8672-a23f65c5c2b5
---
# python 基础

## 基本语法

### 注释

**语法格式**

```python
# comments
```

### 多行表达式

**\\**

```python
>>> print('hello \
... word.')
hello word.
```

**()**

```python
>>> a, b, c = (1,
...            2,
...            3)
>>> print(a, b, c)
1 2 3
>>>
```

## 变量和常量

### 基本概念

**变量**

- 指向一个值得指针;

**常量**

- python 无常量类型;
- 但 python 假定变量名字母全部为大写字母的变量为常量;
- 但并不是真正意义上的常量, 可被改变.

### 赋值

**赋值**

```python
# 赋值
age = 18
# 批量复制
a = b = c = 1
# 分别赋值
a, b, c = 1, 2, 3
```

**使用前赋值**

- 变量使用前必须赋值, 否则报错;

**可变性**

```python
# 变量可在任何时刻改变,
# python 使用最新的当前值.
message = "Hello Python world!"
print(message) # Hello Python world!
message = "Hello Python Crash Course world!"
print(message) # Hello Python Crash Course world!
```

**赋值的本质**

- 首先创建一个对象,
- 其次创建一个变量,
- 再将其指向上步骤创建的对象,
- 变量实质是对对象的引用.
