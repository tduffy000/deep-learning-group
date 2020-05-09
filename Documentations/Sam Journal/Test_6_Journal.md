
<h3> Test 6 </h3>

Model name: CNN with more complex architecture 2

Model architecture:

![archi](/Documentations/Sam%20Journal/Images/Test_6_Archi.png)

In this model, we made some changes to the architecture by changing the size and removing some convolutional layers. The dropout percentage was also increased to 20% across all the dropout layers. We also increased the learning rate and decaying frequency but decreased the decaying magnitude. 

Model result:

![graph](/Documentations/Sam%20Journal/Images/Test_6_Graph.png)

Much much better result. This model was no longer overfitting as crazy as the last model.
Not only that, this model has the highest validation accuracy so far, as much as the first model, while being more robust.

![metrics](/Documentations/Sam%20Journal/Images/Test_6_Metrics.png)

By observing the metrics, we can see that even though the recall and precision values are approximately equal the validation accuracy

![confusion](/Documentations/Sam%20Journal/Images/Test_6_Confusion_Matrix.png)

There is nothing particularly interested about this model's confusion matrix. There are still noises and error.

Next steps:
- Lower the training batch size. I just realized that our training batch size was 200. Crazy! That might be the reason for the differences between validation and train accuracy.