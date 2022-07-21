#   상기 프로그램에 대한 저작권을 포함한 지적재산권은 Deepnoid에 있으며,
#   Deepnoid가 명시적으로 허용하지 않은 사용, 복사, 변경, 제3자에의 공개,
#   배포는 엄격히 금지되며, Deepnoid의 지적재산권 침해에 해당됩니다.
#   (Copyright ⓒ 2020 Deepnoid Co., Ltd. All Rights Reserved|Confidential)
#  -----------------------------------------------------------------------------
#   You are strictly prohibited to copy, disclose, distribute, modify,
#   or use this program in part or as a whole without the prior written
#   consent of Deepnoid Co., Ltd. Deepnoid Co., Ltd., owns the
#   intellectual property rights in and to this program.
#   (Copyright ⓒ 2020 Deepnoid Co., Ltd. All Rights Reserved|Confidential)
#  -----------------------------------------------------------------------------
#

import tensorflow as tf
import numpy as np
import json
import os
PATH_SCRIPT = os.path.dirname(os.path.abspath(__file__))


class BaseModel(object):
    def __init__(self, label_type=None):
        self.path_weight = None
        self.model = None
        self.set_label_type(label_type)
        self.class_info = self.get_class_info()

    def set_label_type(self, label_type):
        self.label_type = self.get_label_name(label_type)

    def compile(self, inputs, outputs, losses, labels):
        self.model = tf.keras.Model(inputs=inputs, outputs=outputs)
        self.load_weight()

    def load_weight(self):
        self.model.load_weights(self.path_weight)

    def __call__(self, data):
        prediction = self.call_tensorflow(data)
        data = self.save_pred_result(data, prediction)
        return data

    def call_tensorflow(self, data):
        img = data['image']['array']
        if not data['image']['header']['IsVector']:
            img = np.expand_dims(img, axis=-1)
        img = np.expand_dims(img, axis=0)

        prediction = self.model.predict(img)[0]
        return prediction

    def processing_pred_result(self, prediction):
        if self.label_type in ('Detection 2D', 'Detection 3D'):
            bbox = prediction[0]
            score = prediction[1]
            label = prediction[2]

            y_pred_this = [bbox, score, label]
        else:
            y_pred_this = prediction

        return y_pred_this

    def save_pred_result(self, data, y_pred_this):
        pred = self._add_prediction(y_pred_this)
        data['prediction'][self.label_type] = pred[self.label_type]
        # if self.label_type == 'classification':
        #     grad_cam_batch = self._get_grad_cam(img)
        #     data['prediction'][self.label_type]['grad_cam'] = grad_cam_batch[0]
        return data

    def _add_prediction(self, y_pred):
        prediction = dict()
        header = {'class_info': self.class_info}
        label_type = self.label_type
        if label_type == 'classification':
            prediction[self.label_type] = {'array': y_pred, 'header': header}
        elif label_type in ['segmentation', 'transformation']:
            if y_pred.shape[-1] == 1:
                y_pred = np.squeeze(y_pred, axis=-1)
            prediction[self.label_type] = {'array': y_pred, 'header': header}
        elif label_type in ['object_detection']:
            cls = np.array(y_pred[..., 0]).astype('int')
            score = y_pred[..., 1]
            bbox = y_pred[..., 2:]

            idx_valid = np.sum(bbox, axis=-1) != 0
            cls = cls[idx_valid]
            score = score[idx_valid]
            bbox = bbox[idx_valid]

            num_object = cls.shape[0]
            num_class = len(self.class_info)

            one_hot = np.zeros([num_object, num_class])
            one_hot[:, cls] = 1

            prediction[self.label_type] = {'bbox_coordinate': bbox,
                                           'bbox_class': one_hot,
                                           'bbox_score': score,
                                           'header': header}
        else:
            raise Exception
        return prediction

    def get_label_name(self, label_type):
        if label_type in ['Classification 2D', 'Classification 3D']:
            label_type = "classification"
        elif label_type in ['Segmentation 2D', 'Segmentation 3D']:
            label_type = "segmentation"
        elif label_type in ['Detection 2D', 'Detection 3D']:
            label_type = "object_detection"
        elif label_type in ['Transformation 2D', 'Transformation 3D']:
            label_type = 'transformation'

        return label_type

    def get_class_info(self):
        with open(f'{PATH_SCRIPT}/../class_info.json', "r") as f:
            class_info = json.load(f)

        return class_info



