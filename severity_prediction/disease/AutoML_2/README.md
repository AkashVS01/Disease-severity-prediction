# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
|              | [1_Baseline](1_Baseline/README.md)                           | Baseline       | accuracy      |       0.757576 |         0.96 |
| **the best** | [2_DecisionTree](2_DecisionTree/README.md)                   | Decision Tree  | accuracy      |       0.989899 |        25.41 |
|              | [3_Linear](3_Linear/README.md)                               | Linear         | accuracy      |       0.969697 |         4.8  |
|              | [4_Default_Xgboost](4_Default_Xgboost/README.md)             | Xgboost        | accuracy      |       0.989899 |         5.42 |
|              | [5_Default_NeuralNetwork](5_Default_NeuralNetwork/README.md) | Neural Network | accuracy      |       0.969697 |         1.86 |
|              | [6_Default_RandomForest](6_Default_RandomForest/README.md)   | Random Forest  | accuracy      |       0.989899 |         3.89 |
|              | [Ensemble](Ensemble/README.md)                               | Ensemble       | accuracy      |       0.989899 |         0.26 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

