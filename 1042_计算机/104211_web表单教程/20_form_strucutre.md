# 表单布局

## \<label\> 标签

**作用**

- 设置说明文字.

**语法格式**

```html
<label for="cheese">Do you like cheese?</label> <label>Click me <input type="text" /></label>
```

**可访问性**

- 关键标签,
- \<label\> 标签与表单控件推荐一一对应.

### 关联机制

**关联方法**

- 使用 for 属性关联 \<input\> id 属性,
- \<input\> 标签嵌套于 \<label\> 标签中.

**机制**

- 点击 \<label\> 标签,
- 同时作用于关联的表单控件.

### Multiple labels

**语法格式**

```html
<div>
  <label for="username">Name:</label>
  <input id="username" type="text" name="username">
  <label for="username"><span aria-label="required">*</abbr></label>
</div>
```

**是否推荐**

- 可以使用, 但不建议,
- 可访问性较差,
- 若必须,
- 将多个 \<label\> 标签合并成一个.

```html
<div>
  <label for="username">Name: <span aria-label="required">*</span></label>
  <input id="username" type="text" name="username" />
</div>
```

### 属性

**for**

- 其属性值为关联控件的 id 属性值,
- 表示与其关联,
- id 值唯一,
- 推荐总是使用.

## \<output\> 标签

**作用**

- 显示多个关联控件的计算结果;
- 显示关联控件值.
  - \<range\> 标签.

**语法格式**

```html
<form oninput="result.value=parseInt(a.value)+parseInt(b.value)">
  <input type="range" id="b" name="b" value="50" /> +
  <input type="number" id="a" name="a" value="10" /> =
  <output name="result" for="a b">60</output>
</form>
```

**关联机制**

- 使用 for 属性关联 \<input\> id 属性.

### 属性

**for**

- 其属性值为关联控件的 id 属性值,
- 表示与其关联,
- id 值可为多个,
- 空格间隔,
- 推荐总是使用.

## \<textarea\> 标签

**作用**

- 多行文本控件,
- 显示文本,
- 可调整大小.

**示意图**

<textarea name="textarea" rows="10" cols="50">Write something here</textarea>

**语法格式**

- 默认值放置于 opening 和 closing tags 之间.

```html
<textarea name="textarea" rows="10" cols="50">Write something here</textarea>
```

**resize 属性**

- 通过 css 中的 resize 属性,
- 控制其是否可以调整大小.

### 属性

**cols**

- 设置一行可见字符数量,
- 正整数,
- 默认为 20,
- 可通过拉伸修改.

**rows**

- 设置一次性显示的行数,
- 正整数,
- 默认为 2,
- 可通过拉伸修改.

**wrap**

- soft;
  - 默认值;
  - 浏览器渲染换行,
  - 服务器提交不换行.
- hard: 浏览器渲染和服务器都换行.
- off: 浏览器渲染和服务器都不换行.

**required**

- 用于 \<input\>, \<select\> 和 \<textarea\>,
- 布尔属性,
- 表明提交表单之前,
- 需要填充一个值.

## \<fieldset\> 标签和 \<legend\> 标签

### \<fieldset\> 标签

**作用**

- 语义标签;
- 将具有相同作用的控件组合.

**语法格式**

```html
<form>
  <fieldset>
    <legend>Fruit juice size</legend>
    <p>
      <input type="radio" name="size" id="size_1" value="small" />
      <label for="size_1">Small</label>
    </p>
    <p>
      <input type="radio" name="size" id="size_2" value="medium" />
      <label for="size_2">Medium</label>
    </p>
    <p>
      <input type="radio" name="size" id="size_3" value="large" />
      <label for="size_3">Large</label>
    </p>
  </fieldset>
</form>
```

**用法**

- 多个 radio 通常嵌套于 \<fieldset\> 标签中.

**可访问性**

- 关键标签.

### \<legend\> 标签

**作用**

- 声明 \<fieldset\> 标签中所有控件的作用.

**语法格式**

- 嵌套于 \<fieldset\> 标签.

```html
<form>
  <fieldset>
    <legend>Fruit juice size</legend>
    ...
  </fieldset>
</form>
```

## 布局技巧

- 使用 \<hx\> 和 \<p\> 标签组织整个表单结构;
- 使用 \<section\> 标签分隔表单不同部分;
- 使用 \<fieldset\> 标签和使用 \<legend\> 标签组合相同作用控件;
- 使用 \<p\> 标签分隔单独控件;
- \<label\> 标签和表单控件一一对应;
- 使用 \<li\> 标签组织同一组表单控件;

```html
<form>
  <h1>Payment form</h1>
  <p>
    Required fields are followed by
    <strong><span aria-label="required">*</span></strong
    >.
  </p>
  <section>
    <h2>Contact information</h2>
    <fieldset>
      <legend>Title</legend>
      <ul>
        <li>
          <label for="title_1">
            <input type="radio" id="title_1" name="title" value="K" />
            King
          </label>
        </li>
        <li>
          <label for="title_2">
            <input type="radio" id="title_2" name="title" value="Q" />
            Queen
          </label>
        </li>
        <li>
          <label for="title_3">
            <input type="radio" id="title_3" name="title" value="J" />
            Joker
          </label>
        </li>
      </ul>
    </fieldset>
    <p>
      <label for="name">
        <span>Name: </span>
        <strong><span aria-label="required">*</span></strong>
      </label>
      <input type="text" id="name" name="username" />
    </p>
    <p>
      <label for="mail">
        <span>E-mail: </span>
        <strong><span aria-label="required">*</span></strong>
      </label>
      <input type="email" id="mail" name="usermail" />
    </p>
    <p>
      <label for="pwd">
        <span>Password: </span>
        <strong><span aria-label="required">*</span></strong>
      </label>
      <input type="password" id="pwd" name="password" />
    </p>
  </section>
  <section>
    <p>
      <button type="submit">Validate the payment</button>
    </p>
  </section>
</form>
```
