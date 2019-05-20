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
//（使得其他模块可以调用该函数）
module.exports = xx;
```
```javascript
// 另一个js调用上面的xx
var greet = require('./test'); // './test'为相对目录！
greet(1123)
```
---
4. 使用函数
