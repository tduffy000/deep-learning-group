
<h3> Test 8 </h3>

Model name: Transfer learning baseline - VGG16

Model architecture:

![archi](/Documentations/Sam%20Journal/Images/Test_8_Archi.png)

For this model, we freezed all the other layers except for the last 6 layers of the VGG16, which were 3 dense layers + 1 conv layer + 1 maxpool layers. We also removed the dropout layer before the output layer as it proved to be restricted. The dropout percentage was kept at 20%. The initial learning rate was 0.005.

Model result:

![graph](/Documentations/Sam%20Journal/Images/Test_8_Graph.png)

This model achieved much higher validation accuracy compared to the simple and complex CNN from the previous tests, about 75%. However, even with the dropout layers and learning rate scheduler, the model still started to be overfitted rather early. The reduced batch size might be still too big.

![metrics](/Documentations/Sam%20Journal/Images/Test_8_Metrics.png)

The average precision and recall values were approximately equal and close to the validation accuracy. Despite overfitting issue in late epoch, this model performed well.

![confusion](/Documentations/Sam%20Journal/Images/Test_8_Confusion_Matrix.png)

The same went for the confusion matrix. There were much less errors across almost all the classes.

Next steps:
- Address the overfitting issues
- Consider the removal of the troublesome classes.
- Address the size of the model.