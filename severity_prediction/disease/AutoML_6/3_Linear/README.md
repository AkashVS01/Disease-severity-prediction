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

3.0 seconds

## Metric details
|           |     score |    threshold |
|:----------|----------:|-------------:|
| logloss   | 0.0924805 | nan          |
| auc       | 1         | nan          |
| f1        | 1         |   0.306397   |
| accuracy  | 1         |   0.306397   |
| precision | 1         |   0.506758   |
| recall    | 1         |   0.00286508 |
| mcc       | 1         |   0.306397   |


## Confusion matrix (at threshold=0.306397)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |               74 |                0 |
| Labeled as 1 |                0 |               25 |

## Learning curves
![Learning curves](learning_curves.png)

## Coefficients
| feature                    |   Learner_1 |
|:---------------------------|------------:|
| ALKALINE_PHOSPHOTASE       |   5.4762    |
| TOTAL_BILIRUBIN            |   0.469458  |
| AGE                        |   0.38142   |
| ASPARTATE_AMINOTRANSFERASE |   0.36504   |
| ALBUMIN                    |   0.120029  |
| GENDER                     |   0.112382  |
| TOTAL_PROTEINS             |   0.0840827 |
| ALBUMIN_AND_GLOBULIN_RATIO |   0.0569469 |
| DIRECT_BILIRUBIN           |  -0.13313   |
| ALAMINE_AMINOTRANSFERASE   |  -0.29203   |
| intercept                  |  -1.0745    |


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
