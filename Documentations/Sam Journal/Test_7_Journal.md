
<h3> Test 7 </h3>

Model name: CNN with more complex architecture 2

Model architecture:

![archi](/Documentations/Sam%20Journal/Images/Test_7_Archi.png)

Compared to the previous model, we only changed the batch_size. The previous model had the batch_size of 200 which might be the reason for overfitting.

Model result:

![graph](/Documentations/Sam%20Journal/Images/Test_7_Graph.png)

Indeed that was the reason. The model is now much less suspect to overfitting. The model was prematurely stopped at epoch 100. However, by continuing to train, the model was approaching 60% validation accuracy while the validation loss continue to decline (to be updated if possible)

![metrics](/Documentations/Sam%20Journal/Images/Test_7_Metrics.png)

Similarly, the precision and recall values of model on test set were much closer to the validation accuracy. It was on par with the previous model, while was much less overfitted. It indicated that overfitting issue had been mitigated. Hooray!
However, again, it still couldn't solve the issues in class 7 and 8

![confusion](/Documentations/Sam%20Journal/Images/Test_7_Confusion_Matrix.png)

Again, there is nothing particularly interesting in this model. However, this time, class 13 had a lot of false positive, and the errors were distributed among all other classes. Wonder what caused this.

Next steps:
- It seems like we approached the limit of simple and slightly complex CNN architecture. We however solved the overfitting issue by employing many tools. Using this knowledge, we can concatenate this model on top of a ResNet or VGG16 model and see!