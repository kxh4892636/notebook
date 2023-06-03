---
id: f2294775-4e3e-4189-8fc5-0b873382c6f9
---

# node 项目配置

## node 项目工具

### ts_node

**安装**

```bash
npm install --save-dev ts-node
```

**作用**

- 直接运行 ts 文件;

**语法格式**

```bash
npx ts-node test.ts
```

### nodemon

**安装**

```bash
npm install --save-dev nodemon
```

**作用**

- 监视 node.js 应用程序中的任何更改并自动重启服务;

**语法格式**

```package.json
{
  "scripts": {
    "start": "nodemon src/index.ts"
  }
}
```

### pm2

**安装**

```bash
npm install --save-dev nodemon
```

**作用**

- 基于 Nodejs 的进程管理器;
- 包括守护进程, 监控, 日志的一整套完整的功能;

**常用命令**

```bash
# 显示所有进程
pm2 list
# 启动 node 应用
pm2 start app.js
# 停止 node 应用
pm2 stop app.js/id
# 删除 node 应用
pm2 delete app.js/id
# 停止所有 node 应用
pm2 stop all
# 删除所有 node 应用
pm2 delete all
# 重启 node 应用
pm2 restart app.js/id
# 重载 node 应用
pm2 reload app.js/id
# 重启所有 node 应用
pm2 restart all
# 重载所有 node 应用
pm2 reload all
# 显示 id 为 0 的进程日志
pm2 logs 0
# 显示所有进程日志
pm2 logs
# 清空日志
pm2 flush
# 重载所有日志
pm2 reloadLogs
```

## ESM 项目配置

**package.json**

```json
// type 设置为 module
// scripts 命令中使用 --experimental-specifier-resolution=node, 省略引入语法中的后缀
{
  "name": "server",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "dependencies": {
    //...
  },
  "devDependencies": {
    // ...
  },
  "scripts": {
    "start": "node dist/index.js --node-args=--experimental-specifier-resolution=node",
    "start:prod": "pm2 start dist/index.js --node-args=--experimental-specifier-resolution=node"
  }
}
```

**tsconfig**

```json
{
  // target 使用 ES6 及更高版本
  // model 使用 ES6 及更高版本推荐使用 ESNext
  // moduleResolution 使用 node
  // ts-node 分别为使用 esm 和 experimentalSpecifierResolution
  "compilerOptions": {
    "target": "ES6",
    "module": "ESNext",
    "moduleResolution": "node",
    "outDir": "dist",
    "allowJs": true,
    "esModuleInterop": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true
  },
  "ts-node": {
    "esm": true,
    "experimentalSpecifierResolution": "node"
  }
}
```
