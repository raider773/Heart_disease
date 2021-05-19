# Heart_disease
Predicting if patient will have a heart disease

- The ultimate goal for this problem is to predict whether the observation has heart problems or not.
- See attributes.txt for more information of each feature.
- I'll divide the problem in different notebooks, first exploratory, then some feature engineering to add some features, then training the models and finally implementing the model with flask.


![image](https://user-images.githubusercontent.com/70241561/118749889-c651ec80-b834-11eb-9e95-94ceec075124.png)

![image](https://user-images.githubusercontent.com/70241561/118749898-cbaf3700-b834-11eb-9ff2-2b67982d322a.png)

![image](https://user-images.githubusercontent.com/70241561/118749926-d8338f80-b834-11eb-8da8-cf21467fb0d1.png)


I trained an extratrees and a random forest to see how much importance each feature has.

![image](https://user-images.githubusercontent.com/70241561/118749981-f13c4080-b834-11eb-8a82-7497c15c7473.png)


we can see how cp and ca are the most influencial ones.

----------------------------

I tried different dimensionality reduction models. All give me the same answer, the data was not so divisible.

![image](https://user-images.githubusercontent.com/70241561/118750088-1af56780-b835-11eb-898f-b079f75164da.png)



Also tried a Self organazing map.

The white squares are observatiosn that are far away from the central neurons, this means they are not common in the dataset. I separated those observations.

![image](https://user-images.githubusercontent.com/70241561/118750148-3fe9da80-b835-11eb-8441-22ac6f42732f.png)

![image](https://user-images.githubusercontent.com/70241561/118750157-44ae8e80-b835-11eb-9877-9802f851e381.png)


---------------------------------------------

I did some feature engineering in the dataset. I added a feature based on clusters. Used square distances, silhouette score and calinski harabasz score to determine
the best k for a k-means, then trained and predict on the data to add the clsuters as a feature. I apllied some log transformations to make the data look more like a 
gaussean,  added intervals of continuous features as new features and trained and applied a one hot encoder. I separated all this into a new module, so i can import it
every time i need to transform new data to make a prediction.

![image](https://user-images.githubusercontent.com/70241561/118750628-27c68b00-b836-11eb-8374-b7343644489c.png)

The final function calling all the transformations in a new module, ready to use.

![image](https://user-images.githubusercontent.com/70241561/118750679-3c0a8800-b836-11eb-9f31-daddbd3fda3a.png)

Hierarchical clustering for deciding the ammount of clusters.

![image](https://user-images.githubusercontent.com/70241561/118750722-57759300-b836-11eb-8d6a-9494f8c23414.png)

The intervals after the one hot encoding.

--------------------------------------

The data was small and not complex so a simple algorithm would work best. I Compared a KNN and Logistic regression and decided to keep the KNN.

![image](https://user-images.githubusercontent.com/70241561/118750827-9ad00180-b836-11eb-9983-99e5f3f8b21e.png)

KNN confusion matrix

![image](https://user-images.githubusercontent.com/70241561/118750864-ae7b6800-b836-11eb-9f21-71dc27491b00.png)


ROC Curve of logistic and knn.


Important note: i didn't change the threshold. Ideally i would have change it to predict more '1' classes (heart disease) at the expense of predicting more '0' classes,
but i leave it at 0.5.






