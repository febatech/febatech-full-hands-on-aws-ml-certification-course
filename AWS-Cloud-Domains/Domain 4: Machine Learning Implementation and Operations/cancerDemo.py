import argparse, os
import numpy as np

import tensorflow

from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from tensorflow.keras.layers import Dense,Flatten,BatchNormalization,Dropout,Conv2D,MaxPooling2D,Activation,MaxPool2D
from tensorflow.keras.models import Model,Sequential
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import backend as K
from tensorflow.keras.utils import multi_gpu_model

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--gpu-count', type=int, default=os.environ['SM_NUM_GPUS'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--training', type=str, default=os.environ['SM_CHANNEL_TRAINING'])

    args, _ = parser.parse_known_args()

    epochs     = args.epochs
    gpu_count  = args.gpu_count
    model_dir  = args.model_dir
    training_dir   = args.training
    
    data_gen = ImageDataGenerator(
        preprocessing_function = preprocess_input,
        validation_split = 0.2
    )
    # Train(80%) and Validation(20%)
    train_data = data_gen.flow_from_directory(
        training_dir,
        target_size=(50,50),
        class_mode = 'binary',
        batch_size=2048,
        subset='training'
    )
    validation_data = data_gen.flow_from_directory(
        training_dir,
        target_size=(50,50),
        class_mode = 'binary',
        batch_size=256,
        subset='validation' 
    )
    
    print(train_data.class_indices)
    decay_lr = ReduceLROnPlateau(factor=0.001,patience=3,min_lr=0.000001)
    callbacks = [decay_lr]

    pretrained_model = ResNet50(include_top=False,weights='imagenet',input_shape=(50,50,3)) 
    for layer in pretrained_model.layers:
      layer.trainable = False
    x = pretrained_model.output
    x = Flatten()(x)
    x = Dense(1,activation='sigmoid')(x)
    model = Model(pretrained_model.input,x)

    if gpu_count > 1:
        model = multi_gpu_model(model, gpus=gpu_count)

    model.compile(optimizer='adam',metrics=['accuracy'],loss='binary_crossentropy')

    history = model.fit(x = train_data, epochs=epochs,validation_data = validation_data,callbacks=callbacks,verbose=2)

    score = model.evaluate(x=validation_data,verbose=0)
    print('Validation loss    :', score[0])
    print('Validation accuracy:', score[1])
    
    #save Keras model for Tensorflow Serving
    tensorflow.saved_model.save(
        model,
        os.path.join(model_dir, 'model/1'),
        )

