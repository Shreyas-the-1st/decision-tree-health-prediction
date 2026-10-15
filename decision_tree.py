
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

url = "https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/DoctorContacts.csv"
df = pd.read_csv(url)

X = df[["educdec"]]
y = df["health"]

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

prediction = clf.predict(
    pd.DataFrame({"educdec": [10]})
)

print("Predicted health category:", prediction[0])