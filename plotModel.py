import matplotlib.pyplot as plt

def plotModel(model_fit):
    acc = model_fit.history['accuracy']
    val_acc = model_fit.history['val_accuracy']
    loss = model_fit.history['loss']
    val_loss = model_fit.history['val_loss']

    epochs = range(1, len(acc) + 1)

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()

    plt.figure()

    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()

    return