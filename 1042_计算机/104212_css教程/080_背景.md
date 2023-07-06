# 颜色和背景

## background 属性

**作用**

- 设置背景样式.

**成分属性**

- background-attachment 属性;
- background-clip 属性;
- background-color 属性;
- background-image 属性;
- background-origin 属性;
- background-position 属性;
- background-repeat 属性;
- background-size 属性.

**简写机制**

- background-color 属性放置于最后;
- background-size 属性仅能放置于 background-position 属性之后, 通过 / 分隔;
- 其余成分属性位置随意.

### background-color 属性

**作用**

- 设置背景颜色.

**语法格式**

```css
.exampletwo {
  background-color: rgb(153, 102, 153);
  color: rgb(255, 255, 204);
}
```

#### 属性值

**关键字**

- currentcolor;
- transparent.

**其他属性值**

- 同 color 属性.

### background-image 属性

**作用**

- 设置背景图片.

**语法格式**

- url 引用图片,
- 多张背景图片 , 分隔.

```css
.catsandstars {
  background-image: url("startransparent.gif"), url("catfront.png");
  background-color: transparent;
}
```

**图片次序机制**

- 先定义的在前面;
- 依次叠加;

#### 属性值

**关键字**

- none;

**\<image\> 类型**

- 不作详述.

### background-repeat 属性

**作用**

- 背景图片重复排列.

**语法格式**

- 多张背景图片 , 分隔.

```css
.one {
  background-repeat: no-repeat;
}
.two {
  background-repeat: repeat;
}
.three {
  background-repeat: repeat space;
}
```

**多值语法**

- 1 value: 对应属性值;
- 2 value: 水平 + 竖直.

#### 属性值

**no-repeat**

- 不重复.

**repeat**

- 尽可能多的重复,
- 最后一幅图片可能会被裁剪,
- 但不会拉伸.

**repeat-x**

- 仅在 x 方向重复,
- 等同于 repeat no-repeat.

**repeat-y**

- 仅在 y 方向重复,
- 等同于 no-repeat repeat.

**space**

- 尽可能多的重复,
- 所有图片不会被裁减,
- 空余区域空白填补.

**round**

- 尽可能多的重复,
- 所有图片不会被裁减,
- 但所有图片会同步拉伸以填补空白区域.

### background-size 属性

**作用**

- 调整背景图片大小.

**语法格式**

- 多张背景图片 , 分隔.

```css
.tiledBackground {
  background-image: url(https://www.mozilla.org/media/img/logos/firefox/logo-quantum.9c5e96634f92.png);
  background-size: 150px;
  width: 300px;
  height: 300px;
}
```

**多值语法**

- 1 value;
  - 图片宽度, 高度为 auto;
- 2 value: width + height;

#### 属性值

**auto**

- 自动设置.

**contain**

- 保持纵横比,
- 填满整个容器,
- 尽可能拉伸放大,
- 若留下空白自动平铺,
- 可采用 no-repeat 防止.

**cover**

- 保持纵横比,
- 填满整个容器,
- 尽可能拉伸缩小,
- 多余部分裁剪.

**\<length\> 类型**

- 正数.

**\<percentage\> 类型**

- 正数.

### background-position 属性

**作用**

- 设置背景图片位置.

**语法格式**

- 多张背景图片 , 分隔.

```css
.examplethree {
  background-image: url("startransparent.gif"), url("catfront.png");
  background-position: 0px 0px, right 3em bottom 2em;
}
```

**默认值**

- left top.

**多值语法**

- 同 position 属性.

#### 属性值

**\<position\> 类型**

- 不作详述.

### background-attachment 属性

**作用**

- 设置背景图片相对于视图的位置.

**语法格式**

- 多张背景图片 , 分隔.

```css
p {
  background-image: url("starsolid.gif");
  background-attachment: fixed;
}
```

#### 属性值

**fixed**

- 相对于视图固定不动;

**local**

- 相对于元素内容固定不动;

**scroll**

- 相对于元素本身固定不动.

## colors 类型

### color 属性

**语法格式**

```css
p {
  color: red;
}
p {
  color: #f00;
}
p {
  color: #ff0000;
}
```

#### 属性值

**属性值**

- keyword;
- 十六进制值;
- rgb;
- rgba;
- hsl;
- hsla;

```css
/* keyword */
background-color: red;
/* 十六进制值 */
background-color: #ff0000;
/* rgb(a) */
background-color: rgb(255, 0, 0);
background-color: rgb(255, 0, 153, 1);
/* hsl(a) */
background-color: hsl(0, 100%, 50%);
background-color: hsl(0, 100%, 50%, 1);
```

### gradients 属性

**作用**

- 生成颜色渐变图象.

**语法格式**

```css
.radial-gradient {
  background: radial-gradient(red, yellow, rgb(30, 144, 255));
}

.radial-repeat {
  background: repeating-radial-gradient(powderblue, powderblue 8px, white 8px, white 16px);
}
```

#### [函数](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient#syntax)

- linear-gradient();
- radial-gradient();
- repeating-linear-gradient();
- repeating-radial-gradient();
- conic-gradient().
