# -------------------------------------------------------------------------
# 상기 프로그램에 대한 저작권을  포함한 지적재산권은 Deepnoid에 있으며,
# Deepnoid가 명시적으로 허용하지 않은 사용, 복사, 변경, 제3자에의 공개,
# 배포는 엄격히 금지되며, Deepnoid의 지적재산권 침해에 해당됩니다.
# (Copyright ⓒ 2020 Deepnoid Co., Ltd. All Rights Reserved|Confidential)
# -------------------------------------------------------------------------
# You are strictly prohibited to copy, disclose, distribute, modify,
# or use this program in part or as a whole without the prior written
# consent of Deepnoid Co., Ltd. Deepnoid Co., Ltd., owns the
# intellectual property rights in and to this program.
# (Copyright ⓒ 2020 Deepnoid Co., Ltd. All Rights Reserved|Confidential)
# -------------------------------------------------------------------------

import logging
import numpy as np
import cv2
from deepphi.image_processing import Preprocessing


class HistogramEqualization__CLAHE_gray(Preprocessing):
    def __init__(self, limit, kernel_size):
        super(HistogramEqualization__CLAHE_gray, self).__init__()
        self.color_rule = ['L']
        self.dtype_rule = 'uint8'
        self.parameter_check(kernel_size, limit)
        self.limit = limit
        self.kernel_size = kernel_size

    def __call__(self, data, save_path=None):
        self.data_check(data)
        img_array = data['image']['array']
        img_dimension = data['image']['header']['dim']

        # main image processing
        # 2d case
        if img_dimension == 2:
            clahe = cv2.createCLAHE(clipLimit=self.limit, tileGridSize=(self.kernel_size, self.kernel_size))
            new_array = clahe.apply(img_array)

        # 3d case
        else:
            new_array = np.zeros_like(img_array)
            for i in range(img_array.shape[0]):
                clahe = cv2.createCLAHE(clipLimit=self.limit, tileGridSize=(self.kernel_size, self.kernel_size))
                new_array[i,] = clahe.apply(img_array[i,])
        
        # rescale
        if 'rescale' in data['image']['header']:
            new_array = np.float32((new_array/255) * (self.ori_max - self.ori_min) + self.ori_min)

        data['image']['array'] = new_array # output image
        data['image']['header']['dtype'] = str(new_array.dtype)
        return data

    # parameter check
    def parameter_check(self, kernel_size, limit):
        if self.isNumber(kernel_size) == False:
            raise ValueError('There is no kernel_size value. \nPlease enter kernel_size.')
        if self.isNumber(limit) == False:
            raise ValueError('There is no limit value. \nPlease enter limit.')      

    # data check
    def data_check(self,data):
        self.header_check(data)
        self.data_type_check(data)

    def header_check(self, data):
        # feature merge check
        if 'feature_merge' in data['image']['header']:
            raise ValueError("After 'Feature Merge' module, image processing module is not available. \n"
                             "Only Neural Network modules can be connected.")
        # color mode check
        if 'color_mode' not in data['image']['header']:
            raise KeyError("Color_mode information is required to process. \nPlease add the Color_mode information.")
        if data['image']['header']['color_mode'] not in self.color_rule:
            raise ValueError("Only grayscale images('Gray' color mode) are accepted. \n"
                            "Please proceed after converting to grayscale image through 'Color to Grayscale' module from the Color categroy. \n"
                            "If the color mode is 'multi', please convert it 1 channel grayscale through 'Channel Split Filter' module in the Data Manipulation.")
        # dimension check
        if 'dim' not in data['image']['header']:
            raise KeyError(
                "Dimension information is required to process. \nPlease add the Dimension information.")
        
    # data type check
    def data_type_check(self,data):
        tmp_array = data['image']['array']
        if tmp_array.dtype != self.dtype_rule:
            tmp_array = self.make_uint8(tmp_array)
            data['image']['array'] = tmp_array
            data['image']['header']['dtype'] = 'uint8'

    # make uint8
    def make_uint8(self,array):
        self.ori_max = np.max(array)
        self.ori_min = np.min(array)
        diviser = self.ori_max - self.ori_min
        if diviser == 0:
            if self.ori_max != 0:
                array = np.uint8(array/self.ori_max*255)
            else:
                array = np.uint8(array)
        else:
            array = np.uint8((array - self.ori_min) / (diviser) * 255)
        return array

    def isNumber(self,number):
        try:
            float(number)
            return True
        except:
            return False