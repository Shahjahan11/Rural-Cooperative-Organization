
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import InterestForm
from .models import Interest
from django.http import JsonResponse
from django.http import HttpResponseBadRequest


def INTEREST(request):
    if request.method == 'POST':
        form = InterestForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('InteresT')  # Redirect to the expense page after submission
    else:
        form = InterestForm()

    interests = Interest.objects.all()

    return  render(request,'Interest/Interest.html', {'form': form, 'interests': interests})


def edit_interest(request, interest_id):
    
    try:
        interest = Interest.objects.get(pk=interest_id)
        interest.person = request.POST.get('productCode')
        interest.description = request.POST.get('product')
        interest.date = request.POST.get('qty')
        interest.amount = request.POST.get('perPrice')
        interest.save()
        return JsonResponse({'status': 'success', 'message': 'Interest updated successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f'Error: {str(e)}'})



def delete_interest(request, interest_id):
    try:
        interest = Interest.objects.get(pk=interest_id)
        print(f"Deleting interest: {interest}")
        interest.delete()
        return JsonResponse({'status': 'success', 'message': 'Interest deleted successfully'})
    except Exception as e:
        print(f"Error deleting interest: {e}")
        return JsonResponse({'status': 'error', 'message': str(e)})
