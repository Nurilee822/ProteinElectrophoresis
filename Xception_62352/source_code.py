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
import layer_60a5c91782ffc54caedc4845 as layer_60a5c91782ffc54caedc4845
import layer_60a5c91782ffc54caedc484f as layer_60a5c91782ffc54caedc484f
import layer_60a5c91782ffc54caedc4851 as layer_60a5c91782ffc54caedc4851
import layer_60a5c91782ffc54caedc4853 as layer_60a5c91782ffc54caedc4853
import layer_60a5c91782ffc54caedc4855 as layer_60a5c91782ffc54caedc4855
import layer_60a5c91782ffc54caedc4857 as layer_60a5c91782ffc54caedc4857
import layer_60a5c91782ffc54caedc4859 as layer_60a5c91782ffc54caedc4859
import layer_60a5c91782ffc54caedc485d as layer_60a5c91782ffc54caedc485d
import layer_60a5c91782ffc54caedc485f as layer_60a5c91782ffc54caedc485f
import layer_60a5c91782ffc54caedc4861 as layer_60a5c91782ffc54caedc4861
import layer_60a5c91782ffc54caedc4863 as layer_60a5c91782ffc54caedc4863
import layer_60a5c91782ffc54caedc4865 as layer_60a5c91782ffc54caedc4865
import layer_60a5c91782ffc54caedc4867 as layer_60a5c91782ffc54caedc4867
import layer_60a5c91782ffc54caedc4869 as layer_60a5c91782ffc54caedc4869
import layer_60a5c91782ffc54caedc486b as layer_60a5c91782ffc54caedc486b
import layer_60a5c91782ffc54caedc4870 as layer_60a5c91782ffc54caedc4870
import layer_60a5c91782ffc54caedc4872 as layer_60a5c91782ffc54caedc4872
import layer_60a5c91782ffc54caedc4874 as layer_60a5c91782ffc54caedc4874
import layer_60a5c91782ffc54caedc4876 as layer_60a5c91782ffc54caedc4876
import layer_60a5c91782ffc54caedc4878 as layer_60a5c91782ffc54caedc4878
import layer_60a5c91782ffc54caedc487a as layer_60a5c91782ffc54caedc487a
import layer_60a5c91782ffc54caedc487c as layer_60a5c91782ffc54caedc487c
import layer_60a5c91782ffc54caedc487e as layer_60a5c91782ffc54caedc487e
import layer_60a5c91782ffc54caedc4880 as layer_60a5c91782ffc54caedc4880
import layer_60a5c91782ffc54caedc4882 as layer_60a5c91782ffc54caedc4882
import layer_60a5c91782ffc54caedc4887 as layer_60a5c91782ffc54caedc4887
import layer_60a5c91782ffc54caedc4889 as layer_60a5c91782ffc54caedc4889
import layer_60a5c91782ffc54caedc488b as layer_60a5c91782ffc54caedc488b
import layer_60a5c91782ffc54caedc488d as layer_60a5c91782ffc54caedc488d
import layer_60a5c91782ffc54caedc488f as layer_60a5c91782ffc54caedc488f
import layer_60a5c91782ffc54caedc4891 as layer_60a5c91782ffc54caedc4891
import layer_60a5c91782ffc54caedc4893 as layer_60a5c91782ffc54caedc4893
import layer_60a5c91782ffc54caedc4895 as layer_60a5c91782ffc54caedc4895
import layer_60a5c91782ffc54caedc4897 as layer_60a5c91782ffc54caedc4897
import layer_60a5c91782ffc54caedc4899 as layer_60a5c91782ffc54caedc4899
import layer_60a5c91782ffc54caedc489e as layer_60a5c91782ffc54caedc489e
import layer_60a5c91782ffc54caedc48b0 as layer_60a5c91782ffc54caedc48b0
import layer_60a5c91782ffc54caedc48a0 as layer_60a5c91782ffc54caedc48a0
import layer_60a5c91782ffc54caedc48a2 as layer_60a5c91782ffc54caedc48a2
import layer_60a5c91782ffc54caedc48a4 as layer_60a5c91782ffc54caedc48a4
import layer_60a5c91782ffc54caedc48a6 as layer_60a5c91782ffc54caedc48a6
import layer_60a5c91782ffc54caedc48a8 as layer_60a5c91782ffc54caedc48a8
import layer_60a5c91782ffc54caedc48aa as layer_60a5c91782ffc54caedc48aa
import layer_60a5c91782ffc54caedc48ac as layer_60a5c91782ffc54caedc48ac
import layer_60a5c91782ffc54caedc48ae as layer_60a5c91782ffc54caedc48ae
import layer_60a5c91782ffc54caedc48b5 as layer_60a5c91782ffc54caedc48b5
import layer_60a5c91782ffc54caedc48c7 as layer_60a5c91782ffc54caedc48c7
import layer_60a5c91782ffc54caedc48b7 as layer_60a5c91782ffc54caedc48b7
import layer_60a5c91782ffc54caedc48b9 as layer_60a5c91782ffc54caedc48b9
import layer_60a5c91782ffc54caedc48bb as layer_60a5c91782ffc54caedc48bb
import layer_60a5c91782ffc54caedc48bd as layer_60a5c91782ffc54caedc48bd
import layer_60a5c91782ffc54caedc48bf as layer_60a5c91782ffc54caedc48bf
import layer_60a5c91782ffc54caedc48c1 as layer_60a5c91782ffc54caedc48c1
import layer_60a5c91782ffc54caedc48c3 as layer_60a5c91782ffc54caedc48c3
import layer_60a5c91782ffc54caedc48c5 as layer_60a5c91782ffc54caedc48c5
import layer_60a5c91782ffc54caedc48cc as layer_60a5c91782ffc54caedc48cc
import layer_60a5c91782ffc54caedc48de as layer_60a5c91782ffc54caedc48de
import layer_60a5c91782ffc54caedc48ce as layer_60a5c91782ffc54caedc48ce
import layer_60a5c91782ffc54caedc48d0 as layer_60a5c91782ffc54caedc48d0
import layer_60a5c91782ffc54caedc48d2 as layer_60a5c91782ffc54caedc48d2
import layer_60a5c91782ffc54caedc48d4 as layer_60a5c91782ffc54caedc48d4
import layer_60a5c91782ffc54caedc48d6 as layer_60a5c91782ffc54caedc48d6
import layer_60a5c91782ffc54caedc48d8 as layer_60a5c91782ffc54caedc48d8
import layer_60a5c91782ffc54caedc48da as layer_60a5c91782ffc54caedc48da
import layer_60a5c91782ffc54caedc48dc as layer_60a5c91782ffc54caedc48dc
import layer_60a5c91782ffc54caedc48e3 as layer_60a5c91782ffc54caedc48e3
import layer_60a5c91782ffc54caedc48f5 as layer_60a5c91782ffc54caedc48f5
import layer_60a5c91782ffc54caedc48e5 as layer_60a5c91782ffc54caedc48e5
import layer_60a5c91782ffc54caedc48e7 as layer_60a5c91782ffc54caedc48e7
import layer_60a5c91782ffc54caedc48e9 as layer_60a5c91782ffc54caedc48e9
import layer_60a5c91782ffc54caedc48eb as layer_60a5c91782ffc54caedc48eb
import layer_60a5c91782ffc54caedc48ed as layer_60a5c91782ffc54caedc48ed
import layer_60a5c91782ffc54caedc48ef as layer_60a5c91782ffc54caedc48ef
import layer_60a5c91782ffc54caedc48f1 as layer_60a5c91782ffc54caedc48f1
import layer_60a5c91782ffc54caedc48f3 as layer_60a5c91782ffc54caedc48f3
import layer_60a5c91782ffc54caedc48fa as layer_60a5c91782ffc54caedc48fa
import layer_60a5c91782ffc54caedc490c as layer_60a5c91782ffc54caedc490c
import layer_60a5c91782ffc54caedc48fc as layer_60a5c91782ffc54caedc48fc
import layer_60a5c91782ffc54caedc48fe as layer_60a5c91782ffc54caedc48fe
import layer_60a5c91782ffc54caedc4900 as layer_60a5c91782ffc54caedc4900
import layer_60a5c91782ffc54caedc4902 as layer_60a5c91782ffc54caedc4902
import layer_60a5c91782ffc54caedc4904 as layer_60a5c91782ffc54caedc4904
import layer_60a5c91782ffc54caedc4906 as layer_60a5c91782ffc54caedc4906
import layer_60a5c91782ffc54caedc4908 as layer_60a5c91782ffc54caedc4908
import layer_60a5c91782ffc54caedc490a as layer_60a5c91782ffc54caedc490a
import layer_60a5c91782ffc54caedc4911 as layer_60a5c91782ffc54caedc4911
import layer_60a5c91782ffc54caedc4923 as layer_60a5c91782ffc54caedc4923
import layer_60a5c91782ffc54caedc4913 as layer_60a5c91782ffc54caedc4913
import layer_60a5c91782ffc54caedc4915 as layer_60a5c91782ffc54caedc4915
import layer_60a5c91782ffc54caedc4917 as layer_60a5c91782ffc54caedc4917
import layer_60a5c91782ffc54caedc4919 as layer_60a5c91782ffc54caedc4919
import layer_60a5c91782ffc54caedc491b as layer_60a5c91782ffc54caedc491b
import layer_60a5c91782ffc54caedc491d as layer_60a5c91782ffc54caedc491d
import layer_60a5c91782ffc54caedc491f as layer_60a5c91782ffc54caedc491f
import layer_60a5c91782ffc54caedc4921 as layer_60a5c91782ffc54caedc4921
import layer_60a5c91782ffc54caedc4928 as layer_60a5c91782ffc54caedc4928
import layer_60a5c91782ffc54caedc493a as layer_60a5c91782ffc54caedc493a
import layer_60a5c91782ffc54caedc492a as layer_60a5c91782ffc54caedc492a
import layer_60a5c91782ffc54caedc492c as layer_60a5c91782ffc54caedc492c
import layer_60a5c91782ffc54caedc492e as layer_60a5c91782ffc54caedc492e
import layer_60a5c91782ffc54caedc4930 as layer_60a5c91782ffc54caedc4930
import layer_60a5c91782ffc54caedc4932 as layer_60a5c91782ffc54caedc4932
import layer_60a5c91782ffc54caedc4934 as layer_60a5c91782ffc54caedc4934
import layer_60a5c91782ffc54caedc4936 as layer_60a5c91782ffc54caedc4936
import layer_60a5c91782ffc54caedc4938 as layer_60a5c91782ffc54caedc4938
import layer_60a5c91782ffc54caedc493f as layer_60a5c91782ffc54caedc493f
import layer_60a5c91782ffc54caedc4951 as layer_60a5c91782ffc54caedc4951
import layer_60a5c91782ffc54caedc4941 as layer_60a5c91782ffc54caedc4941
import layer_60a5c91782ffc54caedc4943 as layer_60a5c91782ffc54caedc4943
import layer_60a5c91782ffc54caedc4945 as layer_60a5c91782ffc54caedc4945
import layer_60a5c91782ffc54caedc4947 as layer_60a5c91782ffc54caedc4947
import layer_60a5c91782ffc54caedc4949 as layer_60a5c91782ffc54caedc4949
import layer_60a5c91782ffc54caedc494b as layer_60a5c91782ffc54caedc494b
import layer_60a5c91782ffc54caedc494d as layer_60a5c91782ffc54caedc494d
import layer_60a5c91782ffc54caedc494f as layer_60a5c91782ffc54caedc494f
import layer_60a5c91782ffc54caedc4956 as layer_60a5c91782ffc54caedc4956
import layer_60a5c91782ffc54caedc4958 as layer_60a5c91782ffc54caedc4958
import layer_60a5c91782ffc54caedc495a as layer_60a5c91782ffc54caedc495a
import layer_60a5c91782ffc54caedc495c as layer_60a5c91782ffc54caedc495c
import layer_60a5c91782ffc54caedc495e as layer_60a5c91782ffc54caedc495e
import layer_60a5c91782ffc54caedc4960 as layer_60a5c91782ffc54caedc4960
import layer_60a5c91782ffc54caedc4962 as layer_60a5c91782ffc54caedc4962
import layer_60a5c91782ffc54caedc4964 as layer_60a5c91782ffc54caedc4964
import layer_60a5c91782ffc54caedc4966 as layer_60a5c91782ffc54caedc4966
import layer_60a5c91782ffc54caedc4968 as layer_60a5c91782ffc54caedc4968
import layer_60a5c91782ffc54caedc496d as layer_60a5c91782ffc54caedc496d
import layer_60a5c91782ffc54caedc496f as layer_60a5c91782ffc54caedc496f
import layer_60a5c91782ffc54caedc4971 as layer_60a5c91782ffc54caedc4971
import layer_60a5c91782ffc54caedc4973 as layer_60a5c91782ffc54caedc4973
import layer_60a5c91782ffc54caedc4975 as layer_60a5c91782ffc54caedc4975
import layer_60a5c91782ffc54caedc4977 as layer_60a5c91782ffc54caedc4977
import layer_60a5c91782ffc54caedc4979 as layer_60a5c91782ffc54caedc4979
import layer_60a5c91782ffc54caedc497b as layer_60a5c91782ffc54caedc497b
import layer_60a5c91782ffc54caedc497f as layer_60a5c91782ffc54caedc497f
import layer_60a5c91782ffc54caedc4847 as layer_60a5c91782ffc54caedc4847
import layer_60a5c91782ffc54caedc484b as layer_60a5c91782ffc54caedc484b
import layer_60a5c91782ffc54caedc4849 as layer_60a5c91782ffc54caedc4849


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

        n1_Image = layer_60a5c91782ffc54caedc4845.Image(shape=[256, 256, 1])
        n2_Backbone_n1_block1_n1_Conv2D = layer_60a5c91782ffc54caedc484f.Conv2D(filters=32, kernel_size=[3, 3], strides=[2, 2], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n1_Image)
        n2_Backbone_n1_block1_n2_BatchNormalization = layer_60a5c91782ffc54caedc4851.BatchNormalization()(n2_Backbone_n1_block1_n1_Conv2D)
        n2_Backbone_n1_block1_n3_Activation = layer_60a5c91782ffc54caedc4853.Activation(activation='relu')(n2_Backbone_n1_block1_n2_BatchNormalization)
        n2_Backbone_n1_block1_n4_Conv2D = layer_60a5c91782ffc54caedc4855.Conv2D(filters=64, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n1_block1_n3_Activation)
        n2_Backbone_n1_block1_n5_BatchNormalization = layer_60a5c91782ffc54caedc4857.BatchNormalization()(n2_Backbone_n1_block1_n4_Conv2D)
        n2_Backbone_n1_block1_n6_Activation = layer_60a5c91782ffc54caedc4859.Activation(activation='relu')(n2_Backbone_n1_block1_n5_BatchNormalization)
        n2_Backbone_n2_Conv2D = layer_60a5c91782ffc54caedc485d.Conv2D(filters=128, kernel_size=[1, 1], strides=[2, 2], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n1_block1_n6_Activation)
        n2_Backbone_n3_BatchNormalization = layer_60a5c91782ffc54caedc485f.BatchNormalization()(n2_Backbone_n2_Conv2D)
        n2_Backbone_n4_block2_n1_SeparableConv2D = layer_60a5c91782ffc54caedc4861.SeparableConv2D(filters=128, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n1_block1_n6_Activation)
        n2_Backbone_n4_block2_n2_BatchNormalization = layer_60a5c91782ffc54caedc4863.BatchNormalization()(n2_Backbone_n4_block2_n1_SeparableConv2D)
        n2_Backbone_n4_block2_n3_Activation = layer_60a5c91782ffc54caedc4865.Activation(activation='relu')(n2_Backbone_n4_block2_n2_BatchNormalization)
        n2_Backbone_n4_block2_n4_SeparableConv2D = layer_60a5c91782ffc54caedc4867.SeparableConv2D(filters=128, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n4_block2_n3_Activation)
        n2_Backbone_n4_block2_n5_BatchNormalization = layer_60a5c91782ffc54caedc4869.BatchNormalization()(n2_Backbone_n4_block2_n4_SeparableConv2D)
        n2_Backbone_n4_block2_n6_MaxPooling2D = layer_60a5c91782ffc54caedc486b.MaxPooling2D(pool_size=[3, 3], strides=[2, 2], padding='same')(n2_Backbone_n4_block2_n5_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc4870.Add().call).args)
        if num_args == 2:
            n2_Backbone_n5_Add = layer_60a5c91782ffc54caedc4870.Add()([n2_Backbone_n3_BatchNormalization, n2_Backbone_n4_block2_n6_MaxPooling2D])
        else:
            n2_Backbone_n5_Add = layer_60a5c91782ffc54caedc4870.Add()(*[n2_Backbone_n3_BatchNormalization, n2_Backbone_n4_block2_n6_MaxPooling2D])
        n2_Backbone_n6_Activation = layer_60a5c91782ffc54caedc4872.Activation(activation='relu')(n2_Backbone_n5_Add)
        n2_Backbone_n7_Conv2D = layer_60a5c91782ffc54caedc4874.Conv2D(filters=256, kernel_size=[1, 1], strides=[2, 2], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n6_Activation)
        n2_Backbone_n8_BatchNormalization = layer_60a5c91782ffc54caedc4876.BatchNormalization()(n2_Backbone_n7_Conv2D)
        n2_Backbone_n9_block2_n1_SeparableConv2D = layer_60a5c91782ffc54caedc4878.SeparableConv2D(filters=256, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n6_Activation)
        n2_Backbone_n9_block2_n2_BatchNormalization = layer_60a5c91782ffc54caedc487a.BatchNormalization()(n2_Backbone_n9_block2_n1_SeparableConv2D)
        n2_Backbone_n9_block2_n3_Activation = layer_60a5c91782ffc54caedc487c.Activation(activation='relu')(n2_Backbone_n9_block2_n2_BatchNormalization)
        n2_Backbone_n9_block2_n4_SeparableConv2D = layer_60a5c91782ffc54caedc487e.SeparableConv2D(filters=256, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n9_block2_n3_Activation)
        n2_Backbone_n9_block2_n5_BatchNormalization = layer_60a5c91782ffc54caedc4880.BatchNormalization()(n2_Backbone_n9_block2_n4_SeparableConv2D)
        n2_Backbone_n9_block2_n6_MaxPooling2D = layer_60a5c91782ffc54caedc4882.MaxPooling2D(pool_size=[3, 3], strides=[2, 2], padding='same')(n2_Backbone_n9_block2_n5_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc4887.Add().call).args)
        if num_args == 2:
            n2_Backbone_n10_Add = layer_60a5c91782ffc54caedc4887.Add()([n2_Backbone_n8_BatchNormalization, n2_Backbone_n9_block2_n6_MaxPooling2D])
        else:
            n2_Backbone_n10_Add = layer_60a5c91782ffc54caedc4887.Add()(*[n2_Backbone_n8_BatchNormalization, n2_Backbone_n9_block2_n6_MaxPooling2D])
        n2_Backbone_n11_Activation = layer_60a5c91782ffc54caedc4889.Activation(activation='relu')(n2_Backbone_n10_Add)
        n2_Backbone_n12_Conv2D = layer_60a5c91782ffc54caedc488b.Conv2D(filters=728, kernel_size=[1, 1], strides=[2, 2], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n11_Activation)
        n2_Backbone_n13_BatchNormalization = layer_60a5c91782ffc54caedc488d.BatchNormalization()(n2_Backbone_n12_Conv2D)
        n2_Backbone_n14_block2_n1_SeparableConv2D = layer_60a5c91782ffc54caedc488f.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n10_Add)
        n2_Backbone_n14_block2_n2_BatchNormalization = layer_60a5c91782ffc54caedc4891.BatchNormalization()(n2_Backbone_n14_block2_n1_SeparableConv2D)
        n2_Backbone_n14_block2_n3_Activation = layer_60a5c91782ffc54caedc4893.Activation(activation='relu')(n2_Backbone_n14_block2_n2_BatchNormalization)
        n2_Backbone_n14_block2_n4_SeparableConv2D = layer_60a5c91782ffc54caedc4895.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n14_block2_n3_Activation)
        n2_Backbone_n14_block2_n5_BatchNormalization = layer_60a5c91782ffc54caedc4897.BatchNormalization()(n2_Backbone_n14_block2_n4_SeparableConv2D)
        n2_Backbone_n14_block2_n6_MaxPooling2D = layer_60a5c91782ffc54caedc4899.MaxPooling2D(pool_size=[3, 3], strides=[2, 2], padding='same')(n2_Backbone_n14_block2_n5_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc489e.Add().call).args)
        if num_args == 2:
            n2_Backbone_n15_Add = layer_60a5c91782ffc54caedc489e.Add()([n2_Backbone_n13_BatchNormalization, n2_Backbone_n14_block2_n6_MaxPooling2D])
        else:
            n2_Backbone_n15_Add = layer_60a5c91782ffc54caedc489e.Add()(*[n2_Backbone_n13_BatchNormalization, n2_Backbone_n14_block2_n6_MaxPooling2D])
        n2_Backbone_n16_block3_n9_Activation = layer_60a5c91782ffc54caedc48b0.Activation(activation='relu')(n2_Backbone_n15_Add)
        n2_Backbone_n16_block3_n1_SeparableConv2D = layer_60a5c91782ffc54caedc48a0.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n16_block3_n9_Activation)
        n2_Backbone_n16_block3_n2_BatchNormalization = layer_60a5c91782ffc54caedc48a2.BatchNormalization()(n2_Backbone_n16_block3_n1_SeparableConv2D)
        n2_Backbone_n16_block3_n3_Activation = layer_60a5c91782ffc54caedc48a4.Activation(activation='relu')(n2_Backbone_n16_block3_n2_BatchNormalization)
        n2_Backbone_n16_block3_n4_SeparableConv2D = layer_60a5c91782ffc54caedc48a6.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n16_block3_n3_Activation)
        n2_Backbone_n16_block3_n5_BatchNormalization = layer_60a5c91782ffc54caedc48a8.BatchNormalization()(n2_Backbone_n16_block3_n4_SeparableConv2D)
        n2_Backbone_n16_block3_n6_Activation = layer_60a5c91782ffc54caedc48aa.Activation(activation='relu')(n2_Backbone_n16_block3_n5_BatchNormalization)
        n2_Backbone_n16_block3_n7_SeparableConv2D = layer_60a5c91782ffc54caedc48ac.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n16_block3_n6_Activation)
        n2_Backbone_n16_block3_n8_BatchNormalization = layer_60a5c91782ffc54caedc48ae.BatchNormalization()(n2_Backbone_n16_block3_n7_SeparableConv2D)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc48b5.Add().call).args)
        if num_args == 2:
            n2_Backbone_n17_Add = layer_60a5c91782ffc54caedc48b5.Add()([n2_Backbone_n15_Add, n2_Backbone_n16_block3_n8_BatchNormalization])
        else:
            n2_Backbone_n17_Add = layer_60a5c91782ffc54caedc48b5.Add()(*[n2_Backbone_n15_Add, n2_Backbone_n16_block3_n8_BatchNormalization])
        n2_Backbone_n18_block3_n9_Activation = layer_60a5c91782ffc54caedc48c7.Activation(activation='relu')(n2_Backbone_n17_Add)
        n2_Backbone_n18_block3_n1_SeparableConv2D = layer_60a5c91782ffc54caedc48b7.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n18_block3_n9_Activation)
        n2_Backbone_n18_block3_n2_BatchNormalization = layer_60a5c91782ffc54caedc48b9.BatchNormalization()(n2_Backbone_n18_block3_n1_SeparableConv2D)
        n2_Backbone_n18_block3_n3_Activation = layer_60a5c91782ffc54caedc48bb.Activation(activation='relu')(n2_Backbone_n18_block3_n2_BatchNormalization)
        n2_Backbone_n18_block3_n4_SeparableConv2D = layer_60a5c91782ffc54caedc48bd.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n18_block3_n3_Activation)
        n2_Backbone_n18_block3_n5_BatchNormalization = layer_60a5c91782ffc54caedc48bf.BatchNormalization()(n2_Backbone_n18_block3_n4_SeparableConv2D)
        n2_Backbone_n18_block3_n6_Activation = layer_60a5c91782ffc54caedc48c1.Activation(activation='relu')(n2_Backbone_n18_block3_n5_BatchNormalization)
        n2_Backbone_n18_block3_n7_SeparableConv2D = layer_60a5c91782ffc54caedc48c3.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n18_block3_n6_Activation)
        n2_Backbone_n18_block3_n8_BatchNormalization = layer_60a5c91782ffc54caedc48c5.BatchNormalization()(n2_Backbone_n18_block3_n7_SeparableConv2D)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc48cc.Add().call).args)
        if num_args == 2:
            n2_Backbone_n19_Add = layer_60a5c91782ffc54caedc48cc.Add()([n2_Backbone_n17_Add, n2_Backbone_n18_block3_n8_BatchNormalization])
        else:
            n2_Backbone_n19_Add = layer_60a5c91782ffc54caedc48cc.Add()(*[n2_Backbone_n17_Add, n2_Backbone_n18_block3_n8_BatchNormalization])
        n2_Backbone_n20_block3_n9_Activation = layer_60a5c91782ffc54caedc48de.Activation(activation='relu')(n2_Backbone_n19_Add)
        n2_Backbone_n20_block3_n1_SeparableConv2D = layer_60a5c91782ffc54caedc48ce.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n20_block3_n9_Activation)
        n2_Backbone_n20_block3_n2_BatchNormalization = layer_60a5c91782ffc54caedc48d0.BatchNormalization()(n2_Backbone_n20_block3_n1_SeparableConv2D)
        n2_Backbone_n20_block3_n3_Activation = layer_60a5c91782ffc54caedc48d2.Activation(activation='relu')(n2_Backbone_n20_block3_n2_BatchNormalization)
        n2_Backbone_n20_block3_n4_SeparableConv2D = layer_60a5c91782ffc54caedc48d4.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n20_block3_n3_Activation)
        n2_Backbone_n20_block3_n5_BatchNormalization = layer_60a5c91782ffc54caedc48d6.BatchNormalization()(n2_Backbone_n20_block3_n4_SeparableConv2D)
        n2_Backbone_n20_block3_n6_Activation = layer_60a5c91782ffc54caedc48d8.Activation(activation='relu')(n2_Backbone_n20_block3_n5_BatchNormalization)
        n2_Backbone_n20_block3_n7_SeparableConv2D = layer_60a5c91782ffc54caedc48da.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n20_block3_n6_Activation)
        n2_Backbone_n20_block3_n8_BatchNormalization = layer_60a5c91782ffc54caedc48dc.BatchNormalization()(n2_Backbone_n20_block3_n7_SeparableConv2D)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc48e3.Add().call).args)
        if num_args == 2:
            n2_Backbone_n21_Add = layer_60a5c91782ffc54caedc48e3.Add()([n2_Backbone_n19_Add, n2_Backbone_n20_block3_n8_BatchNormalization])
        else:
            n2_Backbone_n21_Add = layer_60a5c91782ffc54caedc48e3.Add()(*[n2_Backbone_n19_Add, n2_Backbone_n20_block3_n8_BatchNormalization])
        n2_Backbone_n22_block3_n9_Activation = layer_60a5c91782ffc54caedc48f5.Activation(activation='relu')(n2_Backbone_n21_Add)
        n2_Backbone_n22_block3_n1_SeparableConv2D = layer_60a5c91782ffc54caedc48e5.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n22_block3_n9_Activation)
        n2_Backbone_n22_block3_n2_BatchNormalization = layer_60a5c91782ffc54caedc48e7.BatchNormalization()(n2_Backbone_n22_block3_n1_SeparableConv2D)
        n2_Backbone_n22_block3_n3_Activation = layer_60a5c91782ffc54caedc48e9.Activation(activation='relu')(n2_Backbone_n22_block3_n2_BatchNormalization)
        n2_Backbone_n22_block3_n4_SeparableConv2D = layer_60a5c91782ffc54caedc48eb.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n22_block3_n3_Activation)
        n2_Backbone_n22_block3_n5_BatchNormalization = layer_60a5c91782ffc54caedc48ed.BatchNormalization()(n2_Backbone_n22_block3_n4_SeparableConv2D)
        n2_Backbone_n22_block3_n6_Activation = layer_60a5c91782ffc54caedc48ef.Activation(activation='relu')(n2_Backbone_n22_block3_n5_BatchNormalization)
        n2_Backbone_n22_block3_n7_SeparableConv2D = layer_60a5c91782ffc54caedc48f1.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n22_block3_n6_Activation)
        n2_Backbone_n22_block3_n8_BatchNormalization = layer_60a5c91782ffc54caedc48f3.BatchNormalization()(n2_Backbone_n22_block3_n7_SeparableConv2D)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc48fa.Add().call).args)
        if num_args == 2:
            n2_Backbone_n23_Add = layer_60a5c91782ffc54caedc48fa.Add()([n2_Backbone_n21_Add, n2_Backbone_n22_block3_n8_BatchNormalization])
        else:
            n2_Backbone_n23_Add = layer_60a5c91782ffc54caedc48fa.Add()(*[n2_Backbone_n21_Add, n2_Backbone_n22_block3_n8_BatchNormalization])
        n2_Backbone_n24_block3_n9_Activation = layer_60a5c91782ffc54caedc490c.Activation(activation='relu')(n2_Backbone_n23_Add)
        n2_Backbone_n24_block3_n1_SeparableConv2D = layer_60a5c91782ffc54caedc48fc.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n24_block3_n9_Activation)
        n2_Backbone_n24_block3_n2_BatchNormalization = layer_60a5c91782ffc54caedc48fe.BatchNormalization()(n2_Backbone_n24_block3_n1_SeparableConv2D)
        n2_Backbone_n24_block3_n3_Activation = layer_60a5c91782ffc54caedc4900.Activation(activation='relu')(n2_Backbone_n24_block3_n2_BatchNormalization)
        n2_Backbone_n24_block3_n4_SeparableConv2D = layer_60a5c91782ffc54caedc4902.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n24_block3_n3_Activation)
        n2_Backbone_n24_block3_n5_BatchNormalization = layer_60a5c91782ffc54caedc4904.BatchNormalization()(n2_Backbone_n24_block3_n4_SeparableConv2D)
        n2_Backbone_n24_block3_n6_Activation = layer_60a5c91782ffc54caedc4906.Activation(activation='relu')(n2_Backbone_n24_block3_n5_BatchNormalization)
        n2_Backbone_n24_block3_n7_SeparableConv2D = layer_60a5c91782ffc54caedc4908.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n24_block3_n6_Activation)
        n2_Backbone_n24_block3_n8_BatchNormalization = layer_60a5c91782ffc54caedc490a.BatchNormalization()(n2_Backbone_n24_block3_n7_SeparableConv2D)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc4911.Add().call).args)
        if num_args == 2:
            n2_Backbone_n25_Add = layer_60a5c91782ffc54caedc4911.Add()([n2_Backbone_n23_Add, n2_Backbone_n24_block3_n8_BatchNormalization])
        else:
            n2_Backbone_n25_Add = layer_60a5c91782ffc54caedc4911.Add()(*[n2_Backbone_n23_Add, n2_Backbone_n24_block3_n8_BatchNormalization])
        n2_Backbone_n26_block3_n9_Activation = layer_60a5c91782ffc54caedc4923.Activation(activation='relu')(n2_Backbone_n25_Add)
        n2_Backbone_n26_block3_n1_SeparableConv2D = layer_60a5c91782ffc54caedc4913.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n26_block3_n9_Activation)
        n2_Backbone_n26_block3_n2_BatchNormalization = layer_60a5c91782ffc54caedc4915.BatchNormalization()(n2_Backbone_n26_block3_n1_SeparableConv2D)
        n2_Backbone_n26_block3_n3_Activation = layer_60a5c91782ffc54caedc4917.Activation(activation='relu')(n2_Backbone_n26_block3_n2_BatchNormalization)
        n2_Backbone_n26_block3_n4_SeparableConv2D = layer_60a5c91782ffc54caedc4919.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n26_block3_n3_Activation)
        n2_Backbone_n26_block3_n5_BatchNormalization = layer_60a5c91782ffc54caedc491b.BatchNormalization()(n2_Backbone_n26_block3_n4_SeparableConv2D)
        n2_Backbone_n26_block3_n6_Activation = layer_60a5c91782ffc54caedc491d.Activation(activation='relu')(n2_Backbone_n26_block3_n5_BatchNormalization)
        n2_Backbone_n26_block3_n7_SeparableConv2D = layer_60a5c91782ffc54caedc491f.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n26_block3_n6_Activation)
        n2_Backbone_n26_block3_n8_BatchNormalization = layer_60a5c91782ffc54caedc4921.BatchNormalization()(n2_Backbone_n26_block3_n7_SeparableConv2D)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc4928.Add().call).args)
        if num_args == 2:
            n2_Backbone_n27_Add = layer_60a5c91782ffc54caedc4928.Add()([n2_Backbone_n25_Add, n2_Backbone_n26_block3_n8_BatchNormalization])
        else:
            n2_Backbone_n27_Add = layer_60a5c91782ffc54caedc4928.Add()(*[n2_Backbone_n25_Add, n2_Backbone_n26_block3_n8_BatchNormalization])
        n2_Backbone_n28_block3_n9_Activation = layer_60a5c91782ffc54caedc493a.Activation(activation='relu')(n2_Backbone_n27_Add)
        n2_Backbone_n28_block3_n1_SeparableConv2D = layer_60a5c91782ffc54caedc492a.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n28_block3_n9_Activation)
        n2_Backbone_n28_block3_n2_BatchNormalization = layer_60a5c91782ffc54caedc492c.BatchNormalization()(n2_Backbone_n28_block3_n1_SeparableConv2D)
        n2_Backbone_n28_block3_n3_Activation = layer_60a5c91782ffc54caedc492e.Activation(activation='relu')(n2_Backbone_n28_block3_n2_BatchNormalization)
        n2_Backbone_n28_block3_n4_SeparableConv2D = layer_60a5c91782ffc54caedc4930.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n28_block3_n3_Activation)
        n2_Backbone_n28_block3_n5_BatchNormalization = layer_60a5c91782ffc54caedc4932.BatchNormalization()(n2_Backbone_n28_block3_n4_SeparableConv2D)
        n2_Backbone_n28_block3_n6_Activation = layer_60a5c91782ffc54caedc4934.Activation(activation='relu')(n2_Backbone_n28_block3_n5_BatchNormalization)
        n2_Backbone_n28_block3_n7_SeparableConv2D = layer_60a5c91782ffc54caedc4936.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n28_block3_n6_Activation)
        n2_Backbone_n28_block3_n8_BatchNormalization = layer_60a5c91782ffc54caedc4938.BatchNormalization()(n2_Backbone_n28_block3_n7_SeparableConv2D)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc493f.Add().call).args)
        if num_args == 2:
            n2_Backbone_n29_Add = layer_60a5c91782ffc54caedc493f.Add()([n2_Backbone_n27_Add, n2_Backbone_n28_block3_n8_BatchNormalization])
        else:
            n2_Backbone_n29_Add = layer_60a5c91782ffc54caedc493f.Add()(*[n2_Backbone_n27_Add, n2_Backbone_n28_block3_n8_BatchNormalization])
        n2_Backbone_n30_block3_n9_Activation = layer_60a5c91782ffc54caedc4951.Activation(activation='relu')(n2_Backbone_n29_Add)
        n2_Backbone_n30_block3_n1_SeparableConv2D = layer_60a5c91782ffc54caedc4941.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n30_block3_n9_Activation)
        n2_Backbone_n30_block3_n2_BatchNormalization = layer_60a5c91782ffc54caedc4943.BatchNormalization()(n2_Backbone_n30_block3_n1_SeparableConv2D)
        n2_Backbone_n30_block3_n3_Activation = layer_60a5c91782ffc54caedc4945.Activation(activation='relu')(n2_Backbone_n30_block3_n2_BatchNormalization)
        n2_Backbone_n30_block3_n4_SeparableConv2D = layer_60a5c91782ffc54caedc4947.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n30_block3_n3_Activation)
        n2_Backbone_n30_block3_n5_BatchNormalization = layer_60a5c91782ffc54caedc4949.BatchNormalization()(n2_Backbone_n30_block3_n4_SeparableConv2D)
        n2_Backbone_n30_block3_n6_Activation = layer_60a5c91782ffc54caedc494b.Activation(activation='relu')(n2_Backbone_n30_block3_n5_BatchNormalization)
        n2_Backbone_n30_block3_n7_SeparableConv2D = layer_60a5c91782ffc54caedc494d.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n30_block3_n6_Activation)
        n2_Backbone_n30_block3_n8_BatchNormalization = layer_60a5c91782ffc54caedc494f.BatchNormalization()(n2_Backbone_n30_block3_n7_SeparableConv2D)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc4956.Add().call).args)
        if num_args == 2:
            n2_Backbone_n31_Add = layer_60a5c91782ffc54caedc4956.Add()([n2_Backbone_n29_Add, n2_Backbone_n30_block3_n8_BatchNormalization])
        else:
            n2_Backbone_n31_Add = layer_60a5c91782ffc54caedc4956.Add()(*[n2_Backbone_n29_Add, n2_Backbone_n30_block3_n8_BatchNormalization])
        n2_Backbone_n32_Conv2D = layer_60a5c91782ffc54caedc4958.Conv2D(filters=1024, kernel_size=[1, 1], strides=[2, 2], padding='same', dilation_rate=[1, 1], activation=None, use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n2_Backbone_n31_Add)
        n2_Backbone_n33_BatchNormalization = layer_60a5c91782ffc54caedc495a.BatchNormalization()(n2_Backbone_n32_Conv2D)
        n2_Backbone_n34_block4_n1_Activation = layer_60a5c91782ffc54caedc495c.Activation(activation='relu')(n2_Backbone_n31_Add)
        n2_Backbone_n34_block4_n2_SeparableConv2D = layer_60a5c91782ffc54caedc495e.SeparableConv2D(filters=728, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n34_block4_n1_Activation)
        n2_Backbone_n34_block4_n3_BatchNormalization = layer_60a5c91782ffc54caedc4960.BatchNormalization()(n2_Backbone_n34_block4_n2_SeparableConv2D)
        n2_Backbone_n34_block4_n4_Activation = layer_60a5c91782ffc54caedc4962.Activation(activation='relu')(n2_Backbone_n34_block4_n3_BatchNormalization)
        n2_Backbone_n34_block4_n5_SeparableConv2D = layer_60a5c91782ffc54caedc4964.SeparableConv2D(filters=1024, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n34_block4_n4_Activation)
        n2_Backbone_n34_block4_n6_BatchNormalization = layer_60a5c91782ffc54caedc4966.BatchNormalization()(n2_Backbone_n34_block4_n5_SeparableConv2D)
        n2_Backbone_n34_block4_n7_MaxPooling2D = layer_60a5c91782ffc54caedc4968.MaxPooling2D(pool_size=[3, 3], strides=[2, 2], padding='same')(n2_Backbone_n34_block4_n6_BatchNormalization)
        num_args = len(inspect.getfullargspec(layer_60a5c91782ffc54caedc496d.Add().call).args)
        if num_args == 2:
            n2_Backbone_n35_Add = layer_60a5c91782ffc54caedc496d.Add()([n2_Backbone_n33_BatchNormalization, n2_Backbone_n34_block4_n7_MaxPooling2D])
        else:
            n2_Backbone_n35_Add = layer_60a5c91782ffc54caedc496d.Add()(*[n2_Backbone_n33_BatchNormalization, n2_Backbone_n34_block4_n7_MaxPooling2D])
        n2_Backbone_n36_block4_n1_Activation = layer_60a5c91782ffc54caedc496f.Activation(activation='relu')(n2_Backbone_n35_Add)
        n2_Backbone_n36_block4_n2_SeparableConv2D = layer_60a5c91782ffc54caedc4971.SeparableConv2D(filters=1536, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n36_block4_n1_Activation)
        n2_Backbone_n36_block4_n3_BatchNormalization = layer_60a5c91782ffc54caedc4973.BatchNormalization()(n2_Backbone_n36_block4_n2_SeparableConv2D)
        n2_Backbone_n36_block4_n4_Activation = layer_60a5c91782ffc54caedc4975.Activation(activation='relu')(n2_Backbone_n36_block4_n3_BatchNormalization)
        n2_Backbone_n36_block4_n5_SeparableConv2D = layer_60a5c91782ffc54caedc4977.SeparableConv2D(filters=2048, kernel_size=[3, 3], strides=[1, 1], padding='same', dilation_rate=[1, 1], depth_multiplier=1, activation=None, use_bias=False, depthwise_initializer='glorot_uniform', pointwise_initializer='glorot_uniform', bias_initializer='Zeros', depthwise_regularizer=None, pointwise_regularizer=None, bias_regularizer=None, activity_regularizer=None, depthwise_constraint=None, pointwise_constraint=None, bias_constraint=None)(n2_Backbone_n36_block4_n4_Activation)
        n2_Backbone_n36_block4_n6_BatchNormalization = layer_60a5c91782ffc54caedc4979.BatchNormalization()(n2_Backbone_n36_block4_n5_SeparableConv2D)
        n2_Backbone_n36_block4_n7_MaxPooling2D = layer_60a5c91782ffc54caedc497b.MaxPooling2D(pool_size=[3, 3], strides=[2, 2], padding='same')(n2_Backbone_n36_block4_n6_BatchNormalization)
        n2_Backbone_n37_Activation = layer_60a5c91782ffc54caedc497f.Activation(activation='relu')(n2_Backbone_n36_block4_n7_MaxPooling2D)
        n3_GlobalAveragePooling2D = layer_60a5c91782ffc54caedc4847.GlobalAveragePooling2D()(n2_Backbone_n37_Activation)
        n9_Dropout = layer_60a5c91782ffc54caedc484b.Dropout(rate=0.5)(n3_GlobalAveragePooling2D)
        n4_Dense = layer_60a5c91782ffc54caedc4849.Dense(units=6, activation='softmax', use_bias=False, kernel_initializer='glorot_uniform', bias_initializer='Zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)(n9_Dropout)
        label = keras.layers.Input(shape=[6])
        loss = keras.losses.CategoricalCrossentropy()(label, n4_Dense)
        



        for key in list(config_loss.keys()):
            if len(config_loss[key]) == 1:
                config_loss[key] = config_loss[key][0]
            elif len(config_loss[key]) > 1:
                config_loss[key] = get_loss_sum_fn(config_loss[key])
            else:
                del config_loss[key]
        inputs = [n1_Image]
        outputs = [n4_Dense]
        losses = [loss]
        labels = [label]

        return inputs, outputs, losses, labels

