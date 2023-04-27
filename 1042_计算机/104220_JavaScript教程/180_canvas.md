# Canvas

```typescript
if (isPosition) {
  const urlData = map?.getCanvas().toDataURL()!;
  let base = window.atob(urlData.substring(urlData.indexOf(",") + 1));
  let length = base.length;
  let url = new Uint8Array(length);
  while (length--) {
    url[length] = base.charCodeAt(length);
  }
  let file = new File([url], `logo.png`, {
    type: "image/png",
  });
  // NOTE 私有访问不到
  // 其余参数必须在前面?
  let param = new FormData();
  param.append("datasetID", "assets");
  param.append("file", file);
  result = await axios.request({
    url: serverHost + "/api/data/upload",
    method: "post",
    headers: { "Content-Type": "multipart/form-data" },
    data: param,
  });
} else;
```
