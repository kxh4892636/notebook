# \<input\> 标签

**作用**

- 为表单创建交互式控件.

**语法格式**

```html
<label for="name">Name:</label> <input type="text" id="name" name="name" required size="10" />
```

## 属性

**type**

- 定义 \<input\> 标签样式和行为,
- 默认值为 text,
- 推荐总是使用.

**required**

- 用于 \<input\>, \<select\> 和 \<textarea\>,
- 布尔属性,
- 表明提交表单之前,
- 需要填充一个值.

## 文本控件

**示意图**

<input type="text" id="comment" name="comment" value="I'm a text field" />

### 通用属性值

**placeholder**

- 简要描述 \<input\> 输入信息的类型,
- 最好是一个示例.

**size**

- 设置显示文本内容数量.

**maxlength**

- 设置控件输入内容最大字符数.

**minlength**

- 设置控件输入内容最小字符数.

**pattern**

- 自定义输入数据格式.

### text 属性值

**作用**

- 单行文本.

**语法格式**

```html
<input type="text" id="comment" name="comment" value="I'm a text field" />
```

**换行符机制**

- 如果输入文本具有换行符,
- 发送至服务器时,
- 自动删除.

### password 属性值

**作用**

- 密码形式.

**语法格式**

```html
<input type="password" id="pwd" name="pwd" />
```

**机制**

- 用户输入值会隐藏,
- 但是仅是表面,
- 如果不采取安全措施,
- 依旧以明文发送数据,
- 故建议使用 https:// 地址 以保护.

### hidden 属性值

**作用**

- 隐藏文本形式.

**语法格式**

```html
<input type="hidden" id="timestamp" name="timestamp" value="1286705410" />
```

**机制**

- 用户不可见,
- 但实际存在,
- 需要定义 name 和 value 属性.

### email 属性值

**作用**

- 限制输入数据格式为有效的邮箱地址.

**语法格式**

```html
<input type="email" id="email" name="email" />
```

#### 属性值

**multiple**

- 布尔属性,
- 设置一次输入多个邮箱地址,
- , 分隔.

### search 属性值

**作用**

- 创建搜索栏.

**语法格式**

```html
<input type="search" id="search" name="search" />
```

**与 text 的区别**

- 搜索框渲染成圆角样式,
- 有时会显示 ✖ 清除.

### tel 属性值

**作用**

- 限制输入数据格式为有效的电话号码.

**语法格式**

```html
<input type="tel" id="tel" name="tel" />
```

### url 属性值

**作用**

- 限制输入数据格式为有效的 URLs .

**语法格式**

```html
<input type="url" id="url" name="url" />
```

## 数字控件

### 通用属性

**min**

- 设置允许最小值.

**max**

- 设置允许最大值.

**step**

- int;
  - 数字变化值,
  - 默认变化值为 1,
  - 默认仅对 int 生效.
- any.
  - 暗示无指定 step,
  - 对 float 有效.

### number 属性值

**作用**

- 限制输入数据格式为有效的 Number .

**语法格式**

```html
<input type="number" name="age" id="age" min="1" max="10" step="2" value="1" />
```

**示意图**

<input type="number" name="age" id="age" min="1" max="10" step="2" value="1"/>

**机制**

- 提供了一个微调按钮,
- 且移动设备显示数字键盘.

**数字范围**

- 输入数字范围有限时;
- 若数字范围太大, 以至于微调按钮无用,
- 使用 tel 属性值更为合适.

### range 属性值

**作用**

- 创建一个滑动器选择数字.

**示意图**

<input
  type="range"
  name="price"
  id="price"
  min="50000"
  max="500000"
  step="100"
  value="250000"
/>
<output class="price-output" for="price">视觉反馈</output>

**语法格式**

```html
<input type="range" name="price" id="price" min="50000" max="500000" step="100" value="250000" />
<output class="price-output" for="price"></output>
```

**问题**

- 无法提供当前值的视觉反馈,
- 往往使用 \<output\> 标签用于显示当前值.

## 可选控件

### checkbox 属性值

**作用**

- 复选框形式.

**示意图**

<input type="checkbox" id="questionOne" name="subscribe" value="yes" checked />

**语法格式**

```html
<input type="checkbox" id="questionOne" name="subscribe" value="yes" checked />
```

**机制**

- 具有相同 name 属性值的选项视为同一组,
- 只有选中选中的 value 被发送,
- 如果选中项没有值,
- 发送 on,
- 若无选中项,
- 控件视为未知状态,
- 不发送任何值.

**风格规范**

- 包裹在 \<li\> 标签中;
- 使用 \<fieldset\> 和 \<legend\> 标签;
- \<label\> 标签一一对应.

```html
<fieldset>
  <legend>Choose all the vegetables you like to eat</legend>
  <ul>
    <li>
      <label for="carrots">Carrots</label>
      <input type="checkbox" id="carrots" name="vegetable" value="carrots" checked />
    </li>
    <li>
      <label for="peas">Peas</label>
      <input type="checkbox" id="peas" name="vegetable" value="peas" />
    </li>
    <li>
      <label for="cabbage">Cabbage</label>
      <input type="checkbox" id="cabbage" name="vegetable" value="cabbage" />
    </li>
  </ul>
</fieldset>
```

**checked 属性**

- 布尔属性,
- 决定复选框是否默认选中.

### radio 属性值

**作用**

- 单选框形式.

**示意图**

<input type="radio" id="soup" name="meal" value="soup"/>

**语法格式**

```html
<input type="radio" id="soup" name="meal" value="soup" checked />
```

**机制**

- 在 checkbox 控件基础之上,
- 除非重置表单,
- 一旦选中项,
- 就无法消除.

**风格规范**

- 同 checkbook 控件.

**属性**

- 同 checkbox 控件.

## 时间控件

**时间属性值**

- 同 \<time\> 标签.

### 通用属性

**min**

- 设置允许最小值.

**max**

- 设置允许最大值.

**step**

- 日期变化值,
- 默认值为日期对应单位.

### datetime-local 属性值

**作用**

- 显示和选择本地时间.

**示意图**

<input
  type="datetime-local"
  id="meeting-time"
  name="meeting-time"
  value="2018-06-12T19:30"
  min="2018-06-07T00:00"
  max="2018-06-14T00:00"
/>

**语法格式**

```html
<input
  type="datetime-local"
  id="meeting-time"
  name="meeting-time"
  value="2018-06-12T19:30"
  min="2018-06-07T00:00"
  max="2018-06-14T00:00"
/>
```

### month 属性值

**作用**

- 显示和选择年-月.

**示意图**

<input type="month" id="start" name="start" min="2018-03" value="2018-05" />

**语法格式**

```html
<input type="month" id="start" name="start" min="2018-03" value="2018-05" />
```

### time 属性值

**作用**

- 显示和选择时-分.

**示意图**

<input type="time" id="appt" name="appt" min="09:00" max="18:00" required />

**语法格式**

```html
<input type="time" id="appt" name="appt" min="09:00" max="18:00" required />
```

### week 属性值

**作用**

- 显示和选择年-周.

**示意图**

<input
  type="week"
  name="week"
  id="camp-week"
  min="2018-W18"
  max="2018-W26"
  required
/>

**语法格式**

```html
<input type="week" name="week" id="camp-week" min="2018-W18" max="2018-W26" required />
```

### date 属性值

**作用**

- 显示和选择年-月-日.

**示意图**

<input
  type="date"
  id="start"
  name="trip-start"
  value="2018-07-22"
  min="2018-01-01"
  max="2018-12-31"
/>

**语法格式**

```html
<input
  type="date"
  id="start"
  name="trip-start"
  value="2018-07-22"
  min="2018-01-01"
  max="2018-12-31"
/>
```

## 其他

### color 属性值

**作用**

- 提供一个颜色选择器控件.

**示意图**

<input type="color" name="color" id="color" />

**语法格式**

```html
<input type="color" name="color" id="color" />
```

**机制**

- 返回小写十六进制格式.

### image 属性值

**作用**

- 像 \<img\> 标签一样渲染按钮.

**示意图**

<input type="image" alt="Click me!" src="http://localhost:3000/src/image/open_gms.png" width="80" height="30" />

**语法格式**

```html
<input type="image" alt="Click me!" src="my-img.png" width="80" height="30" />
```

**机制**

- 若向服务器发送数据,
- 返回点击图像位置对应的 xy 坐标,
- 左上角为基准,
- 右下为正方向.

**访问 xy 坐标**

- x: name.x;
- y: name.y;

```html
<!-- get -->
http://foo.com?pos.x=123&pos.y=456
```

### file 属性值

**作用**

- 发送文件至服务器.

**示意图**

<input type="file" name="file" id="file" accept="image/*" multiple />

**语法格式**

```html
<input type="file" name="file" id="file" accept="image/*" multiple />
```

#### 属性值

**accept**

- 规定发送文件格式,
- 推荐总是使用.

**multiple**

- 布尔属性,
- 决定是否可以发送多个文件.

### 按钮控件

**作用**

- 按钮控件.

**示意图**

<input type="submit" value="This is a submit button" />

**语法格式**

```html
<input type="submit" value="This is a submit button" />
```

#### 属性值

**type**

- submit;
  - 默认值,
  - 根据 \<form\> 标签中的 action 属性发送数据;
- reset;
  - 重置所有表单控件为默认值,
  - 不推荐使用.
- button.
  - 什么也不会发生,
  - 用于基于 JavaScript,
  - 构建自定义按钮.
