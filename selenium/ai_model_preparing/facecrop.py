import os
from PIL import Image
from autocrop import Cropper

#다운받은 사진 얼굴만 자르기!

cropper = Cropper()

for i in range(1,2):
    for j in range(1,150):
        try:
            cropped_array = cropper.crop('./img0'+str(i)+'/'+str(j)+'.jpg')
            cropped_image = Image.fromarray(cropped_array)
            cropped_image.save('./img0'+str(i)+'/cropped'+str(j)+'.png')
            if os.path.exists('./img0'+str(i)+'/'+str(j)+'.jpg'):
                os.remove('./img0'+str(i)+'/'+str(j)+'.jpg')
        except:
            pass

