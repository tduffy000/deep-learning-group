Team Journal

<h3> April 26, 8pm.</h3>

- Sam and Jiffar did project touch base.
- We have data loaded into google drive in batches.
- We are going to do a convolution using tensorflow.
- We are reducing the number of labels to ten.
- We need to figure out the folder arrangement of the image files.

<h3> May 5 </h3>

<h4> Working pipeline </h4>
The basic working pipeline is now established for all team members. Those steps are:

- A local folder is synced with google drive.
- The git clone is then put in that local folder.
- That way, any change in the colab notebook on the drive is synced automatically with the local clone.
- Those changes can be commited, pushed, pulled, and merged with master branch without having to create additional copy.
- The dataset is also on each member personal's drive.
- Whenever we want to execute code in Colab, we just have to mount the notebook to our drive to access the data.

<h4> Train, test, validation data split </h4>
Previous, we were using the built-in `validation_split` in `ImageDataGenerator` to split the dataset. However, using this, we couldn't reserve a portion of the dataset to be used as test set. Tony then suggested that we should use `split_utils` to create pseudo directories for train and test set. This would allow us to have train, test, and validation sets separately. This was a great suggestion, and Sam will implement this this week.

<h4> Model development and evaluation toolkits </h4>
Currently, we have decided that can be called to plot model accuracy and model loss. However, we are currently still lacking a function to perform regression analysis to evaluate the model performance on the unseen/test data. We are also lacking a function that can accept user input image and classify it. Those are our goals for this week.

<h4> Baseline model's performance </h4>
We trained a simple CNN to classify 17 different yoga poses. The CNN had 2 `Conv2D` + `MaxPooling2D` layers followed by a `Flatten` layer and 2 `Dense` fully Connected layers, which had 128 and 17 nodes, respectively. `adam` was the optimizer, and `categorical crossentropy` was the loss function. The model achieved maximum `val_accuracy` of 60% within 10 epochs.
