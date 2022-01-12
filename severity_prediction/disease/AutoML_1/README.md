# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
|              | [1_Baseline](1_Baseline/README.md)                           | Baseline       | accuracy      |       0.526439 |         2.44 |
|              | [2_DecisionTree](2_DecisionTree/README.md)                   | Decision Tree  | accuracy      |       0.875441 |        58.94 |
|              | [3_Default_Xgboost](3_Default_Xgboost/README.md)             | Xgboost        | accuracy      |       0.989033 |        26.4  |
| **the best** | [4_Default_NeuralNetwork](4_Default_NeuralNetwork/README.md) | Neural Network | accuracy      |       1        |        14.99 |
|              | [5_Default_RandomForest](5_Default_RandomForest/README.md)   | Random Forest  | accuracy      |       0.913957 |        10.64 |
|              | [Ensemble](Ensemble/README.md)                               | Ensemble       | accuracy      |       1        |         0.69 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

