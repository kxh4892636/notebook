# 表单样式

## css 对不同控件的支持

**good**

- 易于设计;
  - \<form\>;
  - \<fieldset\> 和 \<legend\>;
  - 除了 \<input type = "search"\> 的文本控件;
  - \<textarea\>;
  - \<button\> 和 \<input type = "button"\>;
  - \<label\>;
  - \<output\>.

**bad**

- 比较困难;
  - \<input type = "checkbox"\>;
  - \<input type = "radio"\>;
  - \<input type = "search"\>.

**ugly**

- 几乎无法被设计;
- 其他控件.
  - 下拉控件;
  - 时间控件;
  - \<range\>.

## good

### 字体和文本

**css 属性**

- font-family;
- font-size.

**语法格式**

```css
button,
input,
select,
textarea {
  font-family: inherit;
  font-size: 100%;
}
```

### 盒子模型

**css 属性**

- width/height;
- padding/margin/border;
- box-sizing;

**语法格式**

```css
input,
textarea,
select,
button {
  width: 150px;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
```

**box-sizing 的使用**

- 不同控件具有自己的 padding 和 border,
- 可使用 box-sizing 统一管理.

### \<legend\> 控件位置

**语法格式**

```css
fieldset {
  position: relative;
}

legend {
  position: absolute;
  bottom: 0;
  right: 0;
}
```

**机制**

- \<fieldset\> 控件设置 `position: relative`,
  - 建立 contain blocking;
- \<legend\> 控件设置 `position: absolute`,
  - 控制其位置.

## bad

### Appearance 属性

**作用**

- 在系统层级上修改表单控件样式,
- 主要用于 bad 和 ugly.

**语法格式**

```css
input {
  appearance: none;
}
```

#### 属性值

**none**

- 不使用任何默认样式.

**auto**

- 使用浏览器默认样式.

### 搜素框

**主要问题**

- safari 无法设置 height 和 font-size.

**解决方法**

- 使用 appearance 消除默认样式,
- 在自定义样式.

### 复选框和单选框

**主要问题**

- 不同浏览器的默认样式不同,
- 修改样式显示结果稀奇古怪.

**解决方法**

- 使用 appearance 消除默认样式,
- 在自定义样式.

## ugly

**主要问题**

- 不同浏览器的默认样式及其不同,
- 修改样式显示结果稀奇古怪.

### selects 和 datalist

**主要问题**

- 下拉箭头不同浏览器样式不同;
- 无法控制下拉选项样式.

**解决方法**

- 创建自定义按钮代替两者;
- 下拉箭头;
  - 使用 appearance 属性.
- 下拉选项.
  - 使用 multiple 属性,
  - 将所有下拉选项全部显示出来.

**select 自定义下拉箭头问题**

- \<select\> 无法使用 ::before 和 ::after,
- 需要在其外嵌套一层父标签,
- 对父标签使用伪类.

```html
<div class="select-wrapper">
  <select id="select" name="select">
    <option>Banana</option>
    <option>Cherry</option>
    <option>Lemon</option>
  </select>
</div>
```

```css
.select-wrapper::after {
  content: "▼";
  font-size: 1rem;
  top: 6px;
  right: 10px;
  position: absolute;
}
```

### 时间控件

**主要问题**

- 时间控件外部样式容易设置,
- 但其内部日历无法设置其样式.

**解决方法**

- 需使用 appearance 属性,
- 如需完全控制样式,
- 创建自定义按钮.

### range 控件

**主要问题**

- 设置其拖拽把手样式异常困难.

**解决方法**

- 建议不学习.

## 伪类

**机制**

- 通过伪类,
- 确定控件不同状态,
- 进而修饰控件.

**常用伪类**

- :required 和 :optional;
- :before 和 :after;
- :valid 和 invalid;
- :in-range 和 :out-of-range;
- :enable 和 disabled;
- :read-only 和 :read-write;
- :default, :checked 和 :indeterminate.

### :\required 和 :\optional

**相关属性**

- required.

**作用**

- :required;
  - 设置具有 required 属性的 \<input\>, \<select\> 和 \<textarea\> 标签样式.
- :optional.
  - 设置没有 required 属性的 \<input\>, \<select\> 和 \<textarea\> 标签样式.

**语法格式**

```css
/* Selects any required <input> */
input:required {
  border: 1px dashed red;
}

/* Selects any optional <input> */
input:optional {
  border: 1px dashed black;
}
```

### :\before 和 :\after

**generated content**

- 添加至控件上的文本内容.

**添加方法**

- 通过 :before 和 :after 添加.

#### \<input\> 控件

**主要问题**

- \<input\> 类似于替换元素,
- 无法直接添加 generated content.

**解决方法**

- 紧跟 \<input\> 标签,
- 创建一个空标签 \<span\>,
- 对 \<span\> 使用 :before 和 :after 间接添加.

**\<span\> 问题**

- \<span\> 为块级标签,
- 从而导致换行.

**解决方法**

- 容器使用 flex 布局,
- 设置 `flex-flow: row wrap;`.

**示例**

```html
<div>
  <label for="fname">First name: </label>
  <input id="fname" name="fname" type="text" required />
  <span></span>
</div>
```

```css
div {
  display: flex;
  flex-flow: row wrap;
}

input + span {
  position: relative;
}

input:required + span::after {
  position: absolute;
  top: -26px;
  left: -70px;
  content: "required";
}
```

### 控件数据有效性

**相关属性**

- required;
- pattern;
- min/max.

#### :\valid 和 :\invalid

**作用**

- 根据控件数据有效性设置样式.

**判断原则**

- 无任何验证约束的控件, 值永远有效;
- 具有 required 属性的控件;
  - 若没有值
  - 无效.
- 具有约束验证的控件, 根据其 pattern 判断;
- 具有 min/max 属性的控件,
  - 其值超出对应范围,
  - 无效.

**应用场景**

- 仅仅改变不同状态下控件样式;
- 根据不同状态添加对应 generated content.

**示例**

```html
<div>
  <label for="fname">First name *: </label>
  <input id="fname" name="fname" type="text" required />
  <span></span>
</div>
```

```css
input + span {
  position: relative;
}

input + span::before {
  position: absolute;
  right: -20px;
  top: 5px;
}

input:invalid {
  border: 2px solid red;
}

input:invalid + span::before {
  content: "✖";
  color: red;
}

input:valid + span::before {
  content: "✓";
  color: green;
}
```

#### :\in-range 和 :\out-of-range

**作用**

- 同 :valid 和 invalid.

**应用场景**

- 同 :valid 和 invalid.

**注意问题**

- 当同时使用 :valid/:invalid 和 :in-range/:out-of-range,
- 注意其 css 定义顺序,
- 根据 cascade 规则,
- 最终应用靠后的 css rule.

### 控件生效和读写模式

#### :\enable 和 :\disabled

**作用**

- 根据控件是否生效设置样式.

**相关属性**

- disable.

**应用场景**

- 用于故意阻止用户提交数据.
  - 提交无用数据;
  - 提交重复数据.

#### :\read-only 和 :\read-write

**作用**

- 根据控件读写模式设置样式.

**相关属性**

- readonly.

**应用场景**

- 用于只能查看, 无法编辑的场景.
  - 检查表单内容是否正确.

### Radio 和 checkbox

**相关伪类**

- :default;
- :checked;
- :indeterminate.

**相关属性**

- checked;
- indeterminate.

**作用**

- 根据 radio 和 checkbox 三种状态设置样式.
