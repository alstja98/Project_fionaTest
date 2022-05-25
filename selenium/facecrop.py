from PIL import Image
from autocrop import Cropper

#다운받은 사진 얼굴만 자르기!

cropper = Cropper()

for i in range(1,150):
    try:
        cropped_array = cropper.crop('./img05/'+str(i)+'.jpg')
        cropped_image = Image.fromarray(cropped_array)
        cropped_image.save('./img05/cropped'+str(i)+'.png')
    except:
        pass