import pandas as pd
import csv
import glob

#  Data URL's
url = 'intentions_conv.csv'
url_muestras = '05 ESTADISTICAS DE QUERYS.xlsx'
url_gen = 'intentions_gen.csv'
url_query = 'query.csv'

folder_path = 'queries_pocasm/'
output_file = 'for_statistics.csv'


def create_csv_file(query):
    if query != None:
        #  Create a dataframe the pandas
        df_query= pd.DataFrame(query, columns=['Query'])
        # Save the DataFrame in to a csv file
        df_query.to_csv('int_query.csv', index=False)
    return df_query['Query']

def get_conv_csv_file(url):
    conv_int = []
    with open(url, 'r') as file_csv:
        df_csv = csv.reader(file_csv)
        for row in df_csv:
            conv_int += row
    return conv_int[1:-1]


def get_gen_csv_file(url_gen):
    gen_int = []
    with open(url_gen, 'r') as file_csv:
        df_csv = csv.reader(file_csv)
        for row in df_csv:
            gen_int += row
    return gen_int[1:-1]

def get_query_csv_file(url_query):
    query = []
    with open(url_query, 'r') as file_csv:
        df_csv = csv.reader(file_csv)
        for row in df_csv:
            query += row
    return query[1:-1]

# Return all questions make to llama in the file "Estadisticas de QUERYS.xlsx "
def read_xlsx_file():
    question = []
    df_query = pd.read_excel('05 ESTADISTICAS DE QUERYS.xlsx', sheet_name='QUERY')
    for row in df_query.iterrows():
        if row != 'nan':
            question.append(row[1][1])
    return question


def get_statistics():
    csv_files = glob.glob(folder_path + '*.csv')
    with open(folder_path + output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for csv_file in csv_files:
            with open(csv_file, 'r') as infile:
                reader = csv.reader(infile)
                for row in reader:
                    writer.writerow(row)



if __name__ == '__main__':
    # get_query_csv_file(url_query)
    # get_conv_csv_file(url)
    # get_gen_csv_file(url_gen)
    # read_xlsx_file()
    # print(create_csv_file(query))
    print(get_statistics())


# conversacional = [conv for conv in get_conv_csv_file(url)]
# consulta = [query for query in get_query_csv_file(url_query)]
# generational = [gen for gen in get_gen_csv_file(url_gen)]
# sentencia  = [ question for question in read_xlsx_file()]