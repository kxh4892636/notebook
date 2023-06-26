# eslint 教程

## 基础

**eslint**

- 代码风格检查;

**安装**

```bash
pnpm add eslint
```

**配置文件**

- .eslintrc.js/cjs/xml/json: 配置文件;
- .eslintignore: 忽略文件;

**常用命令**

```bash
# 检查 src 文件夹下所有文件, 最大报错数为 0
eslint src --max-warnings 0
# 尝试修复 src 文件夹下所有文件1错误
eslint src --fix
```

## 配置文件

### 常用配置文件

**node**

```javascript
// eslint-disable-next-line no-undef
module.exports = {
  root: true,
  env: { es2020: true, node: true, "jest/globals": true },
  extends: [
    "eslint:recommended",
    "standard",
    "plugin:@typescript-eslint/recommended",
    "plugin:jsdoc/recommended",
    "plugin:import/recommended",
    "plugin:import/typescript",
    "plugin:promise/recommended",
  ],
  parser: "@typescript-eslint/parser",
  parserOptions: { ecmaVersion: "latest", sourceType: "module" },
  plugins: ["@typescript-eslint","import", "promise", "jest"],
  rules: {
    "no-multiple-empty-lines": ["error", { "max": 1, "maxEOF": 0 }],
    "array-element-newline": ["error", { "multiline": true }]
  },
  settings: {
    "import/resolver": {
      typescript: {
        alwaysTryTypes: true,
        project: ["tsconfig.json", "package/*/tsconfig.json"],
      },
      node: {
        project: ["tsconfig.json", "package/*/tsconfig.json"],
      },
    },
  },
};
```

**react**

```javascript
// eslint-disable-next-line no-undef
module.exports = {
  root: true,
  env: { browser: true, es2020: true, "jest/globals": true },
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:import/recommended",
    "plugin:import/typescript",
    "plugin:jsdoc/recommended",
    "plugin:jsx-a11y/recommended",
    "plugin:promise/recommended",
    "plugin:react/recommended",
    "plugin:react/jsx-runtime",
    "plugin:react-hooks/recommended",
  ],
  parser: "@typescript-eslint/parser",
  parserOptions: { ecmaVersion: "latest", sourceType: "module" },
  plugins: ["@typescript-eslint", "jsx-a11y", "promise", "import", "jest"],
  rules: {
    "no-multiple-empty-lines": ["error", { "max": 1, "maxEOF": 0 }],
    "array-element-newline": ["error", { "multiline": true }]
  },
  settings: {
    react: {
      version: "detect",
    },
  },
};

```

## 常用插件

### eslint-plugin-jsx-a11y

**安装**

```bash
pnpm add add eslint-plugin-jsx-a11y --save-dev
```

**配置**

```javascript
module.exports = {
  extends: ['eslint:recommended', 'plugin:jsx-a11y/recommended'],
  plugins: ['jsx-a11y'],
  root: true,
};
```

### eslint-plugin-jest

**安装**

```bash
pnpm add add eslint-plugin-jest --save-dev
```

**配置**

```javascript
module.exports = {
  env: { "jest/globals": true }
  plugins: ['jest'],
  root: true,
};
```

### eslint-plugin-react

**安装**

```bash
pnpm add add eslint-plugin-react --save-dev
```

**配置**

```javascript
module.exports = {
  extends: ['eslint:recommended', 'plugin:react/recommended', 'plugin:react/jsx-runtime'],
  root: true,
};
```

### eslint-plugin-react-hooks

**安装**

```bash
pnpm add add eslint-plugin-react-hooks --save-dev
```

**配置**

```javascript
module.exports = {
  extends: ['eslint:recommended', 'plugin:react-hooks/recommended'],
  root: true,
};
```

### eslint-plugin-import

**安装**

```bash
pnpm add add eslint-plugin-import --save-dev
```

**配置**

```javascript
module.exports = {
  extends: ['eslint:recommended', 'plugin:import/recommended'],
  plugins: ['import'],
  root: true,
};
```

**typescript 支持**

- 安装 eslint-import-resolver-typescript;

### eslint-import-resolver-typescript

**安装**

```bash
pnpm add add eslint-import-resolver-typescript --save-dev
```

**配置**

```javascript
module.exports = {
  extends: ['eslint:recommended', 'plugin:@typescript-eslint/recommended'],
  plugins: ['import'],
  root: true,
  settings: {
    "import/resolver": {
        typescript: {
        alwaysTryTypes: true,
        project: ["tsconfig.json", "package/*/tsconfig.json"],
        },
        node: {
        project: ["tsconfig.json", "package/*/tsconfig.json"],
        },
    },
  },
};
```

### typescript-eslint/eslint-plugin

**安装**

```bash
pnpm add add @typescript-eslint/parser @typescript-eslint/eslint-plugin --save-dev
```

**配置**

```javascript
module.exports = {
  extends: ['eslint:recommended', 'plugin:@typescript-eslint/recommended'],
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint'],
  root: true,
};
```

**typescript 支持**

- 安装 eslint-import-resolver-typescript;
- 
### eslint-plugin-promise

**安装**

```bash
pnpm add add eslint-plugin-promise --save-dev
```

**配置**

```javascript
module.exports = {
  extends: ['eslint:recommended', 'plugin:promise/recommended'],
  plugins: ['promise'],
  root: true,
};
```

### eslint-config-standard

**安装**

```bash
pnpm add add eslint-config-standard --save-dev
```

**配置**

```javascript
module.exports = {
  extends: ['eslint:recommended', "standard"],
  root: true,
};
```

### eslint-plugin-jsdoc

**安装**

```bash
pnpm add add eslint-plugin-jsdoc --save-dev
```

**配置**

```javascript
module.exports = {
  extends: ['eslint:recommended', "plugin:jsdoc/recommended"],
  root: true,
};
```