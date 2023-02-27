from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Signupp,Detail,Rdetail,Odetail,Detail2

# Create your views here.


def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        role=request.POST['role']



        if Signupp.objects.filter(username=username,email=email):
            
            return render(request,"log.html")
            messages.error(request,"User already exist")

        #messages.success(request,"Your account has created successfully")
        myprofile=Signupp(username=username,email=email,password=password,confirmpassword=confirmpassword,role=role)
        myprofile.save()
        messages.success(request,"Your account has created successfully")
        

        #return render(request,"details.html")

        credentials=Signupp.objects.all()
        flag=0
        
        for i in credentials:
            if i.confirmpassword==confirmpassword and i.password==password:
                for j in credentials:
                    if j.role=='Donor User':
                        return render(request,"ddetails.html")
                    if j.role=='Receiver User':
                        return render(request,"rdetails.html")
                    if j.role=='Organisation User':
                        return render(request,"odetails.html")
                    if j.role=='Organisation User':
                        return render(request,"hdetails.html")
                flag=1
                global val
                def val():
                    return username
                #return render(request,"ddetails.html")
        if flag==0:
            messages.error(request,"Wrong Credentials")
            return redirect('home')
    
    return render(request,"signup.html")

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        credential=Signupp.objects.all()
        flag=0
        for i in credential:
            if i.username==username and i.password==password:
                flag=1
                
                def val():
                    return username
                return render(request,"dashboard.html")
        if flag==0:
            messages.error(request,"Wrong Credentials")
            return redirect('home')

    return render(request,"log.html")

def signout(request):
    messages.success(request,"Logged Out successfully!")
    return redirect('home')

def dashboard(request):
    return render(request,"dashboard.html")

def detail(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        dob=request.POST['dob']
        email=request.POST['email']
        mobno=request.POST['mobno']
        ge=request.POST['ge']
        age=request.POST['age']
        bg=request.POST['bg']
        address=request.POST['address']
        occupation=request.POST['occupation']
        weight=request.POST['weight']
        height=request.POST['height']
        an=request.POST['an']
        tmr=request.POST['tmr']
        ldd=request.POST['ldd']
        dbo=request.POST['dbo']
        if len(request.FILES) !=0:
            image=request.FILES['image']

        username=val()

        #messages.success(request,"Your account has created successfully")
        det=Detail(username=username,fullname=fullname,dob=dob,email=email,mobno=mobno,ge=ge,age=age,bg=bg,address=address,occupation=occupation,weight=weight,height=height,an=an,tmr=tmr,ldd=ldd,dbo=dbo,image=image)
        det.save()
        messages.success(request,"Details added successfully")
        return render(request,"details2.html")
        

    return render(request, "ddetails.html")

def rdetail(request):
    if request.method=="POST":
        fname=request.POST['fname']
        rdob=request.POST['rdob']
        remail=request.POST['remail']
        rmobno=request.POST['rmobno']
        rge=request.POST['rge']
        rage=request.POST['rage']
        rbg=request.POST['rbg']
        raddress=request.POST['raddress']
        roccupation=request.POST['roccupation']
        rweight=request.POST['rweight']
        rheight=request.POST['rheight']
        ran=request.POST['ran']
        rtmr=request.POST['rtmr']
        rldd=request.POST['rldd']
        rdbo=request.POST['rdbo']
        if len(request.FILES) !=0:
            rimage=request.FILES['rimage']

        username=val()

        #messages.success(request,"Your account has created successfully")
        rdet=Rdetail(username=username,fname=fname,rdob=rdob,remail=remail,rmobno=rmobno,rge=rge,rage=rage,rbg=rbg,raddress=raddress,roccupation=roccupation,rweight=rweight,rheight=rheight,ran=ran,rtmr=rtmr,rldd=rldd,rdbo=rdbo,rimage=rimage)
        rdet.save()
        messages.success(request,"Details added successfully")
        return render(request,"details2.html")
        

    return render(request, "rdetails.html")


def odetail(request):
    if request.method=="POST":
        ofname=request.POST['ofname']
        oemail=request.POST['oemail']
        omobno=request.POST['omobno']
        oaddress=request.POST['oaddress']
        if len(request.FILES) !=0:
            oimage=request.FILES['oimage']

        username=val()

        #messages.success(request,"Your account has created successfully")
        odet=Odetail(username=username,ofname=ofname,oemail=oemail,omobno=omobno,oaddress=oaddress,oimage=oimage)
        odet.save()
        messages.success(request,"Details added successfully")
        return render(request,"dashboard.html")
        

    return render(request, "odetails.html")



def detail2(request):
    if request.method=="POST":
        sid=request.POST['sid']
        eidn=request.POST['eidn']
        if len(request.FILES) !=0:
            dsbg=request.FILES['dsbg']

        username=val()

        #messages.success(request,"Your account has created successfully")
        det2=Detail2(username=username,sid=sid,eidn=eidn,dsbg=dsbg)
        det2.save()
        messages.success(request,"Details added successfully")
        return render(request,"dashboard.html")
        

    return render(request, "details2.html")



