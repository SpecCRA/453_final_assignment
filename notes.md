# EDA results

* 1551025 final rows
* Removed 61686 rows with > 2500 word reviews
* A lot of products categorized in other areas are still video games.
* The few stray products may not matter.
* About half the reviews give 5 stars.
* The rest are pretty even.
* Average review has about 430 words.
* Median is 273 words. Most have short (under 150 word) reviews.
* Video games are not just gaming titles. They also include gaming accessories.
    * Keyboards
    * Mice
    * Wheels (some that don't belong there)

# Processing notes

* Keep tokens greater than 3, less than 20 letters
* Final Train/Val/Test split (60/20/20)
    * Train: 75001
    * val: 25001
    * test: 24998

# Modeling notes

* 100 term TF-IDF works better than 200 terms
* 200 dimension embeddings works better than 100
* Moved towards regression because 1-5 is more easily intepretable.

# GloVe Notes

* Tutorial and download link: https://machinelearningmastery.com/develop-word-embeddings-python-gensim/

# Reference notes

* Regression with Keras: https://machinelearningmastery.com/regression-tutorial-keras-deep-learning-library-python/