import json
import pandas as pd

def convert_col_to_list(df:pd.DataFrame, col_name:str, new_col_name:str = "") -> pd.DataFrame:
    """
    Converts every row of a column in a pandas DataFrame into a list containing
    strings delimited by a semi-colon.
    
    Args:
        df (pandas.DataFrame): The DataFrame containing the column to be converted.
        col_name (str): The name of the column to be converted.
        new_col_name (str): The new name of the column to be converted. Defaults to original name
    
    Returns:
        pandas.DataFrame: A new DataFrame with the converted column.
    """
    if new_col_name == "": new_col_name = col_name
    
    df[new_col_name] = df[col_name].apply(lambda x: str(x).strip().split(";"))
    
    return df

def load_spreadsheet_as_intents(df:pd.DataFrame, new_filename:str = "intents.json") -> None:
    """
    Writes to a file a DataFrame as a json object

    Args:
        df (pandas.DataFrame) : The dataframe to be written to the file
        new_filename (str) : The name of the file, Default = intents.json
    """
    df = convert_col_to_list(df, "patterns")
    df = convert_col_to_list(df, "responses")

    res_df = pd.DataFrame().assign(tag = df["tag"], patterns = df['patterns'], responses = df['responses'], context_set = "")

    json_df = res_df.to_json(orient = "table", index = False)

    parsed_df = json.loads(json_df)

    json_obj = json.dumps(parsed_df, indent = 4)

    with open("intents.json", 'w') as f:
        f.write(json_obj)

    with open("intents.json", 'r') as f:
        obj = json.load(f)

    intents = obj['data']

    res = {"intents" : intents}

    with open(new_filename, 'w') as f:
        f.write(json.dumps(res, indent=4))


def get_intents(url:str, new_filename:str = "intents.json") -> None:
   """
    Will generate new intents file from specified spreadsheet url

    Args:
        url (str): url containing the spreadsheet to load
        new_filename (srt): name of intents file, Default = intents.json
   """

   df = pd.read_csv(url)

   load_spreadsheet_as_intents(df, new_filename=new_filename)

def get_creds(path_to_credentials:str):
    pass



if __name__ == "__main__":
   SPREADSHEET = "https://docs.google.com/spreadsheets/d/1m51HUH0AQi28EBnsLwP9gasUHPuLVzFuNu1L4N6Zs-Y/gviz/tq?tqx=out:csv&sheet=Question+and+Answers_new"

   get_intents(url= SPREADSHEET)