# Tesseract
> 开源的OCR识别引擎   
> https://github.com/sirfz/tesserocr   

1. 安装
### Windows
```
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.00dev.exe
```
### Linux
```
```

2. 使用
### pytesseract
* 配置路径
```python
pytesseract.pytesseract.tesseract_cmd = 'C:\\xxx\Tesseract-OCR\\tesseract.exe'

tessdata_dir_config = r'--tessdata-dir "<your_tessdata_dir_path>"'
```
图片识别fun|说明
---|---
get_tesseract_version|返回系统中安装的Tesseract版本。
image_to_string|将图像上的Tesseract OCR运行结果返回到字符串
image_to_boxes|返回包含已识别字符及其框边界的结果
image_to_data|返回包含框边界，置信度和其他信息的结果(需要Tesseract 3.05+)
image_to_osd|返回包含有关方向和脚本检测的信息的结果。
---
图片识别params|类型|说明
---|---|---
image|object|图像对象
lang|String|语言代码字符串
config|String|任何其他配置为字符串，例如：config='--psm 6'
nice|Integer|修改Tesseract运行的处理器优先级(Windows不支持)
output_type|(自定)|类属性，指定输出的类型，默认为string
---
```python
im = Image.open('x.png')
result = pytesseract.image_to_string(im, lang='chi_sim')
# print(result.strip().replace(' ', '').replace('\'', '').replace('。', ''))
print(result)
```

### 简单图像处理
操作|解释
---|---
[二值化处理](#二值化处理)|转为黑白

##### 二值化处理
> 将图像上的像素点的灰度值设置为0或255，也就是将整个图像呈现出明显的黑白效果的过程。
```
from PIL import Image
im = Image.open('xxx.jpg')
im = im.convert('L')
im.save("x1.jpg")

threshold = 200
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
xx = im.point(table, '1')
xx.save("x2.jpg")
```

