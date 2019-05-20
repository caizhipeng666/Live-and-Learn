# Node.js day-1
1. use strict
> 严格模式
```javascript
node --use_strict xxx.js
```
```javascript
'use strict';
...
```
---
2. 使用变量(注意符号是`不是')
```javascript
var name = 'world';
var s = `hello, ${name}!`;
console.log(s);
```
---
3. 使用函数
```javascript
// 创建
function xx(name) {
    console.log(name + ',' + s + '!');
}
// 调用
xx(111)
// ✓暴露给其他模块
module.exports = xx;
```
