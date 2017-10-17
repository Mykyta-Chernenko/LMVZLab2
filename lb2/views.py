from django.shortcuts import render_to_response, get_object_or_404, HttpResponse

from chartit import DataPool, Chart

from .models import Proportion


def page1(request):
    proportions = Proportion.objects.all()
    sexes = proportions.order_by().values_list('sex', flat=True).distinct()
    heights = proportions.order_by().values_list('height', flat=True).distinct()
    return render_to_response('page1.html', {'sexes': sexes, 'heights': heights})


def get_weight(request):
    height = request.GET['height']
    sex = request.GET['sex']
    weight = get_object_or_404(Proportion, height=height, sex=sex).weight
    return HttpResponse(f'<p class="btn alert-info btn-block">Оптимальный вес: {weight} </p>')


def page2(request):
    weatherdata = \
        DataPool(
            series=
            [{'options': {
                'source': Proportion.objects.filter(sex='Мужской')},
                'terms': [
                    {'Мужской рост': 'height'},
                    {'Идеальный мужской вес': 'weight'}
                ]}, {'options': {
                'source': Proportion.objects.filter(sex='Женский')},
                'terms': [
                    {'Женский рост': 'height'},
                    {'Идеальный женский вес': 'weight'}]}
            ])

    # Step 2: Create the Chart object
    cht = Chart(
        datasource=weatherdata,
        series_options=
        [{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
                'Мужской рост': [
                    'Идеальный мужской вес'], 'Женский рост': ['Идеальный женский вес']
            }}],
        chart_options=
        {'title': {
            'text': 'Пропорции'},
            'xAxis': {
                'title': {
                    'text': 'Рост'}}})

    # Step 3: Send the chart object to the template.
    return render_to_response('page2.html', {'proportions': cht})


def page3(request):
    return render_to_response('page3.html', {'men_proportions': Proportion.objects.filter(sex='Мужской'),'women_proportions': Proportion.objects.filter(sex='Женский')})


def page4(request):
    return render_to_response('page4.html',{'men_proportions': list(Proportion.objects.filter(sex='Мужской').values_list('weight',flat=True)),
                                            'women_proportions': list(Proportion.objects.filter(sex='Женский').values_list('weight',flat=True))})
