from sklearn.metrics import roc_auc_score, confusion_matrix

def validate(model, X_test, y_test):
    preds = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, preds)
    cm = confusion_matrix(y_test, preds > 0.5)
    return auc, cm
