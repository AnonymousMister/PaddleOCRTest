import os
import cv2
from paddleocr import PPStructure,draw_structure_result,save_structure_res


if __name__ == '__main__':
    table_engine = PPStructure(show_log=True, image_orientation=True,use_gpu=False)

    save_folder = './output'
    img_path = './fp.jpg'
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder,os.path.basename(img_path).split('.')[0])

    for line in result:
        line.pop('img')
        print(line)

    from PIL import Image

    font_path = './simfang.ttf' # PaddleOCR下提供字体包
    image = Image.open(img_path).convert('RGB')
    im_show = draw_structure_result(image, result,font_path=font_path)
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')