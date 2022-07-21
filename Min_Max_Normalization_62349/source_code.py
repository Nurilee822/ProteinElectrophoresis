# -------------------------------------------------------------------------
# 상기 프로그램에 대한 저작권을 포함한 지적재산권은 Deepnoid에 있으며,
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

from deepphi.image_processing import Preprocessing
import numpy as np


class Min_Max_Normalization(Preprocessing):
    def __init__(self):
        super(Min_Max_Normalization, self).__init__()

    def __call__(self, data, save_path=None):
        self.header_check(data)
        img_array = data['image']['array'] # input image
        
        # main image processing
        min_value = np.min(img_array)
        max_value = np.max(img_array)
        diviser = max_value - min_value
        if diviser == 0:
            if max_value != 0:
                new_array = img_array / max_value
            else:
                new_array = img_array
        else:
            new_array = (img_array - min_value) / (max_value - min_value)

        new_array = np.float32(new_array)
        data['image']['array'] = new_array # output image
        data['image']['header']['dtype'] = str(new_array.dtype)
        data['image']['header']['rescale'] = True # add normalization header
        data['image']['header']['original_scale'] = [min_value, max_value]
        return data

    # header check
    def header_check(self, data):
        # feature merge check
        if 'feature_merge' in data['image']['header']:
            raise ValueError("After 'Feature Merge' module, image processing module is not available. \n"
                             "Only Neural Network modules can be connected.")