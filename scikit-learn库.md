# scikit-learn 常用模块和函数

## 1. 分类指标 (Classification Metrics)

### 1.1 'accuracy_score'计算分类模型的准确率（Accuracy）

```python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_true, y_pred)
```

### 1.2 'precision_score'计算分类模型的精确率（Precision）

```python
from sklearn.metrics import precision_score
precision = precision_score(y_true, y_pred, average='binary')
```

### 1.3 'recall_score'计算分类模型的召回率（Recall）

```python
from sklearn.metrics import recall_score
recall = recall_score(y_true, y_pred, average='binary')
```

### 1.4 'f1_score'计算分类模型的F1分数

```python
from sklearn.metrics import f1_score
f1 = f1_score(y_true, y_pred, average='binary')
```

### 1.5 'confusion_matrix'计算混淆矩阵

```python
from sklearn.metrics import confusion_matrix
conf_matrix = confusion_matrix(y_true, y_pred)
```

### 1.6 'classification_report'生成分类报告，显示精确率、召回率、F1分数和支持度

```python
from sklearn.metrics import classification_report
report = classification_report(y_true, y_pred)
```

### 1.7 'roc_curve'计算 ROC 曲线的假正率（FPR）和真正率（TPR）

```python
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_true, y_score)
```

### 1.8 'auc'计算 ROC 曲线下的面积（AUC）

```python
from sklearn.metrics import auc
roc_auc = auc(fpr, tpr)
```

## 2.回归指标 (Regression Metrics)

### 2.1 'mean_squared_error'计算均方误差（MSE）

```python
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_true, y_pred)
```

### 2.2 'mean_absolute_error'计算平均绝对误差（MAE）

```python
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_true, y_pred)
```

### 2.3 'r2_score'计算 R² 得分，衡量回归模型的拟合效果

```python
from sklearn.metrics import r2_score
r2 = r2_score(y_true, y_pred)
```

## 3. 聚类指标 (Clustering Metrics)

### 3.1 'adjusted_rand_score'计算调整后的 Rand 指数（用于衡量聚类效果

```python
from sklearn.metrics import adjusted_rand_score
ari = adjusted_rand_score(y_true, y_pred)
```

### 3.2 'silhouette_score'计算轮廓系数（用于评估聚类质量）

```python
from sklearn.metrics import silhouette_score
score = silhouette_score(X, labels)
```

## 4. 模型选择与评估 (Model Selection and Evaluation)

### 4.1 'train_test_split'将数据集拆分为训练集和测试集

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### 4.2 'cross_val_score'使用交叉验证评估模型的性能

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
```

### 4.3 'GridSearchCV'通过网格搜索调整模型的超参数

```python
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
grid_search = GridSearchCV(SVC(), param_grid, cv=5)
grid_search.fit(X, y)
```

### 4.4 'RandomizedSearchCV'通过随机搜索调整模型的超参数

```python
from sklearn.model_selection import RandomizedSearchCV
param_distributions = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
random_search = RandomizedSearchCV(SVC(), param_distributions, n_iter=10, cv=5)
random_search.fit(X, y)
```

## 5.数据预处理(Data Preprocessing)

### 5.1 'StandardScaler'标准化特征，使其均值为0，方差为1

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 5.2 'MinMaxScaler'将特征缩放到指定的最小和最大值之间，通常为 [0, 1]

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

### 5.3 'LabelEncoder'将类别标签编码为数字

```python
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
```

### 5.4 'OneHotEncoder'对分类特征进行独热编码

```python
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X)
```

## 6. 特征选择 (Feature Selection)

### 6.1 'SelectKBest'选择 K 个最佳特征

```python
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
selector = SelectKBest(f_classif, k=5)
X_selected = selector.fit_transform(X, y)
```

### 6.2 'RFE'递归特征消除（Recursive Feature Elimination），选择最重要的特征

```python
from sklearn.feature_selection import RFE
selector = RFE(estimator=LinearRegression(), n_features_to_select=5)
X_selected = selector.fit_transform(X, y)
```

## 7. 模型训练与预测 (Model Training and Prediction)

### 7.1 'fit'训练模型

```python
model.fit(X_train, y_train)
```

### 7.2 'predict'使用训练好的模型进行预测

```python
y_pred = model.predict(X_test)
```

### 7.3 'predict_proba'对于分类问题，获取每个类别的预测概率

```python
y_prob = model.predict_proba(X_test)
```

### 7.4 'score'评估模型的性能

```python
model_score = model.score(X_test, y_test)  # 对于分类模型，返回准确率
```

## 8. 核心算法模块 (Core Algorithm Modules)

### 8.1 'LinearRegression'线性回归模型

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
```

### 8.2 'LogisticRegression'逻辑回归模型

```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
```

### 8.3 'SVC'支持向量机分类模型（Support Vector Classifier）

```python
from sklearn.svm import SVC
model = SVC()
```

### 8.4 'RandomForestClassifier'随机森林分类模型

```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
```

### 8.5 'KNeighborsClassifier'K 最近邻分类模型

```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
```

### 8.6 'DecisionTreeClassifier'决策树分类模型

```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
```

以上是 scikit-learn 库的一些常用模块和函数的整理。根据您的实际需求，您可以使用这些函数来评估、训练、优化和处理您的数据和模型。
