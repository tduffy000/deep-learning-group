from tensorflow.keras.preprocessing.image import ImageDataGenerator

def generatorTrainTest(data_DIR,
                        miniBatchSize=200,
                        colorMode='rgb',
                        classMode='categorical',
                        imgSize=64,
                        rotation_range=20,
                        width_shift_range=0.1,
                        height_shift_range=0.1,
                        rescale=1./255,
                        zoom_range=0.3,
                        validation_split=0.3,
                        horizontal_flip=True):

    datagen = ImageDataGenerator(rotation_range=rotation_range,
                                 width_shift_range=width_shift_range,
                                 height_shift_range=height_shift_range,
                                 rescale=rescale,
                                 zoom_range=zoom_range,
                                 validation_split=validation_split,
                                 horizontal_flip=horizontal_flip)
    
    train_generator = datagen.flow_from_directory(data_DIR,
                                                target_size=(imgSize, imgSize),
                                                color_mode=colorMode,
                                                class_mode=classMode,
                                                batch_size=miniBatchSize,
                                                subset='training')

    validation_generator = datagen.flow_from_directory(data_DIR,
                                                target_size=(imgSize, imgSize),
                                                color_mode=colorMode,
                                                class_mode=classMode,
                                                batch_size=miniBatchSize,
                                                subset='validation')

    return train_generator, validation_generator

