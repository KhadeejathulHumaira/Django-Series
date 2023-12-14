from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges={
    "january":"Jan Task",
    "february":"Feb task",
    "march":"March task",
    "april":"April task",
    "may":"May task",
    "june":None,
    "july":"july task",
    "august":"August task",
    "september":"Sep task",
    "october":"Oct task",
    "november":None,
    "december":"Dec task"

}
# Create your views here.

def index(request):
    months=list(monthly_challenges.keys()) 
    return render(request,"challenges/index.html",{
        "months":months
    })

def monthly_challenge_by_number(request,month): 
    try:
        months=list(monthly_challenges.keys())
        forward_month=months[month-1]
        # print(forward_month)
        # This will redirect the path
        # return HttpResponseRedirect("/challenges/"+forward_month)
        redirect_url=reverse("monthly-string",args=[forward_month])
        return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound("<h1>This is not supported!!</h1>")
    

def monthly_challenge(request,month):
    try:
        task_name=monthly_challenges[month]
        print(task_name)
        # redirect_html=f"<h1>{task_name}</h1>"
        # redirect_html=render_to_string("challenges/challenge.html")
        # return HttpResponse(redirect_html)
        return render(request,"challenges/challenge.html",{
            "task":task_name,
            "month":month
        })
    except:
        # return HttpResponseNotFound("<h1>This is not a month</h1>")
        response_data=render_to_string( "404.html")
        return HttpResponseNotFound(response_data)
        

    
    
