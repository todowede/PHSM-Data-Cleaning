import pandas

def stats(data):
    """
    Print basic statistics of the input master file.
    Args:
        
        data: master file
    
    Returns:
    
        Count of total records
        count of non-cleansing data
        count of records for cleaning
    """
    data = pandas.read_csv(data)
    total_recor ds = data.shape[0]
    total_columns = data.shape[1]
    
    print(f'Master file has {total_records} records and {total_columns} columns.')
    
