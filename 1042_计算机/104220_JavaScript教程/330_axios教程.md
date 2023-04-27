// NOTE axios

# axios 教程

## 环境配置

**安装**

```bash
npm install axios
```

## 请求配置

```typescript
axios.request({
  url: "/user", // URL 地址
  method: "get", // 默认 get, get + post
  baseURL: "https://some-domain.com/", // 若 url 为相对路径, 自动添加至 URL 前,
  headers: { "X-Requested-With": "XMLHttpRequest" }, // 设置 header
  params: {
    // 用于 get 请求, 即 req.query
    ID: 12345,
  },
  data: {
    // 用于 post 请求, 即 req.body
    firstName: "Fred",
  },
  timeout: 1000, // 设置请求时间
  responseType: "json", // 设置返回请求数据类型, 默认 json, json + blob + document
  responseEncoding: "utf8", // 设置返回请求编码, 默认 utf8
  proxy: {
    // 设置代理服务器
    host: "127.0.0.1",
    port: 9000,
    auth: {
      username: "kxh",
      password: "123456",
    },
  },
});
```

## 响应结构

```json
{
  // 服务器响应数据
  "data": {},
  // HTTP 状态码
  "status": 200,
  // HTTP 状态信息
  "statusText": "OK",
  // 服务器响应的头
  "headers": {},
  // 请求提供的配置信息
  "config": {},
  //
  "request": {}
}
```
