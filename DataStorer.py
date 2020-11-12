class  DataStorerClass:
    import pandas as pd
    
    def insertUserData(self,userData):
        df = pd.DataFrame()
        df.append(userData,ignore_index=True)
        df.to_excel('./SecureData.xlsx',sheet_name='Úsers', index=False)
