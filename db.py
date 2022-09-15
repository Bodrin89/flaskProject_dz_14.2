import sqlite3


def get_by_data(a, list_select, *args):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = a.format(*args)
        cursor.execute(query)
        result = cursor.fetchall()

        list_result = []
        for i in range(len(result)):
            dict_data = dict(zip(list_select, result[i]))
            list_result.append(dict_data)

    return list_result


