
<h3> Test 5 </h3>

Model name: CNN with more complex architecture 2

Model architecture:

![archi](/Documentations/Sam%20Journal/Images/Test_5_Archi.png)

In this model, batch normalization layers were added after every convolutional layer to prevent the layers from overfitting. The patience period was also increased.

Model result:

![graph](/Documentations/Sam%20Journal/Images/Test_5_Graph.png)

From a glance, this model performance in training was horrific. The model test loss didn't seem to decrease at all while the train loss decreased smoothly. There were big differences between the accuracy of the train and test curves. This model was badly overfitted. However, was it garbage?

![metrics](/Documentations/Sam%20Journal/Images/Test_5_Metrics.png)

Short answer was no. This model achieved a much higher recall and precision values compared to the previous model. Was it the same situation as the first model. It might be or it might be not. This model was trained using smaller train set and larger test and validation set. Hence, the chance that this was an overfitting artifact is lower than the first model. Furthermore, the troublesome performance in identify class 8 images was resolved, for now!

![confusion](/Documentations/Sam%20Journal/Images/Test_5_Confusion_Matrix.png)
From the confusion matrix, we can see that the performance of this model on the test set was much better compared to the previous model. There are less random errors. Most of images from class 7 and 8 were correctly labeled. This was a huge step in the right direction by using the batch normalization to prevent overfitting.

Next steps:
- Try removing some convolutional layers and change the size of them
- Get even more aggressive with the regularlization to prevent overfitting.
- Might try to decrease batch size to see what will happen
- Increase learning rate but also increase the decaying speed.
- Start testing with transfer learning