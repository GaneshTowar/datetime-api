from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from datetime import date,datetime
def datetym(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = date.today()
    #Dtime = "todays date: " +str(current_time)+ "      "  +"current time : "+ str(current_date)
    Dtime = {
        "date": current_date,
        "time": current_time,
    }

    json_data = JSONRenderer().render(Dtime)
    return HttpResponse(json_data, content_type='application/json')
