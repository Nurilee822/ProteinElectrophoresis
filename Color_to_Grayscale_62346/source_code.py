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


class ColortoGrayscale(Preprocessing):
    def __init__(self):
        super(ColortoGrayscale, self).__init__()
        self.color_rule = ['Binary', 'multi', 'mask']
        self.color_offer = ['RGB', 'HSV', 'YCrCb', 'Lab', 'L']
        self.dtype_rule = ['int16', 'int32', 'float64']

    def __call__(self, data, save_path=None):
        self.data_check(data)
        img_array = data['image']['array']
        img_color = data['image']['header']['color_mode'] # image color
        img_dimension = data['image']['header']['dim']

        # main image processing
        # 2d case
        if img_dimension == 2:
            if img_color == 'L':
                new_array = img_array
            if img_color == 'RGB':
                new_array = cv2.cvtColor(img_array,cv2.COLOR_RGB2GRAY)
            elif img_color == 'HSV':
                img_tmp = cv2.cvtColor(img_array, cv2.COLOR_HSV2RGB)
                new_array = cv2.cvtColor(img_tmp, cv2.COLOR_RGB2GRAY)
            elif img_color == 'YCrCb':
                img_tmp = cv2.cvtColor(img_array, cv2.COLOR_YCrCb2RGB)
                new_array = cv2.cvtColor(img_tmp, cv2.COLOR_RGB2GRAY)
            elif img_color == 'Lab':
                img_tmp = cv2.cvtColor(img_array, cv2.COLOR_LAB2RGB)
                new_array = cv2.cvtColor(img_tmp, cv2.COLOR_RGB2GRAY)
        # 3d case
        else:
            if img_color == 'L':
                new_array = img_array
            else:
                new_array = np.zeros_like(img_array[:,:,:,0])
                for i in range(img_array.shape[0]):
                    if img_color == 'RGB':
                        new_array[i,] = cv2.cvtColor(img_array[i,],cv2.COLOR_RGB2GRAY)
                    elif img_color == 'HSV':
                        img_tmp = cv2.cvtColor(img_array[i,], cv2.COLOR_HSV2RGB)
                        new_array[i,] = cv2.cvtColor(img_tmp, cv2.COLOR_RGB2GRAY)
                    elif img_color == 'YCrCb':
                        img_tmp = cv2.cvtColor(img_array[i,], cv2.COLOR_YCrCb2RGB)
                        new_array[i,] = cv2.cvtColor(img_tmp, cv2.COLOR_RGB2GRAY)
                    elif img_color == 'Lab':
                        img_tmp = cv2.cvtColor(img_array[i,], cv2.COLOR_LAB2RGB)
                        new_array[i,] = cv2.cvtColor(img_tmp, cv2.COLOR_RGB2GRAY)

        # rescale
        if 'rescale' in data['image']['header']:
            new_array = (new_array/255) * (self.ori_max - self.ori_min) + self.ori_min

        data['image']['array'] = new_array # output image
        data['image']['header']['dtype'] = str(new_array.dtype)
        data['image']['header']['color_mode'] = 'L' # color mode change

        # dimension change
        data['image']['header']['ndim'] = data['image']['header']['dim']
        data['image']['header']['IsVector'] = False
        return data


    # data check
    def data_check(self,data):
        self.header_check(data)
        self.rescale_check(data)
        self.data_type_check(data)

    def header_check(self, data):
        # feature merge check
        if 'feature_merge' in data['image']['header']:
            raise ValueError("After 'Feature Merge' module, image processing module is not available. \n"
                             "Only Neural Network modules can be connected.")
        # color mode check
        if 'color_mode' not in data['image']['header']:
            raise KeyError("img_color information is required to process. \nPlease add the img_color information.")
        if data['image']['header']['color_mode'] in self.color_rule:
            raise ValueError("Binary, multi, mask images can't process this module. \n" 
                            "Only Color or Grayscale images are accepted")
        else:
            if data['image']['header']['color_mode'] not in self.color_offer:
                raise ValueError("The color mode of the dataset has been changed to something other than the color mode provided by DEEP:PHI. \n" 
                                "Change to one of RGB, HSV, YCrCb, Lab.")
        #   img_dimension check
        if 'dim' not in data['image']['header']:
            raise KeyError("img_dimension information is required to process. \nPlease add the img_dimension information.")

    # rescale check    
    def rescale_check(self, data):
        if 'rescale' in data['image']['header']:
            tmp_array = data['image']['array']
            self.ori_max = np.max(tmp_array)
            self.ori_min = np.min(tmp_array)
            diviser = self.ori_max - self.ori_min
            if diviser == 0:
                if self.ori_max != 0:
                    tmp_array = tmp_array/self.ori_max*255
            else:
                tmp_array =(tmp_array - self.ori_min) / (diviser) * 255
            data['image']['array'] = np.float32(tmp_array)

    # data type check
    def data_type_check(self,data):
        tmp_array = data['image']['array']
        if tmp_array.dtype in self.dtype_rule:
            tmp_array = np.float32(tmp_array)
            data['image']['array'] = tmp_array
            data['image']['header']['dtype'] = 'float32'


