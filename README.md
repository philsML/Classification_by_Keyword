# Classification_by_Keyword

Group Project from ESCP MSc. Big Data & Business Analytics (class of 2020)

Group Members: Jakob Engelhardt, Lorenzo Tozzi, Shivanand Rai, Philipp Aring

Goal: build models to classify gender and regress age of website users based on the keywords they viewed

Results: pred_results_v2.csv

Status: done

Task: We received an anonymized "Train" file with 1.2Gb file with keywords Age and Gender. We are supposed to train a model that can predict Gender and Age and run the model on a "Test" file and submit the predictions. 

All the coding was carried out on Google Colabs to allow for sufficient RAM and Storage space for An

Step 1. Keywords_preprocessing

We cleaned up the data here. The keywords were split by ; and then aggregrated by the number of times they occurred. However, given the large amount of columns, we removed words which occured less than 1% of the time in the overall dataset. We used NLTK stopwords to remove common words in French that won't value add to the analysis. Furthermore, for age, we realized that for marketing purposes, it will be more useful to group users together by age-groups which will be more meaningful since there is not much different between someone who is 25 and 26 but difference between someone who is in their late 30's. 

Step 2. Group Projects Keywords Compiled Analysis

Gender:
We ran multiple algorithms and realized Random Forest is the highest scoring algorithm to predict sex. We were sure to make sure a balanced in the algorithm as there was a tendency to favour males which made up a majority of observations. We did this through stratified sampling as well as balancing class weights in the Random Forest Algorithm. Furthermore, we optimized the final algorithm and achieved an accuracy within the training set of 63%. 

Age: 
We explored a non-bucketed and bucketed approach to the age brackets and realized that grouping age-groups together resulted in better accuracies as well as more meaningful analysis. This took more effort for us to test the outcomes of the algorithms as well however, we realized that Random Forest Classifier was once again the best algorithm. We saw an outcome of 35% for this accuracy.

Step 3: Keywords_Prep Application Set

This file runs our models on the final Test Dataset and outputs the predictions for the dataset. 
