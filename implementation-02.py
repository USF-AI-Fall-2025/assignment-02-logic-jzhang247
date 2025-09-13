import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# For gender
df = pd.read_csv("gallstone.csv")
for col in ["Weight", "Height", "Intracellular Water (ICW)", "Bone Mass (BM)", "Muscle Mass (MM)"]:
    # Using age as x-axis just in case males are younger than females
    sns.scatterplot(data=df, x="Age", y=col, hue="Gender")
    plt.title(col)
    plt.show()

# For glucose
df_all = pd.read_csv("gallstone.csv")
column_name = "Glucose"

Q1 = df_all[column_name].quantile(0.25)
Q3 = df_all[column_name].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(f"Normal range: {lower_bound} ~ {upper_bound}")
df_normal = df_all[(df_all[column_name] >= lower_bound) & (df_all[column_name] <= upper_bound)]
print(stats.shapiro(df_normal[column_name]))
print(stats.anderson(df_normal[column_name], dist="norm"))

for df, name in [(df_all, "All"), (df_normal, "Filtered")]:
    sns.histplot(df[column_name], bins=100)
    plt.title(name)
    plt.show()

    plt.figure()
    stats.probplot(df[column_name], dist="norm", plot=plt)
    plt.title(name)
    plt.show()
