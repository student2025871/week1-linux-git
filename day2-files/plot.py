import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("top20.csv")
plt.figure(figsize=(10,6))
sns.barplot(
    data=df,
    x="GDP (BILLIONS)",
    y="COUNTRY",
    palette="viridis"
)
plt.title("Top 20 GDP Countries (2014)")
plt.tight_layout()
plt.savefig("top20.png")
print("✅ 已生成 top20.png")
