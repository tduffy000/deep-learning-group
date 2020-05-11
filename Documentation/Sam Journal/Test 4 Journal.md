
<h3> Test 4 </h3>

Model name: CNN with more complex architecture

Model architecture:

![archi](/Documentations/Sam%20Journal/Images/Test_4_Archi.png)

In this model, we increased the learning rate and decreased the decaying speed. The model also got more complex with more convolutional layers followed by dense layers along with dropout. The dropout rate for this particular model was 5%

Model result:

![graph](/Documentations/Sam%20Journal/Images/Test_4_Graph.png)

Compared to the previous model, this complex model's overfitting starting point was successfully delayed. It only started to diverge from approximately 10th epoch. This was a step in the right direction!

![metrics](/Documentations/Sam%20Journal/Images/Test_4_Metrics.png)

However, there was slight decrease in the recall and precision in testing the model. It might be due to increase in complexity with only minimal protection from overfitting (adding dropout layers)

![confusion](/Documentations/Sam%20Journal/Images/Test_4_Confusion_Matrix.png)

The same thing goes for observering the confusion matrix. There wasn't much improvement.

Next steps:
- Try new architecture
- Apply more aggressive regularlizer to reduce overfitting
- Increase step_per_epochs
- Increase the patient duration so the model can train for a bit longer
