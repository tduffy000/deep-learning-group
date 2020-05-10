
<h3> Test 11 </h3>

Model name: Transfer learning - Baseline ResNet50 

Model architecture:

![archi](/Documentations/Sam%20Journal/Images/Test_11_Archi.png)

This additional dense layers were the same as the ones using VGG16. However, the number of retrainable layers were reduce from 6 to 4 last layers of the ResNet50. The initial learning rate was 0.00025. The dropout percentage was 20%.

Results:

![graph](/Documentations/Sam%20Journal/Images/Test_11_Graph.png)

The model had much lower validation accuracy compared to the previous models. The value was hovering just below 50% for more than 100 epochs. However, there was literally no overfitting or underfitting in this model. The loss and accuracy of train and test set values were approximately the same during the training period. This was the best model so far in term of addressing the overfitting issue.

![metrics](/Documentations/Sam%20Journal/Images/Test_11_Metrics.png)

Despite being not overfitted, the model had low average precision and recall compared to other models. It might be because the input image size was smaller than the original image size that Resnet50 was trained on (224x224).

![confusion](/Documentations/Sam%20Journal/Images/Test_11_Confusion_Matrix.png)

The confusion matrix further solidated the above statement. The size of the input images was not big enough for the model to accurately predict the labels.

Next steps:
- Realizing the issue, we have 2 choices for our final models: increase the input image size or have more trainable layer.
- Because of the time constraint and consistency with other model, we will have more trainable layers instead of increasing the input image size.
- Because the model did a good in preventing overfitting, we can try to increase learning rate in hope that the model will have higher accuracy.