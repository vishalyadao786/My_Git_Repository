#SVR

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

#Fitting SVR model to the dataset
install.packages('e1071')
regressor = svm(formula = Salary ~ .,
                data = dataset,
                type = 'eps-regression')


#Predicting new result with Regression Model
y_pred = predict(regressor, data.frame(Level = 6.5))

#Visualizing the graphic result of SVR model results
ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary),
                      color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff (SVR Model)') + 
  xlab('Level') +
  ylab('Salary')

#Visualizing the graphic result of Regression model (for higher resolution and smoother curves)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary),
                      color = 'red') + 
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x-grid))),
            color = 'blue') +
  ggtitle('Truth or Bluff (SVR Model)') + 
  xlab('Level') +