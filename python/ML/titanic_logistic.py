import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("./datasets/titanic/train.csv", index_col="PassengerId")
print(df.head())
print(df.info())
print(df.describe())

# Pclass: 1= 1등석, 2=2등석 ...
# Survived: 1:생존 0:사망
# Sex : male, female
# SibSp: siblings/spouses(형제, 배우자)
# Parch : parents / children(부모님, 자녀)

# 탐색적 데이터 분석(EDA, Exploratory Data Analysis)
# 분석 기법을 적용하기 위해서는 데이터의 척도체크가 중요함
# 질적척도 중
# - 명목척도: 관찰하는 대상의 속에 따라 그 값을 숫자로 나타냄
#             연구대상을 구분하거나 분류할 목적으로 숫자를 사용 (ex 남자:1 여자:2)

# - 서열척도: 관찰하는 대상의 특성을 측정해서 그 값을 순위로 나타내는 것
#             (성적1등, 2등, 3등) 높낮이는 알 수 있지만 어느정도 차이인지 알 수 없음

# 양적척도 중
# -등간척도 : 관찰대상의 속성을 상대적 크기로 나타냄
#             순위를 부여할 뿐만 아니라 어느정도 큰 지 숫자간의 의미가 있음
#             (ex온도) 가산이 가능함. 하지만 절대적이지 않음
# -비율척도: 절대적 기준이 있는 영점이 존재하고 모든 사칙연산이 가능
#            연구대상의 차이를 비교할 수 있으며 순위를 만들 수 있음(판매량, 점수)


# 널 값 체크
print(df.isnull().sum())
# null 값이 있으면 해당 값의 평균값으로 대체하는게 일반적인 방법
# 성별 나이 평균
print(df.groupby('Sex')['Age'].mean())
# 생존, 사망인원수
print(df['Survived'].value_counts())
df['Survived_label'] = (
    df['Survived'].replace(0, 'Dead').replace(1,'Survived'))
print(df['Survived_label'].value_counts())
# df['Survived_label'].value_counts().plot(kind='pie', autopct="%1.2f%%")
# plt.xlabel("Survived_label")
# plt.ylabel('Count')
# plt.show()
df['Pclass_label'] = df['Pclass'].replace(1,'First').replace(2,'Business').replace(3,'economy')
# df['Pclass_label'].value_counts().plot(kind='pie',autopct='%1.2f%%')
# plt.show()

#pip install seaborn
import seaborn as sns
#sns.countplot(data=df, x='Pclass_label', hue='Survived_label')
#plt.show()
# df['Age'].hist(bins=10, figsize=(10,5), grid=False, edgecolor='black', color='yellowgreen')
# plt.show()
sns.countplot(x='Age', hue='Survived', data=df)
plt.show()