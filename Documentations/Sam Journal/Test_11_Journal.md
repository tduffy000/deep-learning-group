
<h3> Test 11 </h3>

Model name: Transfer learning - Baseline ResNet50 

Model architecture:

This additional dense layers were the same as the ones using VGG16. However, the number of retrainable layers were reduce from 6 to 4 last layers of the ResNet50. The initial learning rate was 0.0025. The dropout percentage was 20%.

Results:

The model had much lower validation accuracy compared to the previous models. The value was hovering just below 50% for more than 100 epochs. It might be due to complex nature of the ResNet or the learning rate.