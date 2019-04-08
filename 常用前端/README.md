# 常用

* [取消点击事件](#取消点击事件)
* [去除下划线](#去除下划线)
* [无法选中文字](#无法选中文字)



取消点击事件:
```html
style="pointer-events: none;"
```
---
去除下划线
```html
text-decoration: none;
```
---
无法选中文字
*     <head css>
* --为多浏览器兼容
```html
.cannotselect {
-webkit-touch-callout: none;
-webkit-user-select: none;
-moz-user-select: none;
-ms-user-select: none;
user-select: none;
}
```
---
