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












