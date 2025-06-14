import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set file paths
base_path = r"C:\Users\sanaf\Desktop\Task 5 Titanic"

train_path = base_path + r"\train.csv"
test_path = base_path + r"\test.csv"
gender_submission_path = base_path + r"\gender_submission.csv"

# Load datasets
df_train = pd.read_csv(train_path)
df_test = pd.read_csv(test_path)
df_gender = pd.read_csv(gender_submission_path)

# Preview
print("Train Data:")
print(df_train.head(), '\n')

print("Test Data:")
print(df_test.head(), '\n')

print("Gender Submission Data:")
print(df_gender.head())
import os
# Set plotting style
sns.set(style="whitegrid")

# -------------------------------------
# LOAD DATASETS
# -------------------------------------
path = r"C:\Users\sanaf\Desktop\Task 5 Titanic"
df_train = pd.read_csv(os.path.join(path, "train.csv"))
df_test = pd.read_csv(os.path.join(path, "test.csv"))
df_gender = pd.read_csv(os.path.join(path, "gender_submission.csv"))

# -------------------------------------
# a. DESCRIBE, INFO, VALUE_COUNTS
# -------------------------------------
print("=== Info ===")
print(df_train.info(), "\n")

print("=== Describe ===")
print(df_train.describe(), "\n")

print("=== Value Counts ===")
print("Survived:\n", df_train['Survived'].value_counts(), "\n")
print("Pclass:\n", df_train['Pclass'].value_counts(), "\n")
print("Sex:\n", df_train['Sex'].value_counts(), "\n")

# -------------------------------------
# b. PAIRPLOT & HEATMAP
# -------------------------------------
# Pairplot with selected numeric columns
sns.pairplot(df_train[['Survived', 'Pclass', 'Age', 'Fare']].dropna(), hue='Survived')
plt.suptitle("Pairplot of Survived, Pclass, Age, Fare", y=1.02)
plt.show()

# Heatmap of correlation
plt.figure(figsize=(10, 6))
sns.heatmap(df_train.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# -------------------------------------
# c. RELATIONSHIPS & TRENDS (Example)
# -------------------------------------
# Survival by sex
sns.countplot(x='Sex', hue='Survived', data=df_train)
plt.title("Survival Count by Sex")
plt.show()

# Survival by Pclass
sns.countplot(x='Pclass', hue='Survived', data=df_train)
plt.title("Survival Count by Passenger Class")
plt.show()

# -------------------------------------
# d. HISTOGRAMS, BOXPLOTS, SCATTERPLOTS
# -------------------------------------
# Histogram: Age distribution
df_train['Age'].hist(bins=30, edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Boxplot: Age vs Survived
sns.boxplot(x='Survived', y='Age', data=df_train)
plt.title("Age vs Survival")
plt.show()

# Scatterplot: Age vs Fare colored by Survival
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df_train)
plt.title("Fare vs Age (colored by Survived)")
plt.show()

# -------------------------------------
# e. OBSERVATIONS (add to Markdown cell if using Jupyter)
# -------------------------------------
print("\n=== Observations ===")
print("""
1. Age and Fare are positively correlated with survival probability.
2. Females had much higher survival rates than males.
3. 1st class passengers were more likely to survive.
4. Younger passengers (children) had better survival rates.
5. Many missing values in 'Age' and 'Cabin' columns.
""")

# -------------------------------------
# f. SUMMARY OF FINDINGS
# -------------------------------------
print("\n=== Summary of Findings ===")
print("""
- Survival Rate: {:.2f}%
- Majority of passengers did not survive.
- High Fare, Female Gender, and 1st Class are associated with better survival chances.
- Age, Fare, and Class show meaningful trends with survival.
""".format(df_train['Survived'].mean() * 100))