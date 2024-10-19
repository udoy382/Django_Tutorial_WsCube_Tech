from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UsersForm
from math import floor
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from forms.models import Forms
from card.models import Card
from django.core.mail import send_mail, EmailMultiAlternatives

def home(request):
    subject = "Testing Mail"
    form_email = "srudoy436@gmail.com"
    msg = "<p>Hi! My name is <b>Saifur Rahman Udoy</b></p>"
    to = "udoy436@gmail.com"

    msg = EmailMultiAlternatives(subject, msg, form_email, [to])
    msg.content_subtype = "html"
    msg.send()


    # send_mail(
    #     "Testing Mail",
    #     "Hi! This is testing mail from SMTP",
    #     "srudoy436@gmail.com",
    #     ["udoy436@gmail.com"],
    #     fail_silently=False,
    # )


    newsData = News.objects.all()
    serviceData = Service.objects.all()
    # serviceData = Service.objects.all().order_by("-service_title")
    # serviceData = Service.objects.all().order_by("-service_title")[:1]
    # data = {
    #     'title': 'Home page',
    #     'name': 'Saifur Rahman Udoy',
    #     'courseList': ["Python", "Java", "JavaScript", "PHP", 'Sql Injection', "C++"],
    #     'student_details':[
    #         {"name":"Saifur Rahman Udoy", "phone":"01782299436", "study":"Inter first year"},
    #         {"name":"Dipty Shopnil Sara", "phone":"019999999", "study":"Ten"}
    #     ],
    #     'numbers':[10, 20, 30, 40, 50]
    # }


    paginator = Paginator(serviceData, 2)
    page_number = request.GET.get('page')
    serviceDataFinal = paginator.get_page(page_number)
    total_page = serviceDataFinal.paginator.num_pages


    if request.method=="GET":
        st = request.GET.get('servicename')
        if st != None:
            serviceData = Service.objects.filter(service_title=st)

    data = {
        'serviceData':serviceDataFinal,
        'newsData':newsData,
        'last_page':total_page,
        'total_page_list':[n+1 for n in range(total_page)]
    }

    return render(request, "index.html", data)

def aboutUs(request):
    cardData = Card.objects.all()

    data = {
        "cardData":cardData
    }
    
    return render(request, "about.html", data)

def contectUs(request):
    finalAns = {}
    fn = UsersForm()
    data = {'form':fn}
    try:
        if request.method=="POST": # or  "GET"
            # name = request.GET["name"]
            # email = request.GET["email"]
            # password = request.GET["password"]
            # print(f"User name is '{name}' email is '{email}' and password is '{password}'")
            # finalAns = name, email, password

            name = request.POST["name"]
            email = request.POST["email"]
            password = request.POST["password"]
            print(f"User name is '{name}' email is '{email}' and password is '{password}'")
            finalAns = name, email, password
            data = {
                'form':fn,
                "name":name,
                "email":email,
                "password":password,
                "output":finalAns
            }
            return HttpResponseRedirect("/about/", data)
    except:
        pass
    return render(request, "contect.html", data) # {"output":finalAns},

def course(request):
    return render(request, "course.html")

def courseDetaild(request, courseid):
    return HttpResponse(courseid)
  
def submitform(request):
    try:
        if request.method=="POST": # or  "GET"
            name = request.POST["name"]
            email = request.POST["email"]
            password = request.POST["password"]
            print(f"User name is '{name}' email is '{email}' and password is '{password}'")
            finalAns = name, email, password
            data = {
                "name":name,
                "email":email,
                "password":password,
                "output":finalAns
            }
            return HttpResponse("Hey there!")
    except:
        pass


def calculator(request):
    c = ""
    try:
        if request.method == "POST":
            num1 = eval(request.POST.get('num1'))
            num2 = eval(request.POST.get('num2'))
            operator = request.POST.get('operator')

            if operator == "+":
                c = num1 + num2
            elif operator == "-":
                c = num1 - num2
            elif operator == "*":
                c = num1 * num2
            elif operator == "/":
                c = num1 / num2
    except:
        c = "Invalid Operations. Please try again..."
    
    print(c)

    return render(request, "calculator.html", {"c":c})


# def even_odd(request):
#     c = ""
#     try:
#         if request.method == "POST":
#             n = int(request.POST.get("n"))
#             if n%2 == 0:
#                 c = "Even Number"
#             else:
#                 c = "Odd Number"
#     except:
#         c = "Oops! Something Problem. Please Try again"


#     return render(request, "even_odd.html", {"answare":c})



def even_odd(request):
    c = ""
    if request.method == "POST":
        if request.POST.get("n") == "":
            return render(request, "even_odd.html", {"error":True})
        n = int(request.POST.get("n"))
        if n%2 == 0:
            c = "Even Number"
        else:
            c = "Odd Number"


    return render(request, "even_odd.html", {"answare":c})


def marksheet(request):
    mrk = {'total': 0, 'per': 0, 'div':0}  # Initialize with default values
    try:
        if request.method == "POST":
            s1 = eval(request.POST.get("s1"))
            s2 = eval(request.POST.get("s2"))
            s3 = eval(request.POST.get("s3"))
            s4 = eval(request.POST.get("s4"))
            s5 = eval(request.POST.get("s5"))
            t = s1 + s2 + s3 + s4 + s5
            p = t * 100 / 500
            
            if p >= 60:
                d = "First Div"
            elif p >= 48:
                d = "Second Div"
            elif p >= 35:
                d = "Third Div"
            else:
                d = "Fail"
            mrk = {
                'total': t,
                'per': p,
                'div':d
            }
    except:
        pass
    return render(request, "marksheet.html", mrk)


def news(request, slug):
    news = News.objects.get(news_slug=slug)
    data = {
        'news':news
    }
    return render(request, "news.html", data)


def forms(request):
    send_mail(
        "Testing Mail",
        "Hi! This is testing mail from SMTP",
        "srudoy436@gmail.com",
        ["udoy436@gmail.com"],
        fail_silently=False,
    )
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        en = Forms(user_name=name, user_email=email, user_password=password)
        en.save()

        form_email = "srudoy436@gmail.com"
        msg = "<p>Hi! My name is <b>Saifur Rahman Udoy</b></p>"

        msg = EmailMultiAlternatives(name, msg, form_email, [email])
        msg.content_subtype = "html"
        msg.send()

    return render(request, "forms.html")