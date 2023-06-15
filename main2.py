import datetime
import os
import fitz  # fitz就是pip install PyMuPDF
import cv2
import shutil
import numpy as np
import pandas as pd
from tqdm import tqdm
import json


def get_pic_info(path):
    # 将整理后的抽取结果返回为字典
    if os.path.splitext(path)[-1] == '.pdf':
        pdfDoc = fitz.open(path)
        for pg in range(pdfDoc.page_count):
            page = pdfDoc[pg]
            rotate = int(0)
            zoom_x = 4  # (1.33333333-->1056x816)   (2-->1584x1224)
            zoom_y = 4
            mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            # 保存过渡图片
            pix.save(path[:-4] + '_%s.jpeg' % pg)


def get_pics(path):
    filenames = os.listdir(path)
    result = []
    for filename in tqdm(filenames):
        get_pic_info(os.path.join(path, filename))


if __name__ == '__main__':
    result = get_pics('resume_train_20200121/pdf')
