import sys
from tensorflow import keras
import tensorflow.keras.backend as K
import inspect
import os

file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f"{file_path}/layers")
sys.path.append(f"{file_path}/utils")


from base_model import BaseModel
from inspect import getmembers, isfunction

import tensorflow as tf
import layer_60a5c8f582ffc54caedc4450 as layer_60a5c8f582ffc54caedc4450
import layer_60a5c8f582ffc54caedc4454 as layer_60a5c8f582ffc54caedc4454
import layer_60a5c8f582ffc54caedc4456 as layer_60a5c8f582ffc54caedc4456
import layer_60a5c8f582ffc54caedc4458 as layer_60a5c8f582ffc54caedc4458
import layer_60a5c8f582ffc54caedc445a as layer_60a5c8f582ffc54caedc445a
import layer_60a5c8f582ffc54caedc445c as layer_60a5c8f582ffc54caedc445c
import layer_60a5c8f582ffc54caedc445e as layer_60a5c8f582ffc54caedc445e
import layer_60a5c8f582ffc54caedc4460 as layer_60a5c8f582ffc54caedc4460
import layer_60a5c8f582ffc54caedc4462 as layer_60a5c8f582ffc54caedc4462
import layer_60a5c8f582ffc54caedc4464 as layer_60a5c8f582ffc54caedc4464
import layer_60a5c8f582ffc54caedc4466 as layer_60a5c8f582ffc54caedc4466
import layer_60a5c8f582ffc54caedc4468 as layer_60a5c8f582ffc54caedc4468
import layer_60a5c8f582ffc54caedc446a as layer_60a5c8f582ffc54caedc446a
import layer_60a5c8f582ffc54caedc446c as layer_60a5c8f582ffc54caedc446c
import layer_60a5c8f582ffc54caedc446e as layer_60a5c8f582ffc54caedc446e
import layer_60a5c8f582ffc54caedc4470 as layer_60a5c8f582ffc54caedc4470
import layer_60a5c8f582ffc54caedc4472 as layer_60a5c8f582ffc54caedc4472
import layer_60a5c8f582ffc54caedc4474 as layer_60a5c8f582ffc54caedc4474
import layer_60a5c8f582ffc54caedc4476 as layer_60a5c8f582ffc54caedc4476
import layer_60a5c8f582ffc54caedc4478 as layer_60a5c8f582ffc54caedc4478
import layer_60a5c8f582ffc54caedc447a as layer_60a5c8f582ffc54caedc447a
import layer_60a5c8f582ffc54caedc447c as layer_60a5c8f582ffc54caedc447c
import layer_60a5c8f582ffc54caedc447e as layer_60a5c8f582ffc54caedc447e
import layer_60a5c8f582ffc54caedc4480 as layer_60a5c8f582ffc54caedc4480
import layer_60a5c8f582ffc54caedc4482 as layer_60a5c8f582ffc54caedc4482
import layer_60a5c8f582ffc54caedc4484 as layer_60a5c8f582ffc54caedc4484


def get_layer_object(module):
    for member in getmembers(module):
        if member[1].__module__ == module.__name__:
            return member[1]

def get_loss_sum_fn(list_loss):
    def LossSum(y_true, y_pred):
        loss = 0
        for loss_fn in list_loss:
            loss += loss_fn(y_true, y_pred)
        return loss

    return LossSum

class Model(BaseModel):
    def __init__(self, *args, **kwargs):
        super(Model, self).__init__(*args, **kwargs)
        self.path_weight = file_path + "/weight.hdf5"
        inputs, outputs, losses, labels = self.build_source()
        self.compile(inputs, outputs, losses, labels)

    def build_source(self):
        config_loss = dict()
        volume = 256
        height = 256
        width = 256
        channels = 1
        num_class = 6
        output_channels = 1
        batch_size = 1

        n1_Image = layer_60a5c8f582ffc54caedc4450.Image(shape=[256, 256, 1])
        n2_backbone_n1_Conv2D = layer_60a5c8f582ffc54caedc4454.Conv2D(filters=64, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n1_Image)
        n2_backbone_n2_Conv2D = layer_60a5c8f582ffc54caedc4456.Conv2D(filters=64, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n1_Conv2D)
        n2_backbone_n3_MaxPooling2D = layer_60a5c8f582ffc54caedc4458.MaxPooling2D(pool_size=[2, 2], strides=[2, 2], padding='valid')(n2_backbone_n2_Conv2D)
        n2_backbone_n4_Conv2D = layer_60a5c8f582ffc54caedc445a.Conv2D(filters=128, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n3_MaxPooling2D)
        n2_backbone_n5_Conv2D = layer_60a5c8f582ffc54caedc445c.Conv2D(filters=128, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n4_Conv2D)
        n2_backbone_n6_MaxPooling2D = layer_60a5c8f582ffc54caedc445e.MaxPooling2D(pool_size=[2, 2], strides=[2, 2], padding='valid')(n2_backbone_n5_Conv2D)
        n2_backbone_n7_Conv2D = layer_60a5c8f582ffc54caedc4460.Conv2D(filters=256, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n6_MaxPooling2D)
        n2_backbone_n8_Conv2D = layer_60a5c8f582ffc54caedc4462.Conv2D(filters=256, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n7_Conv2D)
        n2_backbone_n9_Conv2D = layer_60a5c8f582ffc54caedc4464.Conv2D(filters=256, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n8_Conv2D)
        n2_backbone_n10_Conv2D = layer_60a5c8f582ffc54caedc4466.Conv2D(filters=256, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n9_Conv2D)
        n2_backbone_n11_MaxPooling2D = layer_60a5c8f582ffc54caedc4468.MaxPooling2D(pool_size=[2, 2], strides=[2, 2], padding='valid')(n2_backbone_n10_Conv2D)
        n2_backbone_n12_Conv2D = layer_60a5c8f582ffc54caedc446a.Conv2D(filters=512, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n11_MaxPooling2D)
        n2_backbone_n13_Conv2D = layer_60a5c8f582ffc54caedc446c.Conv2D(filters=512, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n12_Conv2D)
        n2_backbone_n14_Conv2D = layer_60a5c8f582ffc54caedc446e.Conv2D(filters=512, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n13_Conv2D)
        n2_backbone_n15_Conv2D = layer_60a5c8f582ffc54caedc4470.Conv2D(filters=512, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n14_Conv2D)
        n2_backbone_n16_MaxPooling2D = layer_60a5c8f582ffc54caedc4472.MaxPooling2D(pool_size=[2, 2], strides=[2, 2], padding='valid')(n2_backbone_n15_Conv2D)
        n2_backbone_n17_Conv2D = layer_60a5c8f582ffc54caedc4474.Conv2D(filters=512, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n16_MaxPooling2D)
        n2_backbone_n18_Conv2D = layer_60a5c8f582ffc54caedc4476.Conv2D(filters=512, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n17_Conv2D)
        n2_backbone_n19_Conv2D = layer_60a5c8f582ffc54caedc4478.Conv2D(filters=512, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n18_Conv2D)
        n2_backbone_n20_Conv2D = layer_60a5c8f582ffc54caedc447a.Conv2D(filters=512, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_backbone_n19_Conv2D)
        n2_backbone_n21_MaxPooling2D = layer_60a5c8f582ffc54caedc447c.MaxPooling2D(pool_size=[2, 2], strides=[2, 2], padding='valid')(n2_backbone_n20_Conv2D)
        n3_Flatten = layer_60a5c8f582ffc54caedc447e.Flatten()(n2_backbone_n21_MaxPooling2D)
        n4_Dense = layer_60a5c8f582ffc54caedc4480.Dense(units=4096, activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n3_Flatten)
        n5_Dense = layer_60a5c8f582ffc54caedc4482.Dense(units=4096, activation='relu', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n4_Dense)
        n6_Dense = layer_60a5c8f582ffc54caedc4484.Dense(units=6, activation='softmax', use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n5_Dense)
        label = keras.layers.Input(shape=[6])
        loss = keras.losses.CategoricalCrossentropy()(label, n6_Dense)
        



        for key in list(config_loss.keys()):
            if len(config_loss[key]) == 1:
                config_loss[key] = config_loss[key][0]
            elif len(config_loss[key]) > 1:
                config_loss[key] = get_loss_sum_fn(config_loss[key])
            else:
                del config_loss[key]
        inputs = [n1_Image]
        outputs = [n6_Dense]
        losses = [loss]
        labels = [label]

        return inputs, outputs, losses, labels

