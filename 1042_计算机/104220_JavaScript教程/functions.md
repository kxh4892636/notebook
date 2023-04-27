# FUNCTIONS

**function**

- 函数在 js 中实质是一个 object,
- 是 Function 类型的实例;
- 具有自己的属性和方法.

**定义函数**

```typescript
function sum(num1, num2) {
  return num1 + num2;
}
// function Expressions
let sum = function (num1, num2) {
  return num1 + num2;
};
// arrow function
let sum = (num1, num2) => {
  return num1 + num2;
};
```

## Arrow Functions

**定义箭头函数**

- 箭头函数形式和函数表达式形式等效.

```typescript
// arrow function
let arrowSum = (a, b) => {
  return a + b;
};
// function Expressions
let functionExpressionSum = function (a, b) {
  return a + b;
};
```

**prototype**

- 箭头函数定义的函数没有 prototype 属性.

**省略 {}**

- arrow function 可省略花括号,
- 但函数限制一行代码,
- 默认返回该行代码的值.

```typescript
// Both are valid and will return the value
let double = (x) => {
  return 2 * x;
};
let triple = (x) => 3 * x;
```

## Function names

**函数名的实质**

- 函数名是指向 function 的一个指针.

```typescript
function sum(num1, num2) {
  return num1 + num2;
}
console.log(sum(10, 10)); // 20
let anotherSum = sum;
console.log(anotherSum(10, 10)); // 20
sum = null;
console.log(anotherSum(10, 10)); // 20
```

**name 属性**

- 函数名通过一个只读的 name 属性定义,
- 一般 name 属性为其标识符名称,
- 当函数为命名时,
  - name 属性值为空.
- 当使用用 function constructor 定义函数时,
  - name 属性值为 anonymous.
- 当函数为 get/set 或者是 bind() 的一个实例时,
  - name 属性值添加对应前缀.

```typescript
function foo() {}
console.log(foo.bind(null).name); // bound foo
let dog = {
  years: 1,
  get age() {
    return this.years;
  },
  set age(newAge) {
    this.years = newAge;
  },
};
let propertyDescriptor = Object.getOwnPropertyDescriptor(dog, "age");
console.log(propertyDescriptor.get.name); // get age
console.log(propertyDescriptor.set.name); // set age
```

## Understanding Arguments

**函数传递的实质**

- 函数传递时, 参数数量和类型不用于函数定义相一致,
- ECMAScript 将函数参数作为一个名为 arguments 的 arrayLike 传递,
- 但不关心 arguments 内部,
- arguments 的行为类似 Array,
  - 函数参数可通过 arguments[index] 访问.
- 但 arguments 并不是 Array 的实例,
- 任何函数定义中没有被传递的函数参数赋值 undefined.

**arguments 的 length 属性**

- 传递参数的数量.

```typescript
function howManyArgs() {
  console.log(arguments.length);
}
howManyArgs("string", 45); // 2
howManyArgs(); // 0
howManyArgs(12); // 1
```

**箭头函数中的函数参数**

- 箭头函数中的函数参数不能通过 arguments 访问,
- 只能使用其参数名称.

## no overloading

**overloading**

- js 不支持 overloading,
- 如果存在两个同名函数,
- 后一个函数覆盖前一个.

## Default Parameter Values

**定义函数默认值**

```typescript
function makeKing(name = "Henry") {
  return `King ${name} VIII`;
}
console.log(makeKing("Louis")); // 'King Louis VIII'
console.log(makeKing()); // 'King Henry VIII'
```

**传递 undefined**

- 当函数参数为 undefined 时,
- js 视其为没有传递函数参数.

**arguments**

- arguments 无视函数默认值,
- 对于没有传递的函数参数,
- 即使其有函数默认值,
- 依旧视其为 undefined.

**函数默认值**

- 函数默认值不限于 primitive type 或 reference type,
- 其可以是 object/function.

**函数默认值的作用域**

- 函数默认值等效于在函数内部顶端,
- 根据函数参数的位置顺序,
- 依次使用 let 定义.

## Spread Arguments and Rest Parameters

### Spread Arguments

**机制**

- 调用函数时,
- 使用 ... 操作符拓展数组表示一系列函数参数.

**语法格式**

```typescript
function getSum() {
  let sum = 0;
  for (let i = 0; i < arguments.length; ++i) {
    sum += arguments[i];
  }
  return sum;
}

let values = [1, 2, 3, 4];
console.log(getSum(...values)); // 10
```

**适用范围**

- 箭头函数;
- 普通函数.

### Rest Parameter

**机制**

- 定义函数时,
- 使用 ... 操作符表示任意数量的参数.

**语法格式**

- Rest Parameter 只能放置于最后.

```typescript
function getSum(...values) {
  return values.reduce((x, y) => x + y, 0);
}
console.log(getSum(1, 2, 3)); // 6
```

**适用范围**

- 箭头函数;
- 普通函数.

## Function Declarations versus Function Expressions

**函数提升**

- Function declarations;
  - 代码执行开始,
  - JavaScript engine 获取所有 Function declarations 并提升至顶部;
  - 在代码执行之前便可以读写;
- Function Expressions.
  - Function Expressions 无函数提升机制,
  - 只有代码执行后才能读写.

## Functions as Values

**机制**

- js 中函数和变量没有本质性区别,
- 函数本身可以作为函数参数和函数范围值.

```typescript
function callSomeFunction(someFunction, someArgument) {
  return someFunction(someArgument);
}
```

## Function Internals

### arguments

**callee 属性**

- 指向 arguments 对的函数.

**作用**

- 不使用函数名便可以访问函数;
- 防止一些因为函数名而导致的 bug, 如下列代码.

```typescript
function factorial(num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * arguments.callee(num - 1);
  }
}

let trueFactorial = factorial;
factorial = function () {
  return 0;
};
console.log(trueFactorial(5)); // 120
console.log(factorial(5)); // 0
```

### this

**普通函数**

- 指向函数被调用时所在作用域的 variable object.

**箭头函数**

- 指向箭头函数本身所在作用域的 variable object.

```typescript
// 普通函数
window.color = "red";
let o = {
  color: "blue",
};
function sayColor() {
  console.log(this.color);
}
sayColor(); // 'red'
o.sayColor = sayColor;
o.sayColor(); // 'blue
// 箭头函数
window.color = "red";
let o = {
  color: "blue",
};
let sayColor = () => console.log(this.color);
sayColor(); // 'red'
o.sayColor = sayColor;
o.sayColor(); // 'red
```

### caller

**caller**

- 指向该函数被调用时所在作用域的函数,
- 当函数在 global scope 被调用时为 null.

**strict mode**

- 在 strict mode 下,
- 该属性报错.

### new.target

**new.target**

- 判断函数是否被 new 调用.

```typescript
function King() {
if (!new.target) {
throw 'King must be instantiated using "new"'
}
console.log('King instantiated using "new"';
}
new King(); // King instantiated using "new"
King(); // Error: King must be instantiated using "new"
```

## Function Properties and Methods

**属性**

- length: 函数理想化的参数数量;
- prototype: 存储 function 的方法;
  - 不可枚举.

**方法**

- apply();
- call();
- bind();
- toString()

**Function.prototype.apply() 方法**

- Function.prototype.apply(thisArg[, argsArray]);
  - 调用 Function.
  - 返回值: Function 的返回值.

**Function.prototype.call() 方法**

- Function.prototype.call(thisArg[, arg1,..., argN]);
  - 调用 Function.
  - 返回值: Function 的返回值.

**Function.prototype.bind() 方法**

- Function.prototype.bind(thisArg[, arg1,..., argN]).
  - 创建一个 Function 的实例并调用;
  - 返回值: Function 的返回值.

**Function.prototype.toString() 方法**

- Function.prototype.toString();
  - 打印 Function 的代码;
  - 返回值: str.

**this 的力量**

```typescript
window.color = "red";
let o = {
  color: "blue",
};
function sayColor() {
  console.log(this.color);
}
sayColor(); // red
sayColor.call(this); // red
sayColor.call(window); // red
sayColor.call(o); // blue
```

## Function Expressions

**anonymous function**

- function expression 创建的函数又叫做 anonymous function,
- 因为其没有 name 属性.

**函数作为返回值**

- function expression 的使用能够便利地将某个函数作为另一个函数的返回值.

## Recursion

## Tail Call optimization

## Closures

## Immediately Invoked Function Expressions

## Private Variables
