from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Min, Max, Sum
from webserver.models import LoadedData
from sklearn.cluster import KMeans
from django.http import JsonResponse
from django.conf import settings
import numpy as np

import io
import pandas as pd
import sqlite3
import json


def get_classes(request):
    result = list(LoadedData.objects.values_list('tmp_class', flat=True).distinct())
    return JsonResponse(result, safe=False)


def get_atributes(request):
    result = [f.name for f in LoadedData._meta.get_fields()]
    return JsonResponse(result[3:-1], safe=False)


def get_classes_atributes(request):
    result = {}
    result['classes'] = list(LoadedData.objects.values_list('tmp_class', flat=True).distinct())
    result['atributes'] = [f.name for f in LoadedData._meta.get_fields()][3:-1]
    return JsonResponse(result, safe=False)


def get_boxplot_data(request):
    con = sqlite3.connect(settings.DATABASES['default']['NAME'])
    column_name = ['class', 'attribute', 'avg', 'min', 'max', 'q1', 'q3']
    response = []
    df = pd.read_sql_query('''SELECT * FROM boxplot''', con)
    columns = df.columns
    for i, j in df.iterrows():
        for clm in columns:
            response += [[j["class"], j['attribute'], j['avg'], j['min'], j['max'], j['q1'], j['q3']]]

    response = pd.DataFrame(response, columns=column_name)

    return HttpResponse(response.to_csv(index=False), content_type='text/csv')


def get_heatmap_data(request):
    con = sqlite3.connect(settings.DATABASES['default']['NAME'])
    column_name = ['variable', 'group', 'value']
    response = []
    df = pd.read_sql_query('''SELECT * FROM heat_map''', con)
    columns = df.columns[:-2]
    for i, j in df.iterrows():
        for clm in columns:
            if clm == 'Event_length':
                continue
            response += [[j["tmp_class"], clm, j[clm]]]

    response = pd.DataFrame(response, columns=column_name)

    return HttpResponse(response.to_csv(index=False), content_type='text/csv')


def heatmap(request):
    return render(request, 'heatmap.html')


def boxplot(request):
    return render(request, 'boxplot.html')


def index(request):
    return render(request, 'base.html')


@csrf_exempt
def loadData(request):
    if request.is_ajax():
        if request.method == 'POST':
            try:
                data_set = request.FILES['file'].read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                dataFrame = pd.read_csv(io_string, delimiter='\t')
                dataFrame['tmp_class'] = request.POST['name_of_class']
                dataFrame['file_name'] = request.POST['fileName']
                dataFrame['k_mean'] = None
                con = sqlite3.connect(settings.DATABASES['default']['NAME'])
                dataFrame.to_sql('loaded_data', con, if_exists='append', index=False)
                # for column in csv_reader:
                #     print('Raw Data: "%s"' % column)
                con.close()
                return HttpResponse(201)
            except Exception as e:
                print(e)
                raise Http404()
    return HttpResponse(201)


def normalize(all_objects):
    sum_avg = sum(obj['value']['avg'] for obj in all_objects)
    sum_max = sum(obj['value']['max'] for obj in all_objects)
    sum_min = sum(obj['value']['min'] for obj in all_objects)
    sum_q1 = sum(obj['value']['q1'] for obj in all_objects)
    sum_q3 = sum(obj['value']['q3'] for obj in all_objects)
    for obj in all_objects:
        obj['value']['avg'] = obj['value']['avg'] / sum_avg
        obj['value']['max'] = obj['value']['max'] / sum_max
        obj['value']['min'] = obj['value']['min'] / sum_min
        obj['value']['q1'] = obj['value']['q1'] / sum_q1
        obj['value']['q3'] = obj['value']['q3'] / sum_q3
    return all_objects


def get_first_quantile(df):
    first_quantile = df.quantile(.25)
    return float(first_quantile)


def get_third_quantile(df):
    third_quantile = df.quantile(.75)
    return float(third_quantile)


def get_average(df):
    average = df.mean()
    return float(average)


def get_max(df):
    max = df.max()
    return float(max)


def get_min(df):
    min = df.min()
    return float(min)


def get_all_data(request):
    try:
        all_objects = []
        current_class = ''
        field_names = [field.name for field in LoadedData._meta.get_fields()]
        for field in field_names:
            if field == 'index' or field == 'viability' or field == 'event_length' or field == 'time':
                field_names.remove(field)
                continue
            attribute_data = {}
            data_dict = LoadedData.objects.values(field)
            if field == 'tmp_class':
                attribute_data['class'] = list(data_dict[0].values())[0]
                all_objects.append(attribute_data)
                current_class = attribute_data['class']
                continue
            sum_of_field = list(LoadedData.objects.aggregate(Sum(str(field))).values())[0]
            raw_data = []
            raw_data = raw_data + [(list(d.values())[0] / sum_of_field if sum_of_field != 0 else 0) for d in data_dict]
            attribute_data['key'] = field
            attribute_data['value'] = {'avg': get_average(raw_data), 'min': get_min(raw_data), 'max': get_max(raw_data),
                                       'q1': get_first_quantile(raw_data), 'q3': get_third_quantile(raw_data)}
            # print(field)
            # print(attribute_data)
            all_objects.append(attribute_data)
        field_names.remove('time')
        field_names.remove('viability')
        # print(all_objects)
        # normalize values
        # all_objects = normalize(all_objects)
        return JsonResponse(json.dumps([field_names, all_objects]), safe=False)
    except Exception as e_rror:
        print('Error: ' + str(e_rror))
        return HttpResponse('Error: ' + str(500) + str(e_rror))


@csrf_exempt
def cleanData(request):
    if request.is_ajax():
        if request.method == 'POST':
            try:
                con = sqlite3.connect(settings.DATABASES['default']['NAME'])
                name = request.POST['name']
                if name == 'all':
                    con.execute('''DELETE FROM loaded_data''')
                    con.commit()
                    con.close()
                else:
                    con.execute("DELETE FROM loaded_data WHERE tmp_class==\"" + name + "\"")
                    con.commit()
                    con.close()
                return HttpResponse(201)
            except Exception as e:
                print('Error: ' + e)
            raise Http404()
    return HttpResponse(201)


def loadedData(request):
    if request.is_ajax():
        if request.method == 'GET':
            con = sqlite3.connect(settings.DATABASES['default']['NAME'])
            df = pd.read_sql_query('''SELECT file_name, tmp_class FROM loaded_data GROUP BY tmp_class''', con)
            response = []
            for name, class_name in df.to_numpy():
                response += [{"name": name, "tmp_class": class_name}]
            con.close()

            return JsonResponse(response, safe=False)
    raise Http404()


def tmpClasses(request):
    if True or request.is_ajax():
        if request.method == 'GET':
            con = sqlite3.connect(settings.DATABASES['default']['NAME'])
            df = pd.read_sql_query(
                '''SELECT tmp_class, tmp_color FROM clusters WHERE length(tmp_class) > 0 GROUP BY tmp_class ''', con)
            response = []
            for tmp_class, tmp_color in df.to_numpy():
                response += [{"tmp_class": tmp_class, "tmp_color": tmp_color}]
            con.close()

            return JsonResponse(response, safe=False)
    raise Http404()


def scatter_plot(request):
    return render(request, 'scatter_plot.html')


def tree(request, type_data):
    con = sqlite3.connect(settings.DATABASES['default']['NAME'])
    result = []
    if type_data == "tSNE":
        frac = 0.02
    else:
        frac = 0.02
    df: pd.DataFrame = pd.read_sql_query('''SELECT l.*, c.tmp_color
                              FROM loaded_data as l
                                JOIN clusters as c ON l.k_mean = c."index"
                              ORDER BY c.tmp_color desc;''', con).sample(frac=frac)
    for x in range(1, 4):
        quant = np.quantile(df[type_data + "_" + str(x)], [0.01, 0.99])
        df[type_data + "_" + str(x)][df[type_data + "_" + str(x)] < quant[0]] = quant[0]
        df[type_data + "_" + str(x)][df[type_data + "_" + str(x)] > quant[1]] = quant[1]
        df[type_data + "_" + str(x)] += abs(quant[0])
        df[type_data + "_" + str(x)] /= quant[1]
        df[type_data + "_" + str(x)] *= 200
        df[type_data + "_" + str(x)] -= 100

    df = json.dumps(json.loads(df.reset_index().to_json(orient='records')), indent=2)

    con.close()
    return render(request, 'three.html',
                  context={'my_data': df, 'axes': [type_data + "_" + str(x) for x in range(1, 4)]})


def analyzeData(request):
    con = sqlite3.connect(settings.DATABASES['default']['NAME'])
    df = pd.read_sql_query('''SELECT * FROM loaded_data''', con, index_col='index')

    columns = [x for x in df.columns[1:][df.columns[1:] != object]]
    # print(columns)

    for column in df.columns[1:]:
        if df[column].dtype != object:
            data = df[column]
            columns += [column]
            quantile = data.quantile([.1, .99]).values
            data = data.where(data > quantile[0])
            data = data.where(data < quantile[-1])
            df[column] = (data - quantile[0]) / (quantile[-1] - quantile[0]) * 500

    rows = []
    boxplot_rows = []
    for tmp_class in df.tmp_class.unique():
        row = {}
        row["tmp_class"] = tmp_class
        data_class = df[df['tmp_class'] == tmp_class]
        row["file_name"] = data_class.iloc[0]["file_name"]
        for column in df.columns[1:]:
            boxplot_data = {}
            if df[column].dtype != object:
                data = data_class[column]
                data = data[data > 0]
                row[column] = data.mean()
                boxplot_data['class'] = tmp_class
                boxplot_data['attribute'] = column
                boxplot_data['avg'] = get_average(data)
                boxplot_data['min'] = get_min(data)
                boxplot_data['max'] = get_max(data)
                boxplot_data['q1'] = get_first_quantile(data)
                boxplot_data['q3'] = get_third_quantile(data)
                print(boxplot_data)
                boxplot_rows.append(boxplot_data)
        rows.append(row)

    # for rowb in boxplot_rows:
    #     print(rowb)

    heatmap_df = pd.DataFrame(rows)
    boxplot_df = pd.DataFrame(boxplot_rows)

    heatmap_df.to_sql('heat_map', con, if_exists='replace', index=True)
    k_means(con)
    boxplot_df.to_sql('boxplot', con, if_exists='replace', index=True)
    con.close()

    return HttpResponse(201)


def k_means(con: sqlite3.Connection):
    df = pd.read_sql_query(
        '''SELECT "index", CD34, CD10, CD19, CD27, IgM, IgD, CD138, CD20, CD22, IgG, IgA, CD38, CD45 FROM loaded_data''',
        con, index_col="index")
    print(df.head(10))
    kmean = KMeans(n_clusters=500)
    print(np.shape(df.to_numpy()[::5, :]))
    kmean.fit(df.to_numpy()[::5, :])
    clusters = pd.DataFrame(kmean.cluster_centers_,
                            columns=["CD34", "CD10", "CD19", "CD27", "IgM", "IgD", "CD138", "CD20", "CD22", "IgG",
                                     "IgA", "CD38", "CD45"])
    clusters["tmp_class"] = ''
    clusters["tmp_color"] = ''
    clusters["have_class"] = 125
    print(clusters)
    clusters.to_sql('clusters', con, if_exists='replace', index=True)
    df["prediction"] = kmean.predict(df.to_numpy())

    con.executemany("UPDATE loaded_data SET k_mean = ? WHERE \"index\" == ? ",
                    [(data["prediction"], int(i)) for i, data in df.iterrows()])

    con.commit()

    return None


def get_scatter_data(request):
    con = sqlite3.connect(settings.DATABASES['default']['NAME'])
    df = pd.read_sql_query('''SELECT * FROM clusters''', con, index_col="index")
    con.close()
    return HttpResponse(df.to_csv(index=True), content_type='text/csv')


@csrf_exempt
def postCluster(request):
    if request.is_ajax():
        if request.method == 'POST':
            con = sqlite3.connect(settings.DATABASES['default']['NAME'])

            data = json.loads(request.POST["data"])
            name_color = data[-1]
            name, color = name_color["name"], name_color["color"]
            for row in data[:-1]:
                command = "UPDATE clusters SET " \
                          "tmp_class = \'" + name + "\', have_class = \'" + str(
                    500) + "\', tmp_color = \'" + color + "\'" + " WHERE \"index\" == " + str(row['index'])
                con.execute(command)
                con.commit()
            return HttpResponse('Success')

    return Http404()


@csrf_exempt
def cleanClass(request):
    if request.is_ajax():
        if request.method == 'POST':
            try:
                con = sqlite3.connect(settings.DATABASES['default']['NAME'])
                tmp_class = request.POST['tmp_class']

                command = "UPDATE clusters SET " \
                          "tmp_class = \'\', have_class = 125, tmp_color = \'\'" + " WHERE tmp_class == \"" + tmp_class + "\""
                con.execute(command)
                con.commit()
                con.close()

                return HttpResponse(201)
            except Exception as e:
                print('Error: ', e)
            raise Http404()
    return HttpResponse(201)
