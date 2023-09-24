from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Member,Service,Plans,Review

def index(request):
    srec=Service.objects.all()
    prec=Plans.objects.all()
    vrec=Review.objects.all()
    return render(request,"index.html",{"srec":srec, "prec":prec, "vrec":vrec})

# Create your views here.
def reg(request):
    if request.method=="POST":
        f=request.POST.get('fullname')
        m=request.POST.get('email')
        p=request.POST.get('pno')
        u=request.POST.get('username')
        l=request.POST.get('password')
        sa=Member(fname=f,email=m,phone=p,uname=u,pw=l)
        sa.save()
    return render(request,"regester.html")
def log(request):
    if request.method == "POST":
        s=request.POST.get('usern')
        w=request.POST.get('pass')
        mrec= Member.objects.filter(uname=s,pw=w)
        if mrec.filter(uname=s,pw=w).exists():
            for j in mrec:
                fn=j.fname
                ph=j.phone
                id=j.id
            request.session['id']=id
            request.session['fname']=fn
            request.session['phone']= ph
            request.session['usern']=s
            request.session['pass']=w
            srec = Service.objects.all()
            prec = Plans.objects.all()
            vrec = Review.objects.all()
            return render(request, "userpage.html",{"srec":srec, "prec":prec, "vrec":vrec,})

        else:
            return render(request,"notfound.html")
    return render(request,"login.html")


def frogot(request):
    if request.method == "POST":
        email = request.POST.get("email")
        newpass = request.POST.get("t1")
        confrmpass = request.POST.get("t2")

        try:
            member = Member.objects.get(email=email)
        except Member.DoesNotExist:
            return render(request, "forgot.html")

        if newpass == confrmpass:
            member.pw = newpass
            member.save()
            return render(request, "index.html")
        else:
            return render(request, "forgot.html")

    # Add this return statement for when request.method is not "POST"
    return render(request, "forgot.html")


def contact(request):
    return render(request, "contactus.html")

