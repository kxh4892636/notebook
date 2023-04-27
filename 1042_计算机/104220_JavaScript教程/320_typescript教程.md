---
id: 7e7b3f2c-6098-446c-9789-d3e47c800b80
---

# typescript 教程

## 数据类型

### 原始数据类型

**语法格式**

```typescript
// 布尔值
const isDone: boolean = false;
// 数值
const num: number = 1;
// 字符串
const myName: string = "Tom";
// 表示函数返回空
const alertName = (): void => {
  console.log("My name is Tom");
};
// undefined 表示变量没有值得初始状态;
// undefined 是任何类型的子类型
const u: undefined = undefined;
let num: number = undefined;
// 表示什么都没有
const n: null = null;
```

### 任意类型

**any**

```typescript
// 表示可以赋予任何类型, 可以使用任何类型的属性和方法
let anyThing: any = "Tom";
```

**未声明的变量**

- 若一个变量声明时未指定其类型;
- 将其视为 any;

### 联合类型

**语法格式**

```typescript
let myFavoriteNumber: string | number;
myFavoriteNumber = "seven";
myFavoriteNumber = 7;
```

**访问联合类型的方法和属性**

- 只能访问联合类型共有的方法和属性;

### 接口

**定义接口**

```typescript
interface Person {
  name: string;
  age: number;
}
```

**可选属性**

```typescript
interface Person {
  name: string;
  age?: number;
}
```

**任意属性**

```typescript
// 确定任意属性后, 确定属性和可选属性必须为任意属性的子类型
interface Person {
  name: string;
  age?: number;
  [propName: string]: string | number;
}
```

**只读属性**

```typescript
interface Person {
  readonly id: number;
  name: string;
  age?: number;
  [propName: string]: any;
}
```

**接口继承接口**

```typescript
interface Alarm {
  console.log(): void;
}
interface LightableAlarm extends Alarm {
  lightOn(): void;
  lightOff(): void;
}
```

### 数组类型

**语法格式**

```typescript
// 类型 + 方括号
let fibonacci: number[] = [1, 1, 2, 3, 5];
let fibonacci: object[] = [1, 1, 2, 3, 5];
// 泛型
let fibonacci: Array<number> = [1, 1, 2, 3, 5];
// 接口
interface NumberArray {
  [index: number]: number;
}
let fibonacci: NumberArray = [1, 1, 2, 3, 5];
```

### 函数类型

**语法格式**

```typescript
function (x: number, y: number): number {
    return x + y;
};
const sum = (x: number, y: number): number => {
  return x + y;
};
```

**可选类型**

```typescript
// 可选参数位于必选参数后
const buildName = (firstName: string, lastName?: string) => {
  // ...
};
```

**函数默认值**

```typescript
const buildName = (firstName: string, lastName: string = "kong") => {
  // ...
};
```

**任意数量参数**

```typescript
// 必须位于最后
const push = (array: any[], ...items: any[]) => {
  //...
};
```

**函数重载**

```typescript
// 一个函数接受不同数量或类型的参数
// 进行不同的处理
function reverse(x: number): number;
function reverse(x: string): string;
function reverse(x: number | string): number | string | void {
  if (typeof x === "number") {
    return Number(x.toString().split("").reverse().join(""));
  } else if (typeof x === "string") {
    return x.split("").reverse().join("");
  }
}
```

### 内置对象类型

**ECMAScript**

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)

### 字面量类型

**语法格式**

```typescript
// 约束取值只能为规定值中的一个;
type EventNames = "click" | "scroll" | "mousemove";
const handleEvent = (ele: Element, event: EventNames) => {
  // do something
};
handleEvent(document.getElementById("hello"), "scroll"); // 没问题
handleEvent(document.getElementById("world"), "dblclick"); // 报错，event 不能为 'dblclick'
```

### 元组

**语法格式**

```typescript
// 元组各项类型不同且固定
// 初始化元组需要赋值所有项
const tom: [string, number] = ["Tom", 25];
```

**越界元素**

- 类型限制为元组中各类型的联合类型;

### 枚举

**语法格式**

```typescript
// enum 用于取值限制在一定范围内的场景
// enum 成员赋值为从 0 递增的数字, 枚举值和枚举名相互映射
enum Directions {
  Up,
  Down,
  Left,
  Right,
}
```

**手动赋值**

```typescript
// 未手动赋值的根据上一个枚举项递增
// 该例中 Up 和 Left 均为 3, 但 ts 并不报错, 最好不要出现该情况
enum Directions {
  Up = 3,
  Down = 2,
  Left,
  Right,
}
```

**常数枚举**

```typescript
// 不能使用计算成员, 编译时删除
const enum Directions {
  Up,
  Down,
  Left,
  Right,
}
let directions = [Directions.Up, Directions.Down, Directions.Left, Directions.Right];
// 编译结果
var directions = [0 /* Up */, 1 /* Down */, 2 /* Left */, 3 /* Right */];
```

**外部枚举**

```typescript
// 编译结果中会被删除
declare enum Directions {
  Up,
  Down,
  Left,
  Right,
}
```

**同时使用常数枚举和外部枚举**

```typescript
declare const enum Directions {
  Up,
  Down,
  Left,
  Right,
}

let directions = [Directions.Up, Directions.Down, Directions.Left, Directions.Right];
```

### 类型断言

**语法格式**

```typescript
const tom = getCacheData("tom") as Cat;
```

**使用场景**

- 明确联合类型中的一个类型;
- 将任何类型断言为 any;
- 将 any 断言成具体类型;

**双重断言**

```typescript
// 使用双重断言可以将任意类型断言为另一任意类型
// 建议不要使用
A as any as B;
```

## 类

### 基本概念

**访问修饰符**

```typescript
// public 公有, 任何地方均可访问
// private 私有, 仅能从声明类内部访问
// protected 保护, 仅能从声明类极其子类内部访问
class Animal {
  private name;
  public constructor(name) {
    this.name = name;
  }
}
```

**readonly**

```typescript
// 只读修饰符
// 与其他访问修饰符共存时, 放在其后
class Animal {
  // public readonly name;
  public constructor(public readonly name) {
    // this.name = name;
  }
}
```

**abstract**

```typescript
// 定义抽象类及其抽象方法
// 抽象类和方法不能被实例化
abstract class Animal {
  public name;
  public constructor(name) {
    this.name = name;
  }
  public abstract sayHi();
}
```

**使用类**

```typescript
class Animal {
  // ...
}
let a: Animal = new Animal("Jack");
```

### 类和接口

**类实现接口**

```typescript
interface Alarm {
  console.log(): void;
}
interface Light {
  lightOn(): void;
  lightOff(): void;
}
class Car implements Alarm, Light {
  console.log() {
    console.log("Car alert");
  }
  lightOn() {
    console.log("Car light on");
  }
  lightOff() {
    console.log("Car light off");
  }
}
```

**类继承接口**

```typescript
// 声明类的同时声明了一个同名类型
// 创建的同名类型中只包含类的实例属性和方法
class Point {
  x: number;
  y: number;
  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }
}
interface Point3d extends Point {
  z: number;
}
let point3d: Point3d = { x: 1, y: 2, z: 3 };
```

## 泛型

### 基本概念

**泛型**

- 定义函数, 接口或类时;
- 不确定具体类型;
- 在使用时确定;

**语法格式**

```typescript
// 定义泛型
const createArray = <T>(length: number, value: T): Array<T> => {
  let result: T[] = [];
  for (let i = 0; i < length; i++) {
    result[i] = value;
  }
  return result;
};
// 确定类型
createArray<string>(3, "x"); // ['x', 'x', 'x']
```

**多个类型参数**

```typescript
const swap = <T, U>(tuple: [T, U]): [U, T] => {
  return [tuple[1], tuple[0]];
};
```

**泛型参数的默认类型**

```typescript
// 没有指定类型且 ts 也无法推断类型时, 使用默认类型
const createArray = <T = string>(length: number, value: T): Array<T> => {
  let result: T[] = [];
  for (let i = 0; i < length; i++) {
    result[i] = value;
  }
  return result;
};
```

### 泛型约束

- 函数内部使用泛型时,
- 由于不清楚其类型;
- 无法使用类型的属性和方法;
- 使用泛型约束指定其包含的属性和方法;

```typescript
interface Lengthwise {
  length: number;
}
const loggingIdentity = <T extends Lengthwise>(arg: T): T => {
  console.log(arg.length);
  return arg;
};
```

### 泛型接口

```typescript
// 通过定义泛型接口定义函数形状
interface CreateArrayFunc {
  <T>(length: number, value: T): Array<T>;
}

const createArray: CreateArrayFunc = <T>(length: number, value: T): Array<T> => {
  let result: T[] = [];
  for (let i = 0; i < length; i++) {
    result[i] = value;
  }
  return result;
};
```

### 泛型类

```typescript
class GenericNumber<T> {
  zeroValue: T;
  add: (x: T, y: T) => T;
}
let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = function (x, y) {
  return x + y;
};
```

## 操作符

```typescript
// 非空断言操作符 !
map!; // 表示 map 一定有值
// 可选链操作符 ?
map?.getLayer(); // 表示 map 为可选项, map 非空时才会执行 getLayer() 函数, 为空时返回 undefined
// 空值合并运算符 ??
const foo = null ?? "default string"; // 当左侧操作数为 null 或 undefined 时, 返回右侧操作数，反之返回左侧操作数
```

## 声明文件

### 基本概念

**声明文件**

- 用于声明第三方库类型, 变量, 方法等...

**后缀名**

- .d.ts 为后缀;

### 自定义类型

```typescript
export type CaseListData = {
  key: string;
  title: string;
  data: string[];
};
```

## ts 常见类型

### JavaScript

```typescript
// setInterval() 函数返回 NodeJS.Timer 类型
const intervalFunc: NodeJS.Timer = setInterval();
```

### html

```typescript
// div 标签
const mapContainerRef = useRef<HTMLDivElement>(document.createElement("div"));
```

### mapbox

- mapboxgl.map: map 对象;

```typescript
// map 对象
map: mapboxgl.Map | undefined;
// image 类型的 Source
import { ImageSource } from "mapbox-gl";
map!.getSource(id) as ImageSource).updateImage({ url: url }
```

### express

```typescript
// req 和 res 类型
import { Request, Response } from "express";
const getList = async (req: Request, res: Response) => {
  // ...
};
```

## 进阶

### type 和 interface 的区别

**不知道使用什么**

- 两者都可以实现;
- 但不知道使用 type 或 interface;
- 就使用 type;

**约束或继承**

- 如果要对函数或类进行泛型约束;
- 或者需要被继承;
- 使用 interface;

**type 和 interface**

- type 只是一个类型别名, 并不实际存在;
- interface 是实际存在的;
