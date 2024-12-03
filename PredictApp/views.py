from django.shortcuts import render
from django.http import JsonResponse

import os
import sys
sys.path.append(os.path.dirname(__file__))

from predict_model.code.preprocessing import preprocess_text
from predict_model.code.preparing_nlp import prepare_nlp
from predict_model.code.modeling import classify



# Create your views here.
def input_data(request):
    if request.method == "GET":
        return render(request, 'PredictApp/input_form.html')
    else:
        return JsonResponse({'Error': 'Only GET method is allowed.'}, status=405)

def predict_result(request):
    if request.method == "POST":
        input_text = request.POST.get('input_text', '')

        if input_text:
            after_preprocess = preprocess_text([input_text])
            after_prepare = prepare_nlp(after_preprocess)
            after_classify = classify(after_prepare)

            context = '분류 결과: ' + after_classify[0][0] + '\n' + \
                '해당 확률은 ' + '{:.2f}%'.format(after_classify[0][1].item() * 100) + \
                '입니다.'

            return render(request, 'PredictApp/predict_result.html', {'결과': context})
        else:
            return JsonResponse({'Error': 'Input text is empty.'}, status=400)
    else:
        return JsonResponse({'Error': 'Only POST method is allowed.'}, status=405)


