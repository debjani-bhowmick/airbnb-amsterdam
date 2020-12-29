# Amsterdam-Airbnb-Udacity-Project

### Table of Contents

1. [Summary](#summary)
2. [Installation](#installation)
3. [Project Motivation](#motivation)
4. [File Descriptions](#files)
5. [Results](#results)
6. [Data Resource](#)
6. [Licensing, Authors, and Acknowledgements](#licensing)

### Summary <a name="summary"></a>

This project and the associated code are meant to serve as an assignment project for the partial fulfilment of the Udacity Data Scientist Nanodegree. The project involves analysis of Airbnb data using CRISP-DM method, and we focus on the Airbnb data from the city of Amsterdam. The primary goal is to analyse the data and present the findings. We provide below details related to the motivation for this work, installation of the code, main findings etc below. For further understanding related to the project as well as the findings, see the blog post [here](https://debjani-ism.medium.com/analysis-of-amsterdam-airbnb-dataset-e3ac9beb3551).

## Installation <a name="installation"></a>

This code has been tested with Anaconda distribution of `Python 3.6`. Additional libraries used int the project are:  

numpy 1.19.2<br>
pandas 1.1.3<br>
matplotlib 3.3.2<br>
folium 0.11<br>
geopandas 0.8.1<br>
seaborn 0.11.0


## Motivation<a name="motivation"></a>

Amsterdam is one of the most popular tourist destinations in Europe, attracting up to approximately 46 million tourists in the year 2019 alone. This has also led to significant popularity of Airbnb services within this beautiful city. The houses of the locals are culturally beatiful, and tourists often prefer staying at these localities, rather than going for hotels. These houses also offer cheaper prices which is another reason for Airbnb to have become popular.

For a person willing to rent a room or two from their house as a part of Airbnb services, it is important that the initial prices are chosen reasonably. A price quoted higher than what a room deserves to be quoted can lead to poor reviews, eventually reducing the revenue. Hence, it is important that the price of the room is properly assessed based on the locality, price in the region, as well as the services within.

Based on the problem outlined above, we address the following points this study.
* Analyse the distribution of listings as well as the prices across neighborhoods.
* Identify the regions where the prices are high, and relate them with possible touristic locations in Amsterdam. This information could help in selecting one among multiple properties to list on Airbnb while maximimizing the chances of profit.
* for the prices of the new listings, we address the following questions:
  - Can the prices for future listings be actually predicted using the available data?
  - What are the most important features to model with?
  - Which model is a better/appropriate model to predict the prices?


## File Descriptions <a name="files"></a>

This project structure is divided into two directories:
* ams-airbnb-amsterdam: Contains the two ipynb notebooks on analysis and modeling.
  - Airbnb_Amsterdam.ipynb: Contains scripts for analyzing the data of Airbnb Amsterdam.
  - Modelling.ipynb: Contains script for fitting regression models for price prediction.
* Data: contains files with airbnb data from Amsterdam.

## Results<a name="results"></a>

From the analysis presented above, we have seen that the mean prices as well as the variance are significantly higher in the regions closer to the city center when compared to the places away from it. Further, we have unrealistic outliers as well in the data. Overall, choosing one of these 4 listings could possibly be a nice deal in terms of maximizing the return from the listing. For more concrete analysis, data on daily reservations should also be studied, however, we keep it beyond the scope of this study. We analyzed the Airbnb data of the city of Amsterdam and studied the distributions of listings and pricings. A general observation is that the prices are higher around the city center. In general, most tourist destinations are closer to this region due to which the prices are higher in this areas. Clearly, if we intend to put a new listing this region, we would prefer to quote a higher price.

Further, we also trained regression models for predicting price for a new listing in the Amsterdam region. For regression models, we experimented with linear and ridge regression methods, applied bagging, boosting as well trained random forest model for the task. We also identified the top K features to predict the prices. Among the various methods, we found that Random We see here that the error is mae gets reduced when using random forest. Moreover, with random forest, the mae reduces from 52 to 32 when compared to the dummy classifier baseline. This is almost a reduction of 33%. With improved regressors, this error can be reduced further, however, that is kept beyond the scope of this study. With this study, it is hoped to have been sufficiently demonstrated that the prices of future listings can be predicted.

#### Some important findings can be summarized below :<br>
  * Among the various neighborhoods, those closer to the city center of Amsterdam have the highest mean prices as well as the largest variances.
  * Mostly listings are more common in touristic areas, or those that have more coorporate offices (Zuid Amsterdam) and restaurants, cafes (De Pijp).
  * Based on the features for listing, regression models can indeed be trained to predict price for a new listing. <br>
  * Among the different regression models, random forest performs best, and there is scope for improved results with more advanced models, such as deep neural networks.
 
The main findings of the code can also be found at the blog post [here](https://debjani-ism.medium.com/analysis-of-amsterdam-airbnb-dataset-e3ac9beb3551)

## Data resource<a name="data"></a>:

Data sourced from Airbnb website here [here](http://insideairbnb.com/get-the-data.html).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credits must be given to Airbnb for the data.  Details related to licensing for the data and other descriptive information can be obtained [here](http://insideairbnb.com/get-the-data.html).  
