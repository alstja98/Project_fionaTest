from PIL import Image
from autocrop import Cropper

#다운받은 사진 얼굴만 자르기!

cropper = Cropper()

for i in range(9,10):
    for j in range(1,150):
        try:
            cropped_array = cropper.crop('./img0'+str(i)+'/'+str(j)+'.png')
            cropped_image = Image.fromarray(cropped_array)
            cropped_image.save('./img0'+str(i)+'/cropped'+str(j)+'.png')
        except:
            pass