# FIFA player market valuation

#### • A Machine Learning Web App created with Flask deployed on Heroku platform.
#### • Do ⭐ the repository if it helped you in anyway.

#### • Webapp link: https://fifaplayervaluation.herokuapp.com/

## Preview
![ezgif com-gif-maker](https://user-images.githubusercontent.com/65092456/98434408-3e589080-20f5-11eb-9cbf-c5ecd6d2d4f3.gif)


## What is market value of a soccer player?
When we talk about the market value of a soccer player, we refer to the estimate of the amount his soccer club can sell or transfer his contract to another club. 
And soccer clubs can pay astronomical amount to obtain the top players.

The ability to predict market values may offer a commercial advantage to some of these rich soccer clubs.

## What are some of the most important factors that drive market value?

### • Footballing Skills
As no soccer players are 100% versatile, footballing skills are categorized into several domains such as Defending, Shooting and Goalkeeping. 
And having high ratings in any one of these domains can raise the market value.

### • On-Field Position
On average, strikers are valued more than midfielders, followed by defenders.

### • Age
Or the Coefficient of Youth. Naturally, younger players will command higher market value, as they have greater potential for growth and can have longer service terms.

### • Media Coverage
Or the Media Coefficient. Generally, having popular players, who make a greater media impact, can generate more revenue for the clubs.


Football is a team sport, thus it is quite hard to judge an individual football player’s performance. 
Diﬀerent people have diﬀerent opinions on a player’s performance. 
The responsibilities of each position are diﬀerent, which leads to performance indicators also being diﬀerent by position.
In this project I have tried to ﬁnd the relationship between market value and the performance of players and developedregression models to predict the market value 
on the basis of individual performance. 
A fair market would assign a higher market value to a player with high performance.


## Data Source Description

I web scraped the FIFA Index website using Beautiful Soup. In total, I collected data of 3000 players, which includes their height, weight, age, preferred foot and 
skill ratings. Each skill rating are sub-categorized into domains, which are scored from 0–100. 
The skill ratings are therefore web scraped by taking the mean of their domains. 

Skills ratings of footballers and their respective domains are given as:

Ball Skills: Ball Control, Dribbling

Passing: Crossing, Short Pass, Long Pass

Defense: Marking, Slide Tackle, Stand Tackle

Mental: Aggression, Reactions, Attack Position, Interceptions, Vision, Composure

Physical: Acceleration, Stamina, Strength, Balance, Sprint Speed, Agility, Jumping

Shooting: Heading, Shot Power, Finishing, Long Shots, Curve, Free Kick Accuracy, Penalties, Volleys

Goalkeeping: Positioning, Diving, Handling, Kicking, Reflexes


## Model Selection

To fit the data, the regression models that we wish to compare are Linear Regression, Polynomial Regression and Random Forest Regressor.
I have split the entire data frame into 80% Training Set and 20% Test set, where I hold out the Test Set for final model evaluation.
The best score I got for the model was using Random Forest Regressor, and using that model I hvae further deployed the project.


## Conclusion and Future 

The results of the finalized model is rather respectable given the limited features that I used. 
In the future, should other data sources be available, important features such as on-field position of players and media coefficient should be considered.
