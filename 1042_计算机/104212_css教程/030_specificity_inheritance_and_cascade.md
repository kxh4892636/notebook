# 特殊性, 级联和继承

## 特殊性

**特殊性**

- 一套优先级算法,
- 如果同一标签被多个 css rule 匹配,
- 特殊性告诉浏览器应匹配哪一个 css rule.

**特殊性级别**

- Identifiers + Classes + Elements,
  - Identifiers: ID 选择器;
  - Classes: 类选择器, 属性选择器, 伪类;
  - Element: 元素选择器, 伪元素选择器.
- 越大优先级越高.

| 选择器        | Identifiers | Classes | Elements | 特殊性 |
| ------------- | ----------- | ------- | -------- | ------ |
| h1            | 0           | 0       | 1        | 001    |
| p.class       | 0           | 1       | 0        | 010    |
| h1 + p[class] | 0           | 1       | 1        | 011    |
| \#id          | 1           | 0       | 0        | 100    |

### !important 值

**语法格式**

- !important.

```css
#winning {
  background-color: red;
  border: 1px solid black;
}

.better {
  background-color: gray;
  border: none !important;
}
```

**机制**

- 无视特殊性,
- 强行将 !important 对应的样式,
- 设置为标签样式.

## 级联

**代码顺序优先级**

- 当 css rule 特殊性级别相同时,
- 浏览器匹配位于最后面的 css rule.

**css 规则优先级**

- 浏览器默认 style sheet;
- 用户 style sheet;
- 第三方 style sheet;
- 第三方 style sheet 中的 !important 声明;
- 用户 style sheet 中的 !important 声明;
- 浏览器默认 style sheet 中的 !important 声明.

## 继承

**继承**

- 子标签继承父标签的属性.

**可继承属性和不可继承属性**

- 可继承属性;
  - font;
  - color.
- 不可继承属性.
  - margin;
  - padding;
  - border.

### inherit

**语法格式**

```css
#sidebar h2 {
  color: inherit;
}
```

**机制**

- 表明子标签使用父标签对应样式.

### initial

**语法格式**

```css
#sidebar h2 {
  color: initial;
}
```

**机制**

- 表明子标签使用对应样式默认值,
- 不推荐使用.

### unset

**语法格式**

```css
#sidebar h2 {
  color: unset;
}
```

**机制**

- 如果子标签对应样式自然继承其父标签,
- 使用其父标签样式, 视同为 inherit.
- 否则视同为 initial.

### revert

**语法格式**

```css
#sidebar h2 {
  color: revert;
}
```

**机制**

- 如果子标签对应样式自然继承其父标签,
- 使用其父标签样式, 视同为 inherit.
- 否则恢复浏览器默认样式,
- 很多情况下和 unset 一致.

### all 属性

**语法格式**

```css
.fix-this {
  all: unset;
}
```

**作用**

- 用于控制继承,
- 属性值.
  - inherit;
  - unset;
  - initial;
  - revert.
