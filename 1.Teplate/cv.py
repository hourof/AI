import cv2
import  numpy as np
import  os
# 打开摄像头
cap = cv2.VideoCapture(1)  # 0表示默认摄像头，可以根据需要更改


while True:
    # 读取一帧
    ret, frame = cap.read()

    # 确保成功读取帧
    if not ret:
        print("无法读取视频帧")
        break
    list1 = os.listdir('map/')
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for i in list1:
        template = cv2.imread('map/'+i)
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        # 使用matchTemplate找到匹配位置
        result = cv2.matchTemplate(frame_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

         # 在原始图像上绘制矩形框
        top_left = max_loc
        h, w = template_gray.shape
        bottom_right = (top_left[0] + w, top_left[1] + h)
        threshold = 0.8  # 调整阈值
        loc = np.where(result >= threshold)
        for pt in zip(*loc[::-1]):
             cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
        # 显示图像
        cv2.imshow('Frame', frame)
        # 按下 'q' 键退出循环
        if cv2.waitKey(5) & 0xFF == ord('q'):
             break

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()
