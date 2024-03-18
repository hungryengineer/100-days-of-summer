dict = {
    "student": ["A", "B"],
    "score": [50,60]
}
# print(dict)
import pandas

df = pandas.DataFrame(dict)
for i,j in df.iterrows():
    print(j.score)
# print(df)