from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import UserSubmission, SubmissionDetail
from adminideabajet.models import Lokasi, Elemen1, Elemen2, Elemen3, Elemen4, Elemen5, Elemen6, Elemen7, Elemen8, Aset
import json

def user_home(request):
    """Main user interface page"""
    context = {
        'lokasi_data': Lokasi.objects.all(),
        'e1_data': Elemen1.objects.all(),
        'e2_data': Elemen2.objects.all(),
        'e3_data': Elemen3.objects.all(),
        'e4_data': Elemen4.objects.all(),
        'e5_data': Elemen5.objects.all(),
        'e6_data': Elemen6.objects.all(),
        'e7_data': Elemen7.objects.all(),
        'e8_data': Elemen8.objects.all(),
        'aset_data': Aset.objects.all(),
    }
    return render(request, 'userideabajet/user_home.html', context)

def get_aset_by_elemen5(request):
    """AJAX endpoint to get aset filtered by elemen5"""
    elemen5_id = request.GET.get('elemen5_id')
    if elemen5_id:
        aset_list = Aset.objects.filter(elemen5_id=elemen5_id)
        data = [{'asetid': aset.asetid, 'list_aset': aset.list_aset} for aset in aset_list]
        return JsonResponse({'aset': data})
    return JsonResponse({'aset': []})

@csrf_exempt
@require_http_methods(["POST"])
def submit_budget_idea(request):
    """Handle budget idea submission"""
    try:
        data = json.loads(request.body)
        
        # Create new submission
        submission = UserSubmission.objects.create(
            name=data.get('name', ''),
            email=data.get('email', ''),
            jantina=data.get('jantina', ''),
            bangsa=data.get('bangsa', ''),
            umur=data.get('umur', ''),
            job=data.get('job', ''),
            zon=data.get('zon', ''),
            cad=data.get('cad', '')
        )
        
        # Process submission details for each element
        for element_num in range(1, 9):
            pilihan_key = f'pilihan_{element_num}'
            lokasi_key = f'lokasi_{element_num}'
            butiran_key = f'butiran_{element_num}'
            
            if pilihan_key in data and isinstance(data[pilihan_key], list):
                for i, pilihan in enumerate(data[pilihan_key]):
                    if pilihan:  # Only create if pilihan is not empty
                        lokasi = data.get(lokasi_key, [])[i] if i < len(data.get(lokasi_key, [])) else ''
                        butiran = data.get(butiran_key, [])[i] if i < len(data.get(butiran_key, [])) else ''
                        
                        SubmissionDetail.objects.create(
                            submission=submission,
                            element_number=element_num,
                            pilihan=pilihan,
                            lokasi=lokasi,
                            butiran=butiran
                        )
        
        return JsonResponse({
            'success': True,
            'message': 'Cadangan bajet berjaya dihantar!',
            'submission_id': submission.submission_id
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Ralat: {str(e)}'
        }, status=400)

def submission_status(request, submission_id):
    """Check submission status"""
    try:
        submission = UserSubmission.objects.get(submission_id=submission_id)
        return render(request, 'userideabajet/submission_status.html', {
            'submission': submission
        })
    except UserSubmission.DoesNotExist:
        messages.error(request, 'Cadangan tidak dijumpai.')
        return redirect('user_home')
