# nextjs 入门

## 基本概念

**next**

- react 框架;

**安装 next**

```bash
pnpm create next-app --experimental-app --typescript
```

## 开发环境和生产环境

**差异**

- 开发环境: next 考虑开发者体验;
- 生产环境: 优化代码性能;

**共同点**

- complied;
- bundled;
- minified;
- code split;

## 编译

**Compiling**

- 将一种语言转换至不同版本的同一种语言或另一种语言;

## 最小化

**Minifying**

- 在不影响代码功能的情况下;
- 除去代码中无异议的代码格式和注释;
- 减小代码文件体积;

## 捆绑

**Bundling**

- 解析项目中的依赖;
- 将其合成为少量文件;
- 减少网页请求;

## 代码分割

**Code Splitting**

- 分割 bundling 生成的 bundle.js 为多个 chunk.js;
- 减少网页加载时间;

## 构建时间和运行时

**build time**

- 将开发环境下的代码构建为生产环境下的代码;

**runtime**

- 代码在生产环境下运行的时间;

## 客户端和服务器

**client**

- 用户设备;

**server**

- 服务器;

## 渲染

**rendering**

- 将 react 转换为 html;

**分类**

- Server-Side Rendering;
- Static Site Generation;
- Client-Side Rendering;

**Pre-Rendering**

- Server-Side Rendering 和 Static Site Generation 称作 Pre-Rendering;
- 因为 rendering 过程发生在服务器;
- 将渲染结果发送至客户端;

**Client-Side Rendering**

- 浏览器接受 html 模板和 js 文件;
- 在客户端渲染为显示的 html;

**Server-Side Rendering**

- rendering 发生在服务器;

**Static Site Generation**

- rendering 发生在服务器;
- 无运行时;
- 所有内容在 build time 构建完毕;

## CDN 和 Edge

**CDN**

- 存储静态内容;
- 分布式存储系统;
- 独立于服务器和客户端;
- 减轻服务器或客户端的负担;

**Edge**

- 分布式存储系统;
- CDN 可看做 Edge 的一部分;
- 可运行部分代码;
- 减轻服务器或客户端的负担;
