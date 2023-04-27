---
id: d501f11a-92c3-4d85-92ed-1c500c5c713b
---

# hook

## hook

**hook**

- react 中的特殊函数;
- 以 use 为前缀.

**使用原则**

- hook 只能定义在组件或 hook 的开头;
- 不能定义在条件语句, 循环语句或函数内.

## hook 使用误区

**useEffect 的依赖**

- 不是所有的依赖都必须放到依赖数组中;
- 只有当某变量发生变化, 需要触发 useEffect 时, 将其放入依赖数组中;

**useEffect 的闭包问题**

- 在使用 setTimeout, setInterval, Promise.then 的场景下, 即延迟调用;
- 一定会存在闭包问题;
- 解决方式见 [[900_react最佳实践#闭包问题]];

**useMemo**

```typescript
// 不要滥用 useMemo
// 考虑计算和比较变化的收益
const c = useMemo(() => a + b, [a, b]);
```

**useCallback**

```typescript
// 尽量少的使用 useCallback
// 只有组件被 memo 包裹, 且组件每个属性都使用 useCallback, useCallback 才会生效
const func = useCallback(() => {
  doSomething();
}, []);
const ExpensiveComponent = React.memo(({ func }) => {
  return <div onClick={func}>hello</div>;
});
```

## hook 思想

**返回逻辑函数**

```typescript
const useKeys = () =>  {
  function getAllKeys(data) {
    ...
  }
  function getLayerKeys(data) {
    ...
  }
  function getGroupKeys(data) {
    ...
  }
  return{getAllKeys, getLayerKeys, getGroupKeys}
}
```

## 疑难杂症

### hook 的限制

**相互调用**

- hook 无法相互调用, 否则报错;
  - 即两个 hook A 和 B;
  - 不能 A 中调用 B, B 中有调用 A;

### hook 函数返回值的坑

```typescript
type Action = "all" | "layer" | "group";
// 当 hook 使用 if 或 Switch 返回不同函数时
// ts 无法正常识别返回函数的参数类型
// 如下例, ts 认为返回函数必定有 layer 和 group 两个参数, 导致 getAllKeys 和 getLayerKeys 无法使用, 原因不详
// 如果想要解决, 需要将 layer 和 group 设置为可选参数
// 推荐返回包含三个函数的对象
const useKeys = (type: Action) => {
  function getAllKeys() {
    // ...
  }
  function getLayerKeys(layer: Layer) {
    // ...
  }
  function getGroupKeys(layer: Layer, group: boolean) {
    // ...
  }
  if (type === "all") return getAllKeys;
  else if (type === "layer") return getLayerKeys;
  else return getGroupKeys;
};
```
