import pygetwindow as gw
import pyautogui
import pytesseract
import time
from PIL import ImageEnhance, ImageFilter

# 设置 Tesseract 的路径
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 自定义配置，允许识别数字
custom_config = r'--psm 6 -c tessedit_char_whitelist=0123456789'
count=0 #限制次数
# 获取窗口列表并找到目标窗口
windows = gw.getAllTitles()
target_window = None
for window in windows:
    if "MuMu" in window:
        target_window = gw.getWindowsWithTitle(window)[0]
        break

if not target_window:
    print("未找到目标窗口")
    exit()

left = target_window.left
top = target_window.top
width = target_window.width
height = target_window.height

while count<=200:
    count += 1
    # 截取该区域的屏幕
    screenshot = pyautogui.screenshot(region=(left + 100, top + 300, width - 400, height - 850))
    screenshot2 = pyautogui.screenshot(region=(left + 200, top + 300, width - 400, height - 850))
    screenshot3 = pyautogui.screenshot(region=(left + 300, top + 300, width - 400, height - 850))
    # 将截图转换为灰度图像
    gray_image = screenshot.convert('L')
    gray_image2 = screenshot2.convert('L')
    gray_image3 = screenshot3.convert('L')

    # 调整对比度
    enhancer = ImageEnhance.Contrast(gray_image)
    enhancer2 = ImageEnhance.Contrast(gray_image2)
    enhancer3 = ImageEnhance.Contrast(gray_image3)
    enhanced_image = enhancer.enhance(8.5)  # 进一步增强对比度
    enhanced_image2 = enhancer2.enhance(8.5)
    enhanced_image3 = enhancer3.enhance(8.5)
    # 二值化处理
    binary_image = enhanced_image.point(lambda x: 0 if x < 160 else 255, '1')
    binary_image2 = enhanced_image2.point(lambda x: 0 if x < 160 else 255, '1')
    binary_image3 = enhanced_image3.point(lambda x: 0 if x < 160 else 255, '1')
    # 去除噪点
    denoised_image = binary_image.filter(ImageFilter.MedianFilter())
    denoised_image2 = binary_image2.filter(ImageFilter.MedianFilter())
    denoised_image3 = binary_image3.filter(ImageFilter.MedianFilter())
    # 保存处理后的图片
    #denoised_image.save('processed_image.png')
    # 保存图片到当前目录
    #denoised_image3.save('processed_image3.png')
    # 保存图片到当前目录
    # 使用 pytesseract 进行 OCR 识别
    try:
        text = pytesseract.image_to_string(denoised_image, config=custom_config,lang='eng')
        text3 = pytesseract.image_to_string(denoised_image3, config=custom_config, lang='eng')
        print("识别到的文字:")
        if eval(text)>eval(text3):
            print('{}>{}'.format(eval(text),eval(text3)))

            # 设置绘制的起始位置
            start_x = left + 200
            start_y = top + 800

            # 移动到起始位置并按下鼠标
            pyautogui.moveTo(start_x, start_y)  # 移动到起始位置
            pyautogui.mouseDown()  # 按下鼠标以开始绘制
            pyautogui.dragTo(left + 300, top + 800)
            pyautogui.dragTo(left + 200, top + 600)

            # 释放鼠标
            pyautogui.mouseUp()  # 释放鼠标以结束绘制

        '''if eval(text)==eval(text3):
            print('{}?{}'.format(eval(text),eval(text3)))

            time.sleep(0.1)

            # 设置绘制的起始位置
            start_x = 350
            start_y = 800

            # 移动到起始位置并按下鼠标
            pyautogui.moveTo(start_x, start_y)  # 移动到起始位置
            pyautogui.mouseDown()  # 按下鼠标以开始绘制
            pyautogui.dragTo(150, 1000)
            pyautogui.dragTo(350, 1000)

            # 释放鼠标
            pyautogui.mouseUp()  # 释放鼠标以结束绘制'''
        if eval(text)<eval(text3):
            print('{}<{}'.format(eval(text),eval(text3)))

            # 设置绘制的起始位置
            start_x = left + 300
            start_y = top + 800

            # 移动到起始位置并按下鼠标
            pyautogui.moveTo(start_x, start_y)  # 移动到起始位置
            pyautogui.mouseDown()  # 按下鼠标以开始绘制
            pyautogui.dragTo(left + 200, top + 800)
            pyautogui.dragTo(left + 300, top + 600)

            # 释放鼠标
            pyautogui.mouseUp()  # 释放鼠标以结束绘制

    except :
        print(f"发生错误:")

    time.sleep(0.2)