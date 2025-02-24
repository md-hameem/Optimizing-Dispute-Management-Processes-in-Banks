from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample dispute complaints
complaints = ["Unauthorized charge on account", "Fraudulent transaction", "Late payment processing", "Incorrect billing"]
labels = ["fraud", "fraud", "service", "billing"]

# Convert text data to feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(complaints)

# Train a classifier
model = MultinomialNB()
model.fit(X, labels)

# Predict new complaint category
new_complaint = ["Issue with billing on my account"]
new_vector = vectorizer.transform(new_complaint)
print(f"Predicted category: {model.predict(new_vector)}")

