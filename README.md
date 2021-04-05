# Overview
Traffic jams in the city, as a result, many people in the city are choosing public transportation instead of their private cars. Therefore, scooters are used in response to their origin(first mile) and destination(last mile). This project aims to bring scooter user data to benefit the business.

## Problem formation
- predict the next 24-hour of scooter pick-ups.
- predict trip destinations


## Predict the next 24-hour of scooter pick-ups.
- preprocess by z-score normalization

    ![image](img/zscore.png)

- Divide the data into four groups using a



## Evaluate model
- Overestimate = ( (actual of non-zero pick-up) - predict ) >= 0  
- Underestimate = ( (actual of non-zero pick-up) - predict ) <= 0 
- Zero accuracy = ( (predict zero pick-up) / (actual of zero pick-up) )*100
   ![image](img/evaluate.png)



## Predict trip destinations



## Evaluate model
- Average Distance Days of the week
    ![image](img/evaluate days.png)
- Average Distance hours of the Day
    ![image](img/evaluate hour.png)