from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
# Dữ liệu huấn luyện
training_data = {
    'Height': [158, 158, 158, 160, 160, 163, 163, 160, 163, 165, 165, 165, 168, 168, 168, 170, 170, 170],
    'Weight': [58, 59, 63, 59, 60, 60, 61, 64, 64, 61, 62, 65, 62, 63, 66, 63, 64, 68],
    'T_Shirt_Size': ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']
}
df=pd.DataFrame(training_data)
label_encoder_size = LabelEncoder()
df['T_Shirt_Size'] = label_encoder_size.fit_transform(df['T_Shirt_Size'])
X = df[['Height', 'Weight']]
y = df['T_Shirt_Size']
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Lưu mô hình vào file decision_tree_model.pkl
joblib.dump(clf, 'decision_tree_model.pkl')

print("Model has been saved as 'decision_tree_model.pkl'.")