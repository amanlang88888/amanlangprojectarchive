library(ggplot2)
library(dplyr)
library(rgl)
library(tidyverse)
library(moments)
library(car)
library(plotly)
library(rgl)
library(caret)
library(pROC)
library(sjPlot)

reviews_clean = read.csv("C:\\Users\\andre\\Desktop\\LSE Assignments\\reviews_clean.csv")
View(reviews_clean)

# I will create an MLR model.
# Y=Loyalty Points.
# X1=Remuneration, X2=Spending Score.

# Creating a subset. 
Subset <- data.frame(
  loyalty_points = reviews_clean$loyalty_points,
  rem = reviews_clean$rem,
  spending_score = reviews_clean$spending_score
)

# Checking datatypes.
str(Subset)

# Check for missing values.
missing_values <- sum(is.na(Subset))
print(missing_values)

# Summary statistics.
summary(Subset)

# Fitting the model. 
model <- lm(loyalty_points ~ rem + spending_score,
            data = Subset)
summary(model)

model_summ <- summary(model)
mean(model_summ$residuals^2)

# R-Squared=0.8269 indicates model is a strong fit.
# F-Statistic=4770, p-value=<2.2e-16, indicates model is a good fit. 
# Model indicates a strong relationship between Y and X1, X2.
# However, MSE=284879.8 is high. 

# I check the assumptions for MLR.

# ***1. Multicollinearity.***
cor(Subset$rem, Subset$spending_score)

# 0.0056 indicates a low correlation (0.56%) between remuneration
# and spending score.

vif(model)

vif_values <- vif(model)
barplot(vif_values, main = "VIF Values",
        horiz = TRUE)
abline(v = 5, lwd = 3, lty = 2)

# VIF scores indicate little multicollinearity.

# ***2. Linearity.***
# ***3. Inependence of Residuals
plot(loyalty_points ~ rem, data=Subset)
plot(loyalty_points ~ spending_score, data=Subset)

# Linear Relationship between Y~X1, Y~X2.

Subset <-
  Subset |> 
  mutate(yhat = fitted(model),
         res = residuals(model))

ggplot(Subset, aes(yhat, res)) +
  geom_point() +
  geom_hline(yintercept = 0, color = "red") +
  geom_smooth()

# Residuals are not aligning to predicted values.
# Relationship between predictor variables and outcome variables may be non-linear. 

# ***4. Normality.***
ggplot(Subset, aes(x = loyalty_points)) + 
  geom_histogram(binwidth = 1, fill = "blue", color = "black") + 
  theme_minimal()

hist(Subset$loyalty_points)

boxplot(Subset$loyalty_points)

# Extreme outliers.

qqnorm(Subset$loyalty_points,
       col='blue',
       xlab="z Value",
       ylab='Loyalty Points')

qqline(Subset$loyalty_points,
       col='red',
       lwd=2) 

# Right tail suggests extreme outliers - abnormal distribution.

shapiro.test(Subset$loyalty_points)

skewness(Subset$loyalty_points) 

# High positive skew.

kurtosis(Subset$loyalty_points)

# Heavy right tails.

# Distribution of model residuals.
model_residuals = model$residuals

hist(model_residuals)

# Histogram suggests normal distribution.

qqnorm(model_residuals)

qqline(model_residuals)

shapiro.test(model_residuals)

# Residuals are not normally distributed.
# Note, however, Shapiro-Wilk test is very sensitive.

skewness(model_residuals)

# Symmetry of distribution.

kurtosis(model_residuals)

# Indicates slightly heavy tails. 

# ***5. Homoscedasticity.***
par(mfrow=c(2,2))
plot(model)
par(mfrow=c(1,1))

# Residuals suggest non-collinearity.
# Q-Q plot indicates the presence of extreme outliers. 

# I will remake my model but utilise polynomial regression.

# Randomly shuffle data:
Subset.shuffled <- Subset[sample(nrow(Subset)),]

# Define no. of folds to use for k-fold cross-validation:
K <- 10

# Define degree of polynomials to fit.
degree <- 5

# Create k equal-sized folds:
folds <- cut(seq(1,nrow(Subset.shuffled)),breaks=K,labels=FALSE)

# Create object to hold model MSE's:
mse = matrix(data=NA,nrow=K,ncol=degree)

# Perform K-fold cross validation:
for(i in 1:K){
  
  # Define training and testing data:
  testIndexes <- which(folds==i,arr.ind=TRUE)
  testData <- Subset.shuffled[testIndexes, ]
  trainData <- Subset.shuffled[-testIndexes, ]
  
  # Use k-fold cv to evaluate models:
  for (j in 1:degree){
    fit.train = lm(loyalty_points ~ poly(rem,j) + 
                     poly(spending_score,j), data=trainData)
    fit.test = predict(fit.train, newdata=testData)
    mse[i,j] = mean((fit.test-testData$loyalty_points)^2) 
  }
}

# Find MSE for each polynomial degree:
colMeans(mse)
print(mse)

# The model with the lowest test MSE was the polynomial regression model 
# with degree, h=5.

# I will now fit the model with h=5.

poly_model <- lm(loyalty_points ~ poly(rem,5) + 
                   poly(spending_score,5), data=Subset)
summary(poly_model)

poly_model_summ <- summary(poly_model)
mean(poly_model_summ$residuals^2)

# R-Squared value indicates polynomial model explains large portion of variance
# in loyalty points.
# MSE=266132.7 indicates a significant prediction error, but is more
# accurate than using uncleaned data. 
# Strong relationship between Y and X1, X2 to h=5.
# There are significant polynomial terms:
# >poly(rem, 5)1
# >poly(spending_score, 5)1
# >poly(spending_score, 5)3
# >poly(spending_score, 5)4
# >poly(spending_score, 5)5

# I will remake my polynomial regression model using significant 
# polynomial terms.
significant_poly_model <- lm(loyalty_points ~ poly(rem, 5)[, 1] +
                               poly(spending_score, 5)[, 1] +
                               poly(spending_score, 5)[, 3] +
                               poly(spending_score, 5)[, 4] +
                               poly(spending_score, 5)[, 5],
                             data=Subset)
summary(significant_poly_model)
anova(poly_model, significant_poly_model)
anova(poly_model, model)

# P-value=0.01101 indicates a significant degradation in model fit
# when using only significant polynomial terms.
# P-value=<2.2e-16 indicates a significant improvement in fit 
# when fitting with the polynomial model.
# I will keep the polynomial model.

# I check the assumptions for MLR.

Subset <-
  Subset |> 
  mutate(yhat = fitted(poly_model),
         res = residuals(poly_model))

ggplot(Subset, aes(yhat, res)) +
  geom_point() +
  geom_hline(yintercept = 0, color = "red") +
  geom_smooth()

# There is still a large discrepancy between residuals and actual values. 

poly_residuals = poly_model$residuals

hist(poly_residuals)

shapiro.test(poly_residuals)

# I will remove loyalty points >5000 to attempt to improve model accuracy.
# I will remove remuneration values >100 to attempt to improve model accuracy.
Subset2 <- data.frame(
  loyalty_points = reviews_clean$loyalty_points,
  rem = reviews_clean$rem,
  spending_score = reviews_clean$spending_score
)

Subset2 <- Subset2[-which(Subset2$loyalty_points > 5000),]
Subset2 <- Subset2[-which(Subset2$rem > 100),]

hist(Subset2$loyalty_points) 
hist(Subset2$rem)

model2 <- lm(loyalty_points ~ rem + spending_score,
             data = Subset2)
summary(model2)

model_summ2 <- summary(model2)
mean(model_summ2$residuals^2)

# R-Squared=0.8084 indicates model is a strong fit.
# F-Statistic=4048, p-value=<2.2e-16, indicates model is a good fit. 
# Model indicates a strong relationship between Y and X1, X2.
# MSE=231846.8 indicates a significant prediction error, but is more
# accurate than using uncleaned data. 

cor(Subset2$rem, Subset2$spending_score)

# -0.058 indicates a low correlation between remuneration
# and spending score.

vif(model2)

vif_values <- vif(model2)
barplot(vif_values, main = "VIF Values",
        horiz = TRUE)
abline(v = 5, lwd = 3, lty = 2)

# VIF scores indicate little multicollinearity.

plot(loyalty_points ~ rem, data=Subset2)
plot(loyalty_points ~ spending_score, data=Subset2)

# Linear Relationship between Y~X1, Y~X2.

Subset2 <-
  Subset2 |> 
  mutate(yhat = fitted(model2),
         res = residuals(model2))

ggplot(Subset2, aes(yhat, res)) +
  geom_point() +
  geom_hline(yintercept = 0, color = "red") +
  geom_smooth()

# Residuals are align more to predicted values than when using
# uncleaned data. 

ggplot(Subset2, aes(x = loyalty_points)) + 
  geom_histogram(binwidth = 1, fill = "blue", color = "black") + 
  theme_minimal()

hist(Subset2$loyalty_points)

boxplot(Subset2$loyalty_points)

# Less extreme outliers. 

qqnorm(Subset2$loyalty_points,
       col='blue',
       xlab="z Value",
       ylab='Loyalty Points')

qqline(Subset2$loyalty_points,
       col='red',
       lwd=2) 

# Right tail suggests extreme outliers - abnormal distribution.

shapiro.test(Subset2$loyalty_points)

skewness(Subset2$loyalty_points) 

kurtosis(Subset2$loyalty_points)

model_residuals2 = model2$residuals

hist(model_residuals2)

# Histogram suggests normal distribution.

qqnorm(model_residuals2)

qqline(model_residuals2)

shapiro.test(model_residuals2)

par(mfrow=c(2,2))
plot(model2)
par(mfrow=c(1,1))

# I will identify residual outliers and remove
# residuals 2 standard deviations outside the norm.
Subset2$residuals <- resid(model2)
SD2 <- 2*sd(resid(model2))
SD2

# 2 standard deviations is 963.2605.

# I refit the model.
Subset2_cleaned <- Subset2 %>%
  filter(abs(residuals) <= SD2)

model2_cleaned <- lm(loyalty_points ~ rem + spending_score, data = Subset2_cleaned)
summary(model2_cleaned)

model_summ2cleaned <- summary(model2_cleaned)
mean(model_summ2cleaned$residuals^2)

# R-Squared=0.8224 indicates model is a strong fit.
# F-Statistic=4266, p-value=<2.2e-16, indicates model is a good fit. 
# Model indicates a strong relationship between Y and X1, X2.
# MSE=18874.1 indicates a significant prediction error, but is more
# accurate than using uncleaned data. 

cor(Subset2_cleaned$rem, Subset2_cleaned$spending_score)

# -0.036 indicates a low correlation between remuneration
# and spending score.

vif(model2_cleaned)

vif_values <- vif(model2_cleaned)
barplot(vif_values, main = "VIF Values",
        horiz = TRUE)
abline(v = 5, lwd = 3, lty = 2)

# VIF scores indicate little multicollinearity.

Subset2_cleaned <-
  Subset2_cleaned |> 
  mutate(yhat = fitted(model2_cleaned),
         res = residuals(model2_cleaned))

ggplot(Subset2_cleaned, aes(yhat, res)) +
  geom_point() +
  geom_hline(yintercept = 0, color = "red") +
  geom_smooth()

# Greater model accuracy. 

ggplot(Subset2_cleaned, aes(x = loyalty_points)) + 
  geom_histogram(binwidth = 1, fill = "blue", color = "black") + 
  theme_minimal()

hist(Subset2_cleaned$loyalty_points)

boxplot(Subset2_cleaned$loyalty_points)

# Less extreme outliers. 

shapiro.test(Subset2_cleaned$loyalty_points)

skewness(Subset2_cleaned$loyalty_points) 

kurtosis(Subset2_cleaned$loyalty_points)

model_residuals3 = model2_cleaned$residuals

hist(model_residuals3)

# Histogram suggests normal distribution.

qqnorm(model_residuals3)

qqline(model_residuals3)

shapiro.test(model_residuals3)

par(mfrow=c(2,2))
plot(model2_cleaned)
par(mfrow=c(1,1))

# I will visualise my model as a 3D scatterplot
data <- model2_cleaned$model
Remuneration <- data$rem
SpendingScore <- data$spending_score
LoyaltyPoints <- data$loyalty_points

plane_data <- expand.grid(
  rem = seq(min(Remuneration), max(Remuneration), length.out=30),
  spending_score = seq(min(SpendingScore), max(SpendingScore), length.out=30))

plane_predicted <- predict(model2_cleaned, newdata=plane_data)

predicted_matrix <- matrix(plane_predicted, nrow=30, ncol=30, byrow=TRUE)

plot3d(Remuneration, SpendingScore, LoyaltyPoints)
title3d("Multiple Linear Regression 3D Plot of Loyalty Points, Age, and Remuneration")
axes3d(labels = c("Remuneration", "Spending Score", "Loyalty Points"))
surface3d(
  x = seq(min(Remuneration), max(Remuneration), length.out=30),
  y = seq(min(SpendingScore), max(SpendingScore), length.out=30),
  z = predicted_matrix,
  color = 'green',
  alpha = 0.5
)

# I will visualise my model as a scatterplot with regression lines.
plotting_data <- expand.grid(
  rem = seq(min(Subset2_cleaned$rem), max(Subset2_cleaned$rem), length.out=30),
   spending_score = c(min(Subset2_cleaned$spending_score), mean(Subset2_cleaned$spending_score), max(Subset2_cleaned$spending_score)))

# I plot the predicted Y values my model makes on unseen data. 
plotting_data$predicted_y <- predict.lm(model2_cleaned, newdata=plotting_data)

plotting_data$spending_score <- as.factor(plotting_data$spending_score)

new_plot <- ggplot(Subset2_cleaned, aes(x=rem, y=loyalty_points)) +
  geom_point() +
  geom_line(data=plotting_data, aes(x=rem, y=predicted_y, color=spending_score), size=1.25) + 
  ggtitle("Scatterplot of Remuneration and Loyalty Points") +
  xlab("Remuneration") +
  ylab("Loyalty Points") +
  labs(color="Spending Score") +
  ylim(0, 5000)
new_plot

# I will experiment with a Logistic Regression Model.
# My outcome variable will be loyalty points (>2000 OR <2000).

Subsetlr <- data.frame(
  loyalty_points = reviews_clean$loyalty_points,
  rem = reviews_clean$rem,
  spending_score = reviews_clean$spending_score,
  education = reviews_clean$education,
  gender = reviews_clean$gender
)

str(Subsetlr)

missing_values <- sum(is.na(Subsetlr))
print(missing_values)

# Encode points>2000 as '1', and points<2000 as '0'.
Subsetlr$loyalty_points <- ifelse(Subsetlr$loyalty_points>2000,1,Subsetlr$loyalty_points)
Subsetlr$loyalty_points[Subsetlr$loyalty_points != 1] <- 0

# Convert outcome variable to a factor.
Subsetlr$loyalty_points <- as.character(Subsetlr$loyalty_points)
Subsetlr$loyalty_points <- as.factor(Subsetlr$loyalty_points)

# Encode values for education as it is categorical.
# >'Basic' = 0
# >'diploma = 1
# >'graduate' = 2
# >'postgraduate' = 3
# >'PhD' = 4
Subsetlr$education[Subsetlr$education == "Basic"] <- "0"
Subsetlr$education[Subsetlr$education == "diploma"] <- "1"
Subsetlr$education[Subsetlr$education == "graduate"] <- "2"
Subsetlr$education[Subsetlr$education == "postgraduate"] <- "3"
Subsetlr$education[Subsetlr$education == "PhD"] <- "4"

# Encode values for gender as it is categorical.
# >'Female' = 1
# >'Male' = 0
Subsetlr$gender[Subsetlr$gender == "Female"] <- "1"
Subsetlr$gender[Subsetlr$gender == "Male"] <- "0"

# Convert education to factor. 
Subsetlr$education <- as.factor(Subsetlr$education)

# Convert gender to factor. 
Subsetlr$gender <- as.factor(Subsetlr$gender)

# I split my data into training and test sets.
training.samples <- Subsetlr$loyalty_points %>%
  createDataPartition(p=0.8, list=FALSE)
train.data <- Subsetlr[training.samples, ]
test.data <- Subsetlr[-training.samples, ]

View(train.data)
View(test.data)

# Train the model. 
training_model <- glm(loyalty_points ~.,
                      data=train.data,
                      family="binomial")
summary(training_model)

# Extract statistically significant p-values.
sig_p <- data.frame(summary(training_model)$coef[summary(training_model)$coef[,4] >= .05, 4])
View(sig_p)

# We see that remuneration and spending score are highly significant predictors in 
# predicting loyalty points. 
# Education (diploma, graduate, postgraduate, PhD) is statistically insignificant. 
# Gender(female) is statistically significant.
# Model shows a great reduction in deviance from null deviance (1610.02) to 
# residual deviance (184.76), indicating good model fit.

# I will check the significance of the gender(male) and education(basic).
train.data$education <- relevel(train.data$education, ref = "1") # Set 'diploma' as reference
train.data$gender <- relevel(train.data$gender, ref = "1") # Set 'Female' as reference.

training_model <- glm(loyalty_points ~ ., 
                      data = train.data, 
                      family = "binomial")
summary(training_model)

# Education (basic) is statistically insignificant.
# Gender(male) is statistically significant.

# I will remake my model without using education as a predictor variable. 
training.samples <- Subsetlr$loyalty_points %>%
  createDataPartition(p=0.8, list=FALSE)
train.data <- Subsetlr[training.samples, ]
test.data <- Subsetlr[-training.samples, ]

View(train.data)
View(test.data)

training_model <- glm(loyalty_points ~ rem + spending_score + gender,
                      data=train.data,
                      family="binomial")
summary(training_model)

# Predict test set results.
# I predict the probability of 'loyalty_points'=1 (i.e. >2000 points) for
# each observation in the test set.
probabilities_model <- training_model %>% predict(test.data, type = "response")
head(probabilities_model)

# I round these probability values to either 1 or 0.
predicted.classes <- ifelse(probabilities_model > 0.5, "1", "0")
head(predicted.classes)

# I view the matching rows between predicted and actual values on 
# loyalty point category.
alignment_test <- data.frame(
  predicted = predicted.classes,
  actual = test.data$loyalty_points
)
View(alignment_test)

matching_rows <- subset(alignment_test, predicted == actual)
View(matching_rows)

# My model predicted correct loyalty point category 392/399 times (98% accuracy).

# I will use a confusion matrix to evaluate the predictive accuracy of my model.
alignment_test$predicted <- as.factor(alignment_test$predicted)
alignment_test$actual <- as.factor(alignment_test$actual)

actual_value <- alignment_test$predicted
predicted_value <- alignment_test$actual

confusion_matrix <- confusionMatrix(data=predicted_value, reference = actual_value)
confusion_matrix

# I will use an ROC curve to evaluate the predictive accuracy of my model.
PredLR <- predict(training_model, test.data, type = "response")
lgPredObj <- prediction((PredLR),test.data$loyalty_points)
lgPerfObj <- performance(lgPredObj, "tpr","fpr")

plot(lgPerfObj,main = "ROC Curve on LR Model Performance",col = 2,lwd = 2)
abline(a = 0,b = 1,lwd = 2,lty = 3,col = "black")

auc_value <- performance(lgPredObj, "auc")@y.values[[1]]
print(paste("AUC: ", auc_value))

# AUC=0.99 indicates the model is very good in distinguishing between positive and negative classes.  

# Visualisations:
plot(probabilities_model,
     main="Scatterplot of Probabilities of High Loyalty Points (test data)",
     xlab="Customer",
     ylab="Predicted Probability of High Loyalty Points (>2000 Points)")

plot_model(training_model,
           type = "pred",
           terms = c("spending_score", "rem", "gender"),
           ci.lvl = NA
) +
  labs(y = "Predicted Probability of High Loyalty Points (>2000 Points)",
       x = "Spending Score",
       title = "Predicted Probability of Loyalty Points",
       color="Remuneration") 





