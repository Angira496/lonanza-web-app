# for email
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
#######################################

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from joblib import load
mymodel=load("mysite/loanpredlogm.joblib")

def home(request):
    return render(request, "index.html")

def ourteam(request):
    return render(request, "ourteam.html")

def predict(request):
    return render(request, "predict.html")

def contact(request):
    return render(request, "contact.html")

def model_accuracy(request):
    return render(request, "model_accuracy.html")

def analysis(request):
    return render(request, "analysis.html")

def result(request):
    a=request.POST['self-employed']
    b=request.POST['applicant-income']
    c=request.POST['loan-amount']
    d=request.POST['loan-term']
    e=request.POST['credit-history']
    f=request.POST['property-area']

    arr=[[a,b,c,d,e,f]]
    outp=mymodel.predict(arr)

    #return HttpResponse(a+" "+b+" "+c+" "+d+" "+e+" "+f)
    return render(request, "result.html",{'approved':outp[0]})
    return render(request, "result.html",{'rejected':outp[1]})


def about(request):
    e=request.POST['exp']
    inp = [[e]]
    yp = mymodel.predict(inp)
    return HttpResponse(yp)


def myui(request):
    return render(request, "ui.html")

def myapi(request):
    return JsonResponse({'djangomsg' : 'I am from Django Cloud'})


######## email
def send_email(request):
    if request.method == 'POST':
        # Collect form data from POST
        name = request.POST.get('name')
        sender_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_body = request.POST.get('message')

        # Build the full message content
        full_message = f"Message from {name} ({sender_email}):\n\n{message_body}"

        try:
            send_mail(
                subject,                             # Email subject
                full_message,                        # Email body
                settings.DEFAULT_FROM_EMAIL,         # Sender from settings.py
                ['gnitprojectweather@gmail.com'],    # Recipient
                fail_silently=False,                 # Raise exception on error
            )
        except Exception as e:
            # Log the exception (you can also add additional error handling here)
            print("Email sending failed:", e)

        # Redirect to the blank "test.html" page after processing the email
        return redirect('test')
    else:
        # If the request is not POST, redirect back to the contact page.
        return redirect('contact')


def test_page(request):
    # Render the blank test.html page.
    return render(request, 'test.html')