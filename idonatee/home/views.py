from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Signupp,Detail,Rdetail,Odetail,Hdetail,Detail2,Quick,Rdetail2

# Create your views here.
#global val


def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        role=request.POST['role']

        global val
        def val():
            return username



        if Signupp.objects.filter(username=username,email=email):
            messages.error(request,"User already exist")
            return render(request,"log.html")
            

        #messages.success(request,"Your account has created successfully")
        myprofile=Signupp(username=username,email=email,password=password,role=role)
        myprofile.save()
        messages.success(request,"Your account has created successfully")
        

        #return render(request,"details.html")

        dongli=Signupp.objects.all()
        flag=0


        for i in dongli:
            #if i.confirmpassword==confirmpassword and i.password==password:
            if role=='Organisation User':
                return render(request,"odetails.html")
            if role=='Hospital User':
                return render(request,"hdetails.html")
            if role=='Donor User':
                return render(request,"ddetails.html")
            if role=='Receiver User':
                return render(request,"rdetails.html")
            

            
        
            flag=1
            username = val()
                
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
            if i.username==username and i.password==password :
                if i.role=='Receiver User':
                    flag=1
                    global val
                    def val():
                        return username
                
                    return render(request,"rdashboard.html")
                if i.role=='Donor User':
                    flag=1
                    #global val
                    def val():
                        return username
                
                    return render(request,"dashboard.html")
                if i.role=='Hospital User':
                    flag=1
                    #global val
                    def val():
                        return username
                
                    return render(request,"hdashboard.html")
                if i.role=='Organisation User':
                    flag=1
                    #global val
                    def val():
                        return username
                
                    return render(request,"odashboard.html")
        if flag==0:
            messages.error(request,"Wrong Credentials")
            return redirect('home')

    return render(request,"log.html")

def adminlogin(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        #credential=Signupp.objects.all()
        flag=0
        #for i in credential:
        if username==username and password==password:
                flag=1
                global val
                def val():
                    return username
                return render(request,"admindash.html")
        if flag==0:
            messages.error(request,"Wrong Credentials")
            return redirect('home')

    return render(request,"adminlogin.html")

def admin_home(request):
    return render(request,"admindash.html")



def signout(request):
    messages.success(request,"Logged Out successfully!")
    return redirect('home')

def dashboard(request):
    return render(request,"dashboard.html")

def rdashboard(request):
    return render(request,"rdashboard.html")

def odashboard(request):
    return render(request,"odashboard.html")

def hdashboard(request):
    return render(request,"hdashboard.html")

def qdashboard(request):
    return render(request,"qdashboard.html")


def admindash(request):
    return render(request,"admindash.html")

def admdonar(request):
    return render(request,"admdonar.html")

def admrec(request):
    return render(request,"admrec.html")

def admorg(request):
    return render(request,"admorg.html")

def admhos(request):
    return render(request,"admhos.html")

def detail(request):
    def val(username):
        return username
    
    if request.method == "POST":
        fullname = request.POST['fullname']
        dob = request.POST['dob']
        email = request.POST['email']
        mobno = request.POST['mobno']
        ge = request.POST['ge']
        age = request.POST['age']
        bg = request.POST['bg']
        address = request.POST['address']
        occupation = request.POST['occupation']
        weight = request.POST['weight']
        height = request.POST['height']
        an = request.POST['an']
        tmr = request.POST['tmr']
        ldd = request.POST['ldd']
        dbo = request.POST['dbo']
        if len(request.FILES) != 0:
            image = request.FILES['image']

        username = val(request.user.username)

        #messages.success(request, "Your account has created successfully")
        det = Detail(username=username, fullname=fullname, dob=dob, email=email, mobno=mobno, ge=ge, age=age, bg=bg, address=address, occupation=occupation, weight=weight, height=height, an=an, tmr=tmr, ldd=ldd, dbo=dbo, image=image)
        det.save()
        messages.success(request, "Details added successfully")
        return render(request, "details2.html")
    
    return render(request, "ddetails.html")


    

def rdetail(request):
    def val():
        return request.user.username
        
    if request.method == "POST":
        fname = request.POST['fname']
        rdob = request.POST['rdob']
        remail = request.POST['remail']
        rmobno = request.POST['rmobno']
        rge = request.POST['rge']
        rage = request.POST['rage']
        rbg = request.POST['rbg']
        raddress = request.POST['raddress']
        roccupation = request.POST['roccupation']
        rweight = request.POST['rweight']
        rheight = request.POST['rheight']
        ran = request.POST['ran']
        rtmr = request.POST['rtmr']
        rlrd = request.POST['rlrd']
        rdbo = request.POST['rdbo']
        
        if len(request.FILES) != 0:
            rimage = request.FILES['rimage']
        else:
            rimage = None

        username = val()

        rdet = Rdetail(username=username, fname=fname, rdob=rdob, remail=remail, rmobno=rmobno, rge=rge, rage=rage, rbg=rbg, raddress=raddress, roccupation=roccupation, rweight=rweight, rheight=rheight, ran=ran, rtmr=rtmr, rlrd=rlrd, rdbo=rdbo, rimage=rimage)
        rdet.save()
        messages.success(request, "Details added successfully")
        return render(request, "rdetail2.html")
    
    return render(request, "rdetails.html")



def odetail(request):
    if request.method == "POST":
        ofname = request.POST['ofname']
        oemail = request.POST['oemail']
        omobno = request.POST['omobno']
        oaddress = request.POST['oaddress']
        if len(request.FILES) != 0:
            oimage = request.FILES['oimage']

        username = request.user.username

        # messages.success(request,"Your account has created successfully")
        odet = Odetail(username=username, ofname=ofname, oemail=oemail, omobno=omobno, oaddress=oaddress, oimage=oimage)
        odet.save()
        messages.success(request, "Details added successfully")
        return render(request, "odashboard.html")

    def val():
        return request.user.username

    return render(request, "odetails.html")


def hdetail(request):
    if request.method == "POST":
        hfname = request.POST['hfname']
        hid = request.POST['hid']
        hemail = request.POST['hemail']
        hmobno = request.POST['hmobno']
        haddress = request.POST['haddress']
        bbp = request.POST['bbp']
        obp = request.POST['obp']
        if len(request.FILES) != 0:
            himage = request.FILES['himage']

        username = request.user.username

        # messages.success(request,"Your account has created successfully")
        hdet = Hdetail(username=username, hfname=hfname, hid=hid, hemail=hemail, hmobno=hmobno, haddress=haddress, bbp=bbp, obp=obp, himage=himage)
        hdet.save()
        messages.success(request, "Details added successfully")
        return render(request, "hdashboard.html")

    def val():
        return request.user.username

    return render(request, "hdetails.html")



def detail2(request):
    def val(username):
        return username
    
    if request.method == "POST":
        sid = request.POST['sid']
        eidn = request.POST['eidn']
        if len(request.FILES) != 0:
            dsbg = request.FILES['dsbg']

        username = val(request.user.username)

        #messages.success(request, "Your account has created successfully")
        det2 = Detail2(username=username, sid=sid, eidn=eidn, dsbg=dsbg)
        det2.save()
        messages.success(request, "Details added successfully")
        return render(request, "dashboard.html")
    
    return render(request, "details2.html")



def rdetail2(request):
    if request.method == "POST":
        rsid = request.POST['rsid']
        reidn = request.POST['reidn']
        if len(request.FILES) != 0:
            rdsbg = request.FILES['rdsbg']

        rdet2 = Rdetail2.objects.create(rsid=rsid, reidn=reidn, rdsbg=rdsbg, username=request.user.username)

        messages.success(request, "Details added successfully")
        return render(request, "rdashboard.html")
    
    return render(request, "rdetail2.html")


def quick(request):
    if request.method=="POST":
        qfname=request.POST['qfname']
        qdob=request.POST['qdob']
        qemail=request.POST['qemail']
        qmobno=request.POST['qmobno']
        qge=request.POST['qge']
        qage=request.POST['qage']
        qbg=request.POST['qbg']
        qweight=request.POST['qweight']
        qheight=request.POST['qheight']
        qan=request.POST['qan']
        qtmr=request.POST['qtmr']
        qidtype=request.POST['qidtype']
        if len(request.FILES) !=0:
            qimage=request.FILES['qimage']
        
    

        #messages.success(request,"Your account has created successfully")
        detq=Quick(qfname=qfname,qdob=qdob,qemail=qemail,qmobno=qmobno,qge=qge,qage=qage,qbg=qbg,qweight=qweight,qheight=qheight,qan=qan,qtmr=qtmr,qidtype=qidtype,qimage=qimage)
        detq.save()
        messages.success(request,"Details added successfully")
        return render(request,"qdashboard.html")
    return render(request, "quick.html")


def profile(request):
    username=val()
    user_profile=Detail.objects.all()
    for i in user_profile:
        if username==i.username:
            break
    return render(request,'profile.html',{'i':i})

def rprofile(request):
    username=val()
    user_profile=Rdetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break
    return render(request,'rprofile.html',{'i':i})

def admdonreq(request):
    # username = request.POST.get('username', '')
    un = Signupp.objects.all()
    up = Detail.objects.all()
    up1 = Detail2.objects.all()
    return render(request, 'admdonreq.html', {'un': un, 'up': up, 'up1': up1})

# def admdonreq(request):
#     signups = Signupp.objects.all()
#     detail = Detail.objects.all()
#     return render(request, 'admdonreq.html', {'signups': signups,'detail':detail})


def admrecreq(request):
    # username=val()
    rd=Rdetail.objects.all()
    rd1=Detail2.objects.all()
    return render(request,'admrecreq.html',{'rd':rd,'rd1':rd1})

def qrec(request):
    # username=val()
    i=Rdetail.objects.all()
    return render(request,'qrec.html',{'i':i})

def qorg(request):
    # username=val()
    org=Odetail.objects.all()
    return render(request,'qorg.html',{'org':org})

def qhos(request):
    # username=val()
    hos=Hdetail.objects.all()
    return render(request,'qhos.html',{'hos':hos})

def dsearch(request):
    # username=val()
    dsear=Rdetail.objects.all()
    return render(request,'dsearch.html',{'dsear':dsear})

def admorgreq(request):
    # username=val()
    org=Odetail.objects.all()
    return render(request,'admorgreq.html',{'org':org})

def admhosreq(request):
    # username=val()
    hos=Hdetail.objects.all()
    return render(request,'admhosreq.html',{'hos':hos})

