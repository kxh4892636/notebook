# 字体

## 字体样式

### font-families 属性

**作用**

- 修改字体类型;

**语法格式**

```css
.serif {
  font-family: Times, "Times New Roman", Georgia, serif;
}

.sansserif {
  font-family: Verdana, Arial, Helvetica, sans-serif;
}

.monospace {
  font-family: "Lucida Console", Courier, monospace;
}
```

**字体栈机制**

- 读取第一个,
- 若不存在, 则读取第二个,
- 以此类推.

#### 属性值

**family-name**

- 具体字体名称.

**generic-name**

- 字体类型名称,
- values.
  - serif: 衬线;
  - sans-serif: 无衬线;
  - monospace: 等宽;
  - cursive: 手写体;
  - fantasy: 花字体.

**global value**

- 继承相关属性.

### 网络安全字体

**网络安全字体**

- 基本所有设备都支持的字体类型.

**常见字体**

- serif: Times New Roman;
- sans-serif: Arial;
- monospace: Courier New;

### color 属性

**作用**

- 修改字体颜色.

**语法格式**

```css
.serif {
  color: red.;
}
```

**属性值**

- 不作详述.

### font-size 属性

**作用**

- 修改字体大小.

**语法格式**

```css
.small {
  font-size: xx-small;
}
.larger {
  font-size: larger;
}
.point {
  font-size: 24pt;
}
.percent {
  font-size: 200%;
}
```

**属性值**

- 同 size 属性,
- 不作详述.

### font-style 属性

**作用**

- 修改字体样式.

**语法格式**

```css
.normal {
  font-style: normal;
}

.italic {
  font-style: italic;
}

.oblique {
  font-style: oblique;
}
```

#### 属性值

**normal**

- 默认样式;

**italic**

- 斜体.

**oblique**

- oblique 样式,
- 若无此样式, 则为 italic,
- 若无 italic,
- 人工模拟倾斜,
- 可加入可选参数 angle.

```css
.oblique {
  font-style: oblique 10deg;
}
```

### font-weight 属性

**作用**

- 修改字体粗细.

**语法格式**

```css
p {
  font-weight: bold;
}

div {
  font-weight: 600;
}

span {
  font-weight: lighter;
}
```

#### 属性值

**关键字属性值**

- normal: 对应 400;
- bold: 对应 700;
- lighter;
- bolder.

**数字**

- 100 - 900,
- 整百.

## 自定义字体

### 字体格式

**字体格式**

| 格式                   | MIME type  |
| ---------------------- | ---------- |
| TrueType               | font/ttf   |
| OpenType               | font/otf   |
| Web Open Font Format   | font/woff  |
| Web Open Font Format 2 | font/woff2 |

### @font-face

**作用**

- 添加自定义字体.

**语法格式**

- @font-face.
  - font-family;
  - src;
    - url;
    - format;
  - font-weight: 可选.
  - font-style: 可选.

```css
@font-face {
  font-family: "Open Sans";
  src: url("/fonts/OpenSans-Regular-webfont.woff2") format("woff2"), url("/fonts/OpenSans-Regular-webfont.woff")
      format("woff");
  font-weight: bold;
  font-style: normal;
}
```

**font-weight 和 font style 属性的应用场景**

- 同一字体, 多个文件, 多个样式;
- 不同字体, 多个文件, 同一样式.

```css
@font-face {
  font-family: "DroidSerif";
  src: url("DroidSerif-Regular-webfont.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "DroidSerif";
  src: url("DroidSerif-Italic-webfont.ttf") format("truetype");
  font-weight: normal;
  font-style: italic;
}
@font-face {
  font-family: "DroidSerif";
  src: url("DroidSerif-Bold-webfont.ttf") format("truetype");
  font-weight: bold;
  font-style: normal;
}
@font-face {
  font-family: "DroidSerif";
  src: url("DroidSerif-BoldItalic-webfont.ttf") format("truetype");
  font-weight: bold;
  font-style: italic;
}
```

```css
@font-face {
  font-family: "DroidSerifRegular";
  src: url("DroidSerif-Regular-webfont.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "DroidSerifItalic";
  src: url("DroidSerif-Italic-webfont.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "DroidSerifBold";
  src: url("DroidSerif-Bold-webfont.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "DroidSerifBoldItalic";
  src: url("DroidSerif-BoldItalic-webfont.ttf") format("truetype");
  font-weight: normal;
  font-style: normal;
}
```
