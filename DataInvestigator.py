import pandas as pd

class DataInvestigator:

    def __init__(self, df):
        self.df = df

    def baseline(self, col):
        return self.zeroR(col)

    def corr(self, col1, col2):
        return self.df.iloc[:,col1].corr(self.df.iloc[:,col2])

    def zeroR(self, col):
        return self.df.iloc[:,col].mode()[0]


if __name__ == "__main__":
    df = pd.read_csv('gallstone.csv')
    di = DataInvestigator(df)
    print(di.baseline(1))
