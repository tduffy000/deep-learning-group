# deep-learning-group
Repo for Deep Learning @ CCNY Group Project (Spring 2020)

<h2>Yoga Pose classification</h2>

<h4>Motivation</h4>

Being in quarantine and working from home, our belly fat is stacking up, and our back is hurting. Since we have no prior experience with yoga poses, and can’t have an instructor to correct our poses while at home. Hence, for the final project, we are working on training a model that can classify different yoga poses and correct them via a smartphone  or laptop’s camera. We hope that it can help people to do yoga poses correctly at home and be healthy.

<h4>Method</h4>

To tackle this problem, we will first train a simple CNN classifier to establish a baseline performance for the final model. Next, other pose identifying models will be concatenated to segment and classify those poses. To do this, specifically, we will first experiment with pose classifying algorithms/models and see how well they are performing on the yoga poses dataset. Based on the results, the outputs of the pose classifier model on the yoga dataset will be used to train a different neural network classifier to classify those yoga poses. The latter one can either be a simple DNN or a CNN with DNN layer as output layers. In summary, the plan is dataset -> yoga poses image classifier -> model and then dataset -> pose classifier -> segmented yoga poses -> yoga poses classifier -> model. The idea is to see how well and how fast an image-based classifier alone can classify yoga poses compared to a pose-based classifier. Based on the results, additional datasets from videos of new yoga poses can then be added and retrain the last couple of layers of the classifier using transfer learning.

<h4>Evaluate</h4>

To evaluate the model, a simple train test split from the dataset will be used first to evaluate the result. Then, some non-yoga pose images can be used to evaluate how well the model is differentiating between yoga and non-yoga poses. Finally, if the model performed well on the previous two tests, the final model can then be implemented and evaluate by a human using a laptop webcam or smartphone’s camera to first differentiate yoga and non-yoga poses, then between different types of yoga poses.

<h4>Others</h4>
Regarding the pose classifier, there are many choices to choose from. One of them is OpenPose. Based on other project’s, the model can perform a really good job in detecting the human body, hand, and legs key-points. With many different types of output and its Python API, the output result of the dataset can be used to classify the poses.

The dataset is from the Oregon State University. It contains approximately 107 different yoga poses, 5994 total images, and about 60 images per class. Combining with data augmentation, this dataset should be sufficient to train the model. You can download it from this [link](https://oregonstate.app.box.com/s/4c5o6gilogogdm9m23tgtop7vw23e9vj).

<h4>Similar Projects and Conclusion</h4>
  Even though there are already plenty of similar projects on the internet, the idea of using transfer learning to add new poses to the model is still new. Hence, this project can be built upon the previous work to improve its capabilities.

These are some prior works that this project can be based on and improve it.

[Stanford Project](http://cs230.stanford.edu/projects_winter_2019/reports/15813480.pdf)

[Smart Mirror Yoga AI](https://www.hackster.io/yogai/yogai-smart-personal-trainer-f53744)

[Sample Project](https://github.com/DhruvJawalkar/yoga-pose-estimation)
