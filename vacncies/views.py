import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from vacncies.models import Vacancy


# Create your views here.

def hello(request):
    return HttpResponse("hello world")



@method_decorator(csrf_exempt, name='dispatch')
class VacancyView(View):
    def get(self, request):

            vacncies = Vacancy.objects.all()
            search_text = request.GET.get("text", None)

            if search_text:
                vacncies = vacncies.filter(text=search_text)

            response = []
            for vacancy in vacncies:
                response.append({
                    "id":vacancy.id,
                    "text": vacancy.text
                })

            return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        vacancy_data = json.loads(request.body)

        vacancy = Vacancy()
        vacancy.text = vacancy_data['text']

        vacancy.save()

        return JsonResponse({
                "id":vacancy.id,
                "text": vacancy.text
            })

class VacancyDetailView(DetailView):
    model = Vacancy
    def get(self, request, *args, **kwargs):
        vacancy = self.get_object()
        return  JsonResponse({
            "id": vacancy.id,
            "text": vacancy.text
        })



