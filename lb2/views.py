from django.shortcuts import render_to_response, get_object_or_404, HttpResponse

from lb2.models import Proportion


def page1(request):
    proportions = Proportion.objects.all()
    sexes =proportions.order_by().values_list('sex',flat=True).distinct()
    heights = proportions.order_by().values_list('height',flat=True).distinct()
    return render_to_response('page1.html',{'sexes':sexes,'heights':heights})
def get_weight(request):
    height = request.GET['height']
    sex = request.GET['sex']
    weight = get_object_or_404(Proportion,height=height,sex=sex).weight
    return HttpResponse(f'<p class="btn alert-info btn-block">Оптимальный вес: {weight} </p>')
def page2(request):
    pass
def page3(request):
    pass
def page4(request):
    pass