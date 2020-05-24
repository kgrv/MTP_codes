import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import re
import seaborn as sns


codes=['ABT','AMZN','BCS','BP','C','F','GM','HMC','HSBC','JNJ','JPM','MRK','MSFT','PFE','SLB','TCEHY','TM','TSLA','UNH','XOM']

file=pd.read_excel(r'data\trainingFolder\master_data.xlsx')

article=[]
for i in range(len(file)):
    a=str(file.article[i])
    y=""
    for x in a.split("***"):
        y=y+" "+x
    article.append(str(y))
file['article']=article
File=pd.DataFrame()
File['sentence']=article
File['upintraday']=file['upintraday']
train_df=File[:800]

test_df=File[801:]


# Training input on the whole training set with no limit on training epochs.
train_input_fn = tf.compat.v1.estimator.inputs.pandas_input_fn(
    train_df, train_df["upintraday"], num_epochs=None, shuffle=True)

# Prediction on the whole training set.
predict_train_input_fn = tf.compat.v1.estimator.inputs.pandas_input_fn(
    train_df, train_df["upintraday"], shuffle=False)
# Prediction on the test set.
predict_test_input_fn = tf.compat.v1.estimator.inputs.pandas_input_fn(
    test_df, test_df["upintraday"], shuffle=False)

embedded_text_feature_column = hub.text_embedding_column(
    key="sentence", 
    module_spec="https://tfhub.dev/google/nnlm-en-dim128/1")



estimator = tf.estimator.DNNClassifier(
    hidden_units=[500, 100],
    feature_columns=[embedded_text_feature_column],
    n_classes=2,
    optimizer=tf.keras.optimizers.Adagrad(lr=0.003))


# Training for 5,000 steps means 640,000 training examples with the default
# batch size. This is roughly equivalent to 25 epochs since the training dataset
# contains 25,000 examples.
estimator.train(input_fn=train_input_fn, steps=4400)


train_eval_result = estimator.evaluate(input_fn=predict_train_input_fn)
test_eval_result = estimator.evaluate(input_fn=predict_test_input_fn)

print("Training set accuracy: {accuracy}".format(**train_eval_result))
print("Test set accuracy: {accuracy}".format(**test_eval_result))



train_eval_result = estimator.evaluate(input_fn=predict_train_input_fn)
test_eval_result = estimator.evaluate(input_fn=predict_test_input_fn)

print("Training set accuracy: {accuracy}".format(**train_eval_result))
print("Test set accuracy: {accuracy}".format(**test_eval_result))


def get_predictions(estimator, input_fn):
    return [x["class_ids"][0] for x in estimator.predict(input_fn=input_fn)]

LABELS = [
    "downintraday", "upintraday"
]

# Create a confusion matrix on training data.
cm = tf.math.confusion_matrix(train_df["upintraday"], 
                              get_predictions(estimator, predict_train_input_fn))

# Normalize the confusion matrix so that each row sums to 1.
cm = tf.cast(cm, dtype=tf.float32)
cm = cm / tf.math.reduce_sum(cm, axis=1)[:, np.newaxis]

sns.heatmap(cm, annot=True, xticklabels=LABELS, yticklabels=LABELS)
plt.xlabel("Predicted")
plt.ylabel("True")
