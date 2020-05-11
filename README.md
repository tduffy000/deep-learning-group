# deep-learning-group
Repo for Deep Learning @ CCNY Group Project (Spring 2020)

<h2>Yoga Pose classification</h2>

<h4>Motivation</h4>

Being in quarantine and working from home, our belly fat is stacking up, and our back is hurting. Since we have no prior experience with yoga poses, and can’t have an instructor to correct our poses while at home. Hence, for the final project, we are working on training a model that can classify different yoga poses and correct them via a smartphone  or laptop’s camera. We hope that it can help people to do yoga poses correctly at home and be healthy.

< More discussion in /Documentations >

<h4>Method</h4>

To tackle this problem, we will first train a simple CNN classifier to establish a baseline performance for the final model. Next, other pose identifying models will be concatenated to segment and classify those poses. To do this, specifically, we will first experiment with pose classifying algorithms/models and see how well they are performing on the yoga poses dataset. Based on the results, the outputs of the pose classifier model on the yoga dataset will be used to train a different neural network classifier to classify those yoga poses. The latter one can either be a simple DNN or a CNN with DNN layer as output layers. In summary, the plan is dataset -> yoga poses image classifier -> model and then dataset -> pose classifier -> segmented yoga poses -> yoga poses classifier -> model. The idea is to see how well and how fast an image-based classifier alone can classify yoga poses compared to a pose-based classifier. Based on the results, additional datasets from videos of new yoga poses can then be added and retrain the last couple of layers of the classifier using transfer learning.

<h3>Setup</h3>
First thing you can do is open a fresh notebook on [Google Colab](https://colab.research.google.com/). This will
allow you to make use of the managed environment (no need for `pip` or `conda`) and run the models contained
herein on the provided GPUs.

<h4>Data</h4>
Before we get started, we'll need data. Google exposes Google Drive files to Google Colab via a file stream. In order to setup this up all we need to do is mount it. First run (in a Colab cell):

```python
>>> from google.colab import drive, files
>>> _ = drive.mount('/content/drive')
```
This step will then send you a TSO link and once accepted will provide you with an access token to paste back in Colab.

Now we should have our Goolge Drive mounted and accessible via Colab. You should see
```bash
%ls -lrt

drwxr-xr-x 1 root root 4096 ..... .... sample_data/
drwx------ 4 root root 4096 ..... .... drive/
```
Your drive is in `drive/My\ Drive/`. We'll assume you have downloaded the dataset from [this site](https://oregonstate.app.box.com/s/4c5o6gilogogdm9m23tgtop7vw23e9vj). And have uploaded it within your Google Drive.

Go to the directory where `dataset.zip` that you downloaded is from and run (in a Cell). Note this will _overwrite_ the target directory:
```bash
!unzip -o dataset.zip -d <OUTPUT_DIR>
```
Now we have all the data nicely setup in our Google drive.

<h4>This repo</h4>

Next, you'll need to clone _this_ repo. You can do that within Google Colab several ways (depending on how you have authentication setup). Note we need to auth because this is a private repository.

If you *do not* have 2FA for your GitHub account you can simply open a new cell in Colab.
```bash
! git clone https://<username>:<password>@github.com/tduffy000/deep-learning-group.git
```

If you *do* have 2FA setup, you'll need a [Personal Access Token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) to include instead of your regular password. Then your request to GitHub will look like this
```bash
! git clone https://<username>:<personal_access_token>@github.com/tduffy000/deep-learning-group.git
```

To confirm everything went according to plan, you should be in a directory where you see the following:
```bash
%ls -lrt

-rw------- 1 root root 1053355720 ... ... ... dataset.zip
drwx------ 4 root root       4096 ... ... ... <OUTPUT_DIR>/
drwx------ 6 root root       4096 ... ... ... deep-learning-group/
```
Now, we're all ready to start messing around :smile:.

<h4>Models</h4>



MOVE BELOW ...

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
