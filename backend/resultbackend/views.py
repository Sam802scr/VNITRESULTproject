from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count 
from .models import ResultColumn

def get_grade_distribution(request):
    selected_course = request.GET.get('course')
    
    if selected_course:
        results = ResultColumn.objects.filter(course=selected_course)
        
        grade_counts = results.values('grade').annotate(count=Count('grade'))
        data = {item['grade']: item['count'] for item in grade_counts}

        return JsonResponse(data)
    return JsonResponse({'error': 'No course selected'})

# Create your views here.
