# flight-delay-predictions

![](https://github.com/nithabalakrishnan/flight-delay-prediction/blob/master/Pictures/scheduled.JPG)

Graph sourced from:
https://public.tableau.com/profile/loba8789#!/vizhome/Flightdelay_15719588855170/Sheet2

Predicting flight delays has been a popular hobby for many people for decades. Now that we have the ability to use AI and the many machine learning algorithms, we decided to use a couple of them to see how accurate these predictions are. This study analyzes high-dimensional data from US Airports and presents a practical flight delay prediction model. Following a multifactor approach, a novel method is employed to mine the inner patterns of flight delays. The proposed method has proven to be highly capable of handling the challenges of large datasets and capturing the key factors influencing delays. Accurate predictions of far out delays took a few refining steps and here is what we did with our Flight predictor models:

•	First we built mini model to get a better sense of what our dataset is capable of or its limits

•	Random forest classifier

•	80/20 data set for training and testing respectively

•	Since its classifier just predicting delay or no delay

•	Parameters ‘day of month’, ‘departure airport’ ‘destination airport’

•	R2 = 78

•	Linear & ridge 

•	50/50 split

•	Predicting how many minutes will be delayed

•	Parameters used: day_of_week, dep_time, origin_airport_id, op_carrier_fl_num, arr_delay, dest_airport_id

•	R2 = 94



![](https://github.com/nithabalakrishnan/flight-delay-prediction/blob/master/Pictures/by%20state.JPG)

BUILT WITH

https://www.bts.gov/ -  data source for flight information

https://openflights.org/data.html - Airports csv for coordinates



Jupyter Notebook - tool for coding

Pandas - tool for manipulating data

Tableau - visualization of data

Machine Learning Algorithms to Predict delays :  

1) Random Forest: used to predict whether a flight will be delayed or not 

2) Ridge Regression to see how many minutes a particular flight will be delayed

![](https://github.com/nithabalakrishnan/flight-delay-prediction/blob/master/Pictures/topdelayed.JPG)


2018 USA Domestic flights analysis:
https://public.tableau.com/profile/loba8789#!/vizhome/Flightspredictor/Mapofstateswithdelays?publish=yes


