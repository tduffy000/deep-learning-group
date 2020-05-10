
<h3> Test 10 </h3>

Model name: Transfer learning baseline - VGG16 - Same as model 9 but the dataset of the 2 buggy classes were merged together

Model architecture:

![archi](/Documentations/Sam%20Journal/Images/Test_10_Archi.png)

For this model, we freezed all the other layers except for the last 6 layers of the VGG16, which were 3 dense layers + 1 conv layer + 1 maxpool layers. We also removed the dropout layer before the output layer as it proved to be restricted. The dropout percentage was kept at 20%. L2 = 0.1 was used  for kernel and bias regularlizer. The initial learning rate was 0.0025. Batch size was halved to 32 and steps per epoch to 30 from 50.

Model result:

![graph](/Documentations/Sam%20Journal/Images/Test_10_Graph.png)

This model had the highest validation accuracy across all the tested models for far, about 86%. Similar to the last model, this model was not badly overfitted.

![metrics](/Documentations/Sam%20Journal/Images/Test_10_Metrics.png)

Because of the merging of the 2 bad classes in the dataset, the precision and recall values are now much higher as well. The values are also still closed to the validation accuracy. This was also another metric to show that this model was not overfitted.

![confusion](/Documentations/Sam%20Journal/Images/Test_10_Confusion_Matrix.png)

The class label issue was fixed. However, because the data was merged together, the merged class now had the more images than other classes. It may potential skew the result.

Next steps:
- With this model, it can be shown that the upper limit for this classification task is about 86%, which is acceptable! Next, we will test training the model again using the ResNet50 because Tony had troubles with that in the past. 
- Address the size of the model.