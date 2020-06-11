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

# GloVe Notes

* Tutorial and download link: https://machinelearningmastery.com/develop-word-embeddings-python-gensim/