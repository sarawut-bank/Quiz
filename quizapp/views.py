from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from .models import Leavelist

def index(request):

    if request.method == 'POST':
        name = request.POST['name']
        surename = request.POST['surename']
        position = request.POST['position']
        email = request.POST['email']
        phone = request.POST['phone']
        type_leave = request.POST['type_leave']
        cause = request.POST['cause']
        date_first = request.POST['date_first']
        date_end = request.POST['date_end']
        status = "รอพิจารณา"
        date_save = timezone.now()
        del_flg = 0

        new_data = Leavelist(name=name, surename=surename, position=position, email=email, phone=phone, type_leave=type_leave, cause=cause, date_first=date_first, date_end=date_end, status=status, date_save=date_save, del_flg=del_flg)
        new_data.save()

        return redirect('success')

    return render(request, 'index.html')

def delete_data(request):
    del_flg = 1
    new_data = Leavelist(del_flg=del_flg)
    new_data.save()

    return redirect('alldata')

def success(request):
    return render(request, 'success.html')

def allData(request):
    data = Leavelist.objects.filter(status="รอพิจารณา",del_flg=0).order_by('-id')
    context = {
        'data': data,
    }
    return render(request, 'alldata.html',context)

@csrf_exempt
def approve_status(request, data_id):
    return update_status(request, data_id, 1)  # 1 คือสถานะอนุมัติ

@csrf_exempt
def reject_status(request, data_id):
    return update_status(request, data_id, 2)  # 2 คือสถานะไม่อนุมัติ

def update_status(request, data_id, new_status):
    if request.method == "POST":
        try:
            data_to_update = Leavelist.objects.get(id=data_id)
            data_to_update.status = new_status
            data_to_update.save()
            return JsonResponse({"message": "อัปเดตสถานะสำเร็จ"}, status=200)
        except Leavelist.DoesNotExist:
            return JsonResponse({"message": "ไม่พบข้อมูล"}, status=404)
    return JsonResponse({"message": "ไม่อนุญาตให้เข้าถึง"}, status=403)

# def success(request):
#     desired_value = 'ผ่าน'
#     latest_data = AllData.objects.latest('id')
#     count_pass = 0
#     for field_name in ['eye_color', 'eye_length', 'eye_astigmatism', 'body_response']:
#         if getattr(latest_data, field_name) == desired_value:
#             count_pass += 1
#     result = 'ผ่าน' if count_pass > 2 else 'ไม่ผ่าน'

#     columns_to_check = ['signs_traffic', 'lines_traffic', 'give_way']
#     max_score = 50

#     # คำนวณเปอร์เซ็นต์สำหรับแต่ละคอลัมน์
#     percentages = {}
#     for field_name in columns_to_check:
#         score = getattr(latest_data, field_name)
#         percentage = (score / max_score) * 100
#         percentages[field_name] = floatformat(percentage, 2)

#     # คำนวณเปอร์เซ็นต์เฉลี่ย
#     average_percentage = sum(float(percentages[field_name]) for field_name in columns_to_check) / len(columns_to_check)
#     percent_result = 'ผ่าน' if average_percentage >= 80 else 'ไม่ผ่าน'

#     status_work = latest_data.status_work
#     nameData = latest_data
#     context = {
#         'result': result,
#         'percent_result': percent_result,
#         'average_percentage': floatformat(average_percentage, 2),
#         'status_work': status_work,
#         'nameData': nameData
#     }

#     return render(request, 'success.html', context)
