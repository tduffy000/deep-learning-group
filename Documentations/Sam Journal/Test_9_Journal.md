
<h3> Test 8 </h3>

Model name: Transfer learning baseline - VGG16

Model architecture:

![archi](/Documentations/Sam%20Journal/Images/Test_9_Archi.png)

For this model, we freezed all the other layers except for the last 6 layers of the VGG16, which were 3 dense layers + 1 conv layer + 1 maxpool layers. We also removed the dropout layer before the output layer as it proved to be restricted. The dropout percentage was kept at 20%. L2 = 0.1 was used  for kernel and bias regularlizer. The initial learning rate was 0.0025. Batch size was halved to 32 and steps per epoch to 30 from 50.

Model result:

![graph](/Documentations/Sam%20Journal/Images/Test_9_Graph.png)

This model achieved much even higher validation accuracy compared to the previous model, approximately 79%, while the overfitting effect was minimized. The differences between test and train accuracy were reduced. The same went for test and train lost. 

![metrics](/Documentations/Sam%20Journal/Images/Test_9_Metrics.png)

However, the average precision and recall values were approximately equal to the values from the previous model. This model was not overfitted badly, so this was a realiable result.

![confusion](/Documentations/Sam%20Journal/Images/Test_9_Confusion_Matrix.png)

The same went for the confusion matrix. There were much less errors across almost all the classes.

Next steps:
- Consider the removal of the troublesome classes.
- Address the size of the model.