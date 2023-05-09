import pandas as pd


def get_first_four(d):
    ''' date -> string '''
    s = str(d)
    s = s[:4]
    return s


def main():
    print('long way...')
    # import dataframe from excel
    df = pd.read_excel('./test.xlsx', sheet_name='Sheet1', engine="openpyxl")
    print(df)

    # convert date to string and get first 4 characters
    df['Date_Str_First4'] = df['Created_Date'].apply(lambda d: str(d)[:4])
    print(df)
    
    # filter using the dataframe method
    b = (df['Date_Str_First4'] == '2023')
    df_2023 = df[b]
    print(df_2023)

    print('single line...')    
    # import dataframe from excel
    df = pd.read_excel('./test.xlsx', sheet_name='Sheet1', engine="openpyxl")

    # filter where it is '2023' and reassign df
    # df = df[(df['Created_Date'].apply(lambda s: s[:4]) == '2023')]
    # df = df[(df['Created_Date'].apply(get_first_four) == '2023')]
    # df = df[(df['Created_Date'].apply(lambda d: get_first_four(d)) == '2023')]
    df = df[(df['Created_Date'].apply(lambda d: str(d)[:4]) == '2023')]
    print(df)
    
    return None
    
    
if __name__ == '__main__':
    main()
