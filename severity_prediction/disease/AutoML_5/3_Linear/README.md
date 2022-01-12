# Summary of 3_Linear

[<< Go back](../README.md)


## Logistic Regression (Linear)
- **n_jobs**: -1
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
accuracy

## Training time

2.7 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.106642 | nan          |
| auc       | 0.997101 | nan          |
| f1        | 0.978723 |   0.342291   |
| accuracy  | 0.973684 |   0.560936   |
| precision | 1        |   0.977425   |
| recall    | 1        |   5.5417e-06 |
| mcc       | 0.946963 |   0.560936   |


## Confusion matrix (at threshold=0.560936)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               30 |                0 |
| Labeled as 1 |                2 |               44 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature            |   Learner_1 |
|:-------------------|------------:|
| PARTIAL_PARESIS    |    1.74653  |
| MUSCLE_STIFFNESS   |    1.67068  |
| POLYPHAGIA         |    1.59762  |
| DELAYED_HEALING    |    1.47837  |
| ITCHING            |    1.3438   |
| VISUAL_BLURRING    |    1.17016  |
| POLYDIPSIA         |    1.16454  |
| WEAKNESS           |    1.01093  |
| SUDDEN_WEIGHT_LOSS |    0.927536 |
| POLYURIA           |    0.892691 |
| intercept          |   -0.641262 |


## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence (Fold 1)
![SHAP Dependence from Fold 1](learner_fold_0_shap_dependence.png)

## SHAP Decision plots

### Top-10 Worst decisions for class 0 (Fold 1)
![SHAP worst decisions class 0 from Fold 1](learner_fold_0_shap_class_0_worst_decisions.png)
### Top-10 Best decisions for class 0 (Fold 1)
![SHAP best decisions class 0 from Fold 1](learner_fold_0_shap_class_0_best_decisions.png)
### Top-10 Worst decisions for class 1 (Fold 1)
![SHAP worst decisions class 1 from Fold 1](learner_fold_0_shap_class_1_worst_decisions.png)
### Top-10 Best decisions for class 1 (Fold 1)
![SHAP best decisions class 1 from Fold 1](learner_fold_0_shap_class_1_best_decisions.png)

[<< Go back](../README.md)
