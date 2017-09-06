#Random Forest Regression
#importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

#Splitting the datasets into Training Set and Test Set
#install.packages('caTools')
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

#Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])

#Fitting Random Forest Regression to the dataset
install.packages("randomForest")
set.seed(1234)
regressor = randomForest(x = dataset[1],
                         y = dataset$Salary,
                         ntree = 500)

#Predicting new result with Random Regression Model
y_pred = predict(regressor, data.frame(Level = 6.5))


#Visualizing the graphic result of Random Forest Regression model (for higher resolution and smoother curves)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary),
                      color = 'red') + 
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') +
  ggtitle('Truth or Bluff (Random Forest Regression Model)') + 
  xlab('Level') +
  ylab('Salary')