# multiple-column layout

## column-count 属性

**作用**

- 设置为 multiple-column 布局.

**语法格式**

```css
.container {
  column-count: 3;
}
```

### 属性值

**auto**

- 根据其他 css 属性自动计算.
  - column-width 属性.

**\<integer\> 类型**

- 不作详述.

## column-width 属性

**作用**

- 设置为 multiple-column 列宽度.

**语法格式**

```css
.container {
  column-width: 120px;
}
```

### 属性值

**auto**

- 根据其他 css 属性自动计算.
  - column-count 属性.

**\<length\> 类型**

- 不作详述.

## column-rule 属性

**作用**

- 设置 multi-column 列间隔线样式.

**语法格式**

```css
.container {
  column-rule: thick inset blue;
}
```

**成分属性**

- column-rule-width 属性;
- column-rule-style 属性;
- column-rule-color 属性.

**简写机制**

- 随便写.

### column-rule-width 属性

**作用**

- 设置 multi-column 列间隔线粗细.

**语法格式**

```css
.container {
  column-rule-width: medium;
}
```

**属性值**

- 同 border-width 属性.

### column-rule-style 属性

**作用**

- 设置 multi-column 列间隔线样式.

**语法格式**

```css
.container {
  column-rule-style: dotted;
}
```

**属性值**

- 同 border-style 属性.

### column-rule-color 属性

**作用**

- 设置 multi-column 列间隔线颜色.

**语法格式**

```css
.container {
  column-rule-color: red;
}
```

**属性值**

- 同 border-color 属性.

## column-gap 属性

**作用**

- 设置为 multiple-column/flex/grid 列间隔.

**语法格式**

```css
.container {
  column-gap: 9px;
}
```

### 属性值

**normal**

- 使用浏览器默认值,
- multiple-column 为 1 em,
- 其余布局为 0.

**\<length\> 类型**

- 非负值.

**\<percentage\> 类型**

- 非负值.

## column-span 属性

**作用**

- 设置对应标签是否能够跨越 multi-column 所有列.

**语法格式**

```css
.container {
  column-span: all;
}
```

### 属性值

**none**

- 不可以跨列.

**all**

- 可以跨列.

## break-inside 属性

**作用**

- 设置是否允许单个标签内容中断,
- 分配至多个列.

**语法格式**

```css
.container {
  break-inside: avoid;
}
```

### 属性值

**auto**

- 允许中断.

**avoid**

- 不允许中断.
