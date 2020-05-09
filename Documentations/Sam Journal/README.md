Test 1 
Model name: Simple CNN
Model architecture:
![archi](/Documentations/Sam%20Journal/Test_1_Archi.png)

Model result
![graph](/Documentations/Sam%20Journal/Test_1_Graph.png)
Because this model is super simple, it gets quickly overfitted after only 2 epochs. However, one of the reasons might be because the batch_size of was 32 and steps_per_epoch was 200 which trained the model on the repetitive data many times and caused it to overfitted.

![metrics](/Documentations/Sam%20Journal/Test_1_Metrics.png)
When the model tried to predict the unseen data, surprisingly, the precisions across classes were much higher than the validation_accuracy. It might be a good thing because the validation data was augmented during the training process to make it much more varied and hence, more difficult for the model to predict during the training process.
![confusion](/Documentations/Sam%20Journal/Test_1_Confusion_Matrix.png)
The confusion matrix here visualized the result. This basic model has no trouble in predicting the labels for most of the classes. However, the model had slight troubles in its precision for class 8. One of the explaination might be because of the uneven distribution of the test set. The usual higher precision of the test set compared to the validation accuracy might be due to its size.

Next step
To address the issue in this step, we will try these changes in the subsequent iterations:
- Lower the steps_per_epoch value to solve the overfitting issue
- Lower the batch_size as well
- Test other methods: such as using regularlizer to lower the learning rate as the training goes on or change the optimizer.
- It might be a good idea to generate addition images to ensure that the number of images per class are the same.
- Changing the architecture will follow after fixing the overfitting issue