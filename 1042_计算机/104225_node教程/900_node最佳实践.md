---
id: e5239581-eba5-402e-bb93-01112e5c84d2
---

# node 最佳实践

## 异步

### 使用 promise 简易封装 child_process

```typescript
import { spawn } from "child_process";

export const spawnAsPromised = (command:string, args:string[], options:object) => {
  return new Promise( (resolve, reject) {
    let stdout = "";
    let stderr = "";
    const cp = spawn(command, args, options);
    cp.stdout.on("data",  (chunk) {
      stdout += chunk;
    });
    cp.stderr.on("data",  (chunk) {
      stderr += chunk;
    });
    cp.on("close",  (code) {
      if (code === 0) {
        resolve(stdout);
      } else {
        reject(stderr);
      }
    });
  });
};
```
