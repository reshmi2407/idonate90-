from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Signupp,Detail,Rdetail,Odetail,Hdetail,Detail2,Quick

# Create your views here.
global val


def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        role=request.POST['role']

        def val():
            return username



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
                if i.role=='Donor User':
                    return render(request,"ddetails.html")
                if i.role=='Receiver User':
                    return render(request,"rdetails.html")
                if i.role=='Organisation User':
                    return render(request,"odetails.html")
                if i.role=='Hospital User':
                    return render(request,"hdetails.html")
                flag=1
                username = val()
                
                return render(request,"ddetails.html")
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
    def val():
        return username
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
    def val():
        return username
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


def hdetail(request):
    if request.method=="POST":
        hfname=request.POST['hfname']
        hid=request.POST['hid']
        hemail=request.POST['hemail']
        hmobno=request.POST['hmobno']
        haddress=request.POST['haddress']
        bbp=request.POST['bbp']
        obp=request.POST['obp']
        if len(request.FILES) !=0:
            himage=request.FILES['himage']

        username=val()

        #messages.success(request,"Your account has created successfully")
        hdet=Hdetail(username=username,hfname=hfname,hid=hid,hemail=hemail,hmobno=hmobno,haddress=haddress,bbp=bbp,obp=obp,himage=himage)
        hdet.save()
        messages.success(request,"Details added successfully")
        return render(request,"dashboard.html")
        

    return render(request, "hdetails.html")


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


def quick(request):
    if request.method=="POST":
        qfname=request.POST['qfname']
        qdob=request.POST['qdob']
        qemail=request.POST['qemail']
        qmobno=request.POST['qmobno']
        qge=request.POST['qge']
        qage=request.POST['qage']
        qbg=request.POST['qbg']
        qaddress=request.POST['qaddress']
        qweight=request.POST['qweight']
        qheight=request.POST['qheight']
        qan=request.POST['qan']
        qtmr=request.POST['qtmr']
        qidtype=request.POST['qidtype']
        if len(request.FILES) !=0:
            qimage=request.FILES['qimage']

        username=val()

        #messages.success(request,"Your account has created successfully")
        det=Detail(username=username,qfname=qfname,qdob=qdob,qemail=qemail,qmobno=qmobno,qge=qge,qage=qage,qbg=qbg,qaddress=qaddress,qweight=qweight,qheight=qheight,qan=qan,qtmr=qtmr,qidtype=qidtype,qimage=qimage)
        det.save()
        messages.success(request,"Details added successfully")
        return render(request,"dashboard.html")
    return render(request, "quick.html")


