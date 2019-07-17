# NPS Sentiment Analysis

## Introduction
This project is my solution to annotate sentiments of NPS comments using pre-trained language models.

## Library/Environment
This is not meant to work in one single environment. I switched between two environments (one using Pytorch, one using Tensorflow) to make everything run smoothly.
- Pytorch
- Fastai
- Tensorflow 2.0
- Tensorflow hub

## Results
This is not a fair comparison and please take it only as a reference. I personally like the small model (gnews-swivel) provided by Tensorflow hub as it is very easy to train and still powerful enough to give decent result also it makes deployment much easier.

| Model | Accuracy | Precision | Recall | F1 Score |
| ----- | ----- | ----- | ----- | -----|
| ULMFIT (Fastai) | 0.97 | 0.98 | 0.92 | 0.95 |
| gnews-swivel (TF Hub) | 0.93 | 0.93 | 0.84 | 0.88 |
| nnlm-en-50 (TF Hub) | 0.96 | 0.96 | 0.90 | 0.93 |
| nnlm-en-128 (TF Hub) | 0.96 | 0.94 | 0.93 | 0.94 |
| AutoML (Google) | 0.96/0.93 | 0.98/0.81 | 0.87/0.96 | 0.92/0.88 |

Note: Since (AA custom trained) AutoML splits out `Neutral` on top of `Positive` and `Negative`, so it is very challenging to do unbiased comparison. Hence I recorded two values where 1st values are metrics considering `Neutral` to be `Negative` while the 2nd values are metrics considering `Neutral` to be `Positive`. Also, AutoML is used to test against only half of the human labelled dataset.

## Shoutout
Shoutout to all AA ASL 2018 members!

## Disclaimer
This project is not associated with my current employer. This project is solely initiated in attempt to beat Google AutoML.
