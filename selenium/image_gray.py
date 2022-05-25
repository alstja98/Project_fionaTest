import cv2
from PIL import Image

#이미지 회색으로 바꾸기
for i in range(1,2):
    for j in range(1,150):
        try:
            path = "./img0"+str(i)+"/gray"+str(j)+".jpg"
            # 이미지 읽기
            img_color = cv2.imread("./img0"+str(i)+"/cropped"+str(j)+".png", cv2.IMREAD_COLOR)

            # 컬러 이미지를 그레이스케일로 변환
            img_cv_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

            # 이미지 저장
            cv2.imwrite(path, img_cv_gray)
        except:
            pass
