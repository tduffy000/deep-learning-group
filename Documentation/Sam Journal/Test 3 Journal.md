<h2> Test 3 </h3>

Model name: Simple CNN

Model architecture:

![archi](/Documentations/Sam%20Journal/Images/Test_3_Archi.png)

Model result:

![graph](/Documentations/Sam%20Journal/Images/Test_3_Graph.png)

Compared to the previous model, this model had an even lower validation accuracy during the training process. However, this model employed a learning rate schedule to prevent the model from overfitting too early and from growing. The scheduler proved itself to be useful. Although it failed to prevent overfitting from happening, it successfully prevent overfitting to grow exponential as the training go on. As a result, the model was able to continue to train for about 40 epochs, a 2 times increased from the previous model (the early stop patience was doubled as well - so that might partly contribute to that). 

![metrics](/Documentations/Sam%20Journal/Images/Test_3_Metrics.png)

The metrics' changes compared to the previous model are dismissible. The recall rate for class 8 is really low. It means that our classifer for class 8 is really picky.

![confusion](/Documentations/Sam%20Journal/Images/Test_3_Confusion_Matrix.png)

Again, the confusion matrix remains largely unchange from the previous model. However, this time, because of the really high precision and low recall, class 8 had no wrong error, but it also missed a lot of its images.

Next steps:
- Try new, more complex architecture
- Add more dense layer along with dropout
- Play around with the new learning rate to make sure that overfitting is delayed as much as possible
- The goal is to bring the validation accuracy to above 50% consistently