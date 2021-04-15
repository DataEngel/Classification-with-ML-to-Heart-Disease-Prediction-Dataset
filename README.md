# Project: Algorithms and methods for classification
 
**What is the Heart disease prediction dataset about?** It is a subset of variables from a study carried out in 1988 in different regions of the world to predict the risk of suffering a heart-related disease.
 
>**_Note:_** In this readme only the results will be shown, for more details see the code in the code folder of this repo.
 
## Principal component analysis
 
**Why do we use this algorithm?**
 
 Because in machine learning it is normal to find problems where we have a huge amount of features where there are complex relationships between them and with the variable we want to predict.
 
**Where can a PCA algorithm be used?**
 
* Our dataset has a high number of features and not all of them are significant.
* There is a high correlation between the features.
* When there is overfitting.
* When it involves a high computational cost.
 
---
 
**What is the PCA algorithm?**
 
It basically consists of reducing the complexity of the problem:
 
**1.-** Selecting only the relevant variables.
 
**2.-** Combining them in new variables that keep the most important information (variance of the features).

![1](https://user-images.githubusercontent.com/63415652/105783945-5645f080-5f3d-11eb-97f5-b0ab1ab96f3b.PNG)
 
Well, now that we have the context of our dataset, let's see what the result / precision was applying a logistic regression with the complexity reduction applied:
 
![8](https://user-images.githubusercontent.com/63415652/103371135-4f3dd680-4a94-11eb-9f04-e409c3c9587b.PNG)
 
Well from the outset we see that the 2 algorithms have almost the same performance, but what do we achieve with this?
 
The original dataset had 13 features to try to predict a binary classification of whether the patient has heart disease or not, and now with PCA we only need 3 artificial features to arrive at a good enough result.
 
 >**_Conclusion:_** we are saving computational cost, since we are only using the relevant information for our model.
 
## Project 2: Kernels and KPCA
 
**Now that we know the PCA algorithm, what other alternatives do we have?**
 
---
 
Well, an alternative is the kernels. A kernel is a mathematical function that takes measurements that behave non-linearly and projects them into a larger dimensional space where they are linearly separable.
 
**And what is this for?**
 
![2](https://user-images.githubusercontent.com/63415652/105783948-580fb400-5f3d-11eb-982e-949bfb6c8f1c.PNG)
 
It serves for cases where they are not linearly separable. In the first image it is not possible to separate them with a line and in image 2 if we can do it through Kernels. What the Kernels function does is project the points into another dimension and thus make the data linearly separable.
 
Now we are going to implement kernels to our dataset and measure with which precession it was correct when classifying:
 
![10](https://user-images.githubusercontent.com/63415652/103372281-32ef6900-4a97-11eb-8c9b-d4fb4f3abf94.PNG)
 
> **_Conclusion:_** Implementing a kernel is relatively easy and has good precision, the biggest problem we will face is identifying when we will need to model a higher dimensional space.
 
## Assembly methods
 
### Bagging:
 
What if instead of relying on the opinion of a single "expert" we consult the opinion of several experts in parallel and try to reach a consensus?
 
For this we have to imagine that our ML model is an expert, but what if we could have the opinion of several experts? Well, it would be much better, right? So, in this algorithm, several expert votes are taken into consideration and for this a count can be made or simply an average.
 
### Boosting.
 
* It means to propel / propel.
* It is a sequential method.
* Seeks to gradually strengthen a learning model always using the residual error of the previous stages.
* The final result is also achieved by consensus among all models.
 
Now, we are going to see the results implementing the methods in code.
 
Here we can see the precession that all assembly methods had in relation to the KNN without assembly method:
 
![12](https://user-images.githubusercontent.com/63415652/103423141-a910d000-4b6a-11eb-8255-38255ac7a2bc.PNG)
 
And finally the boosting precision:
 
![13](https://user-images.githubusercontent.com/63415652/103423142-aa41fd00-4b6a-11eb-8f84-c6e2682d0bad.PNG)
 
As we can see, the Boosting method gave us very significant accuracy.
 
With the assembly methods, even though we had a classifier that was not that good, we can achieve much better results using the assembly methods. Also, a classifier alone is not always as powerful as applying that classifier many times with different parameters and different settings with a consensus method applied.
 
>**_Conclusion:_** In a real life exercise we are classifying a patient and we have a super high percentage of accuracy when predicting a patient, so this is excellent support for a doctor in a clinic at work daily.

---

## Data source: [Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci "Heart Disease UCI")

Although the code is not proprietary and is free to use, the data is licensed, please read it before using this data.
This project is not for commercial purposes, it is for academic purposes only.

## You can check the main notebook in my kaggle profile and if you like, my other contributions too:

* [Classification in Heart Disease Prediction DataSet](https://www.kaggle.com/dataengel/classification-in-heart-disease-prediction-dataset "Classification in Heart Disease Prediction DataSet") 
