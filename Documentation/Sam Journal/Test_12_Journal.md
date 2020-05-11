
<h3> Test 12 </h3>

Model name: Transfer learning - Improved ResNet50 

Model architecture:

![archi](/Documentations/Sam%20Journal/Images/Test_12_Archi.png)

The overall architecture and hyperparameters of this model remained unchange. However, the number of retrainable layers were doubled from 4 to 8 last layers of the ResNet50. The initial learning rate remained at 0.00025, but it was now updated every 20 epochs instead of 10. The dropout percentage remained at 20% as well.

Results:

![graph](/Documentations/Sam%20Journal/Images/Test_12_Graph.png)

The overfitting/underfitting issue was still kept at base for this model. However, the fluctuations in the validation accuracy and loss were much higher compared to the last model. The validation accuracy was slightly lower as well.

![metrics](/Documentations/Sam%20Journal/Images/Test_12_Metrics.png)

The average precision and recall values were slightly lower. It showed that having more trainable layers didn't solve the problem.

![confusion](/Documentations/Sam%20Journal/Images/Test_12_Confusion_Matrix.png)

The same went for the confusion matrix. However, it was also noteworthy that the magnitude of the random errors across the labels were higher compared to other models (excluded the previous one). It showed that increasing the input image size should be the next thing to be tried.

Next steps:
- Increase the input image size