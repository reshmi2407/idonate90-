from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Signupp,Detail,Rdetail,Odetail,Odetail2,Hdetail,Hdetail2,Detail2,Quick,Rdetail2,Edit

# Create your views here.
#global val

global val
def home(request):
    return render(request, "index.html")
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        role=request.POST['role']

        if Signupp.objects.filter(username=username).exists() or Signupp.objects.filter(email=email).exists():
            # messages.error(request,"User already exists")
            return render(request,"log.html")
            
        myprofile=Signupp(username=username,email=email,password=password,role=role)
        myprofile.save()
        # messages.success(request,"Your account has been created successfully")
        global val
        def val():
            return username
        if role=='Organisation User':
            return render(request,"odetails.html")
        elif role=='Hospital User':
            return render(request,"hdetails.html")
        elif role=='Donor User':
            return render(request,"ddetails.html")
        elif role=='Receiver User':
            return render(request,"rdetails.html")
        else:
            # messages.error(request,"Invalid Role")
            return redirect('home')
    
    return render(request,"signup.html")

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        global val
        def val():
            return username
        credential=Signupp.objects.all()
        flag=0
        for i in credential:
            if i.username==username and i.password==password :
                if i.role=='Receiver User':
                    flag=1
                    
                    def val():
                        return username
                
                    return render(request,"rdashboard.html")
                if i.role=='Donor User':
                    flag=1
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
            # messages.error(request,"Wrong Credentials")
            return redirect('home')

    return render(request,"log.html")

def adminlogin(request):
    def val():
        return username

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == 'idonate' and password == 'idonate':
            username = val()
            return render(request, "admindash.html")
        else:
            context = {
                'error_message': 'Wrong Credentials'
            }
            return render(request, 'index.html', context)

    return render(request, "adminlogin.html")



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

        username=val()
        #messages.success(request, "Your account has created successfully")
        det = Detail(username=username, fullname=fullname, dob=dob, email=email, mobno=mobno, ge=ge, age=age, bg=bg, address=address, occupation=occupation, weight=weight, height=height, an=an, tmr=tmr, ldd=ldd, dbo=dbo, image=image)
        det.save()
        messages.success(request, "Details added successfully")
        return render(request, "details2.html")
    
    return render(request, "ddetails.html")

def edit(request):
    if request.method == "POST":
        don_edit_email = request.POST['don_edit_email']
        don_edit_mobno = request.POST['don_edit_mobno']
        don_edit_address = request.POST['don_edit_address']
        don_edit_occupation = request.POST['don_edit_occupation']
        don_edit_weight = request.POST['don_edit_weight']
        don_edit_height = request.POST['don_edit_height']
        don_edit_an = request.POST['don_edit_an']
        don_edit_tmr = request.POST['don_edit_tmr']
        don_edit_ldd = request.POST['don_edit_ldd']
        don_edit_sid = request.POST['don_edit_sid']
        don_edit_eidn = request.POST['don_edit_eidn']
        if len(request.FILES) != 0:
            don_edit_dsbg = request.FILES['don_edit_dsbg']
        username=val()
        #messages.success(request, "Your account has created successfully")
        edit = Edit(don_edit_email = don_edit_email,don_edit_mobno = don_edit_mobno,don_edit_address = don_edit_address,don_edit_occupation = don_edit_occupation,don_edit_weight = don_edit_weight,don_edit_height = don_edit_height,don_edit_an = don_edit_an,don_edit_tmr=don_edit_tmr,don_edit_ldd = don_edit_ldd,don_edit_sid = don_edit_sid,don_edit_eidn = don_edit_eidn,don_edit_dsbg = don_edit_dsbg)
        edit.save()
        messages.success(request, "Details added successfully")
        return render(request, "dashboard.html")
    
    return render(request, "edit.html")

    

def rdetail(request):
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

        username=val()


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

        username=val()

        # messages.success(request,"Your account has created successfully")
        odet = Odetail(username=username, ofname=ofname, oemail=oemail, omobno=omobno, oaddress=oaddress, oimage=oimage)
        odet.save()
        # messages.success(request, "Details added successfully")
        return render(request, "odetail2.html")

    return render(request, "odetails.html")


def odetail2(request):
    if request.method == "POST":
        olicenceid = request.POST['olicenceid']
        if len(request.FILES) != 0:
            oiimage = request.FILES['oiimage']

        username=val()

        # messages.success(request,"Your account has created successfully")
        odet2 = Odetail2(username=username, olicenceid=olicenceid ,oiimage=oiimage)
        odet2.save()
        #messages.success(request, "Details added successfully")
        return render(request, "odashboard.html")

    return render(request, "odetail2.html")

def oprofile(request):

    username=val()
    user_profile=Odetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Odetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'oprofile.html',{'i':i,'j':j})

def oidentity(request):
    username=val()
    user_profile=Odetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Odetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'oidentity.html',{'i':i,'j':j})

def orgsearch(request, username):
    r_p = Odetail.objects.filter(username=username).first()
    r2_p = Odetail2.objects.filter(username=username).first()
    return render(request, 'oprofile.html', {'i': r_p,'j':r2_p})

def orgidentity(request, username):
    r_p = Odetail.objects.filter(username=username).first()
    r2_p = Odetail2.objects.filter(username=username).first()
    return render(request, 'oidentity.html', {'i': r_p,'j':r2_p})

def admorgreq(request):

    up = Odetail.objects.all()
    up1 = Odetail2.objects.all()
    return render(request, 'admorgreq.html', {'up': up, 'up1': up1})



def hdetail(request):
    if request.method == "POST":
        hfname = request.POST['hfname']
        hemail = request.POST['hemail']
        hmobno = request.POST['hmobno']
        haddress = request.POST['haddress']
        bbp = request.POST['bbp']
        obp = request.POST['obp']
        if len(request.FILES) != 0:
            himage = request.FILES['himage']

        username=val()

        # messages.success(request,"Your account has created successfully")
        hdet = Hdetail(username=username, hfname=hfname, hemail=hemail, hmobno=hmobno, haddress=haddress, bbp=bbp, obp=obp, himage=himage)
        hdet.save()
        messages.success(request, "Details added successfully")
        return render(request, "hdetail2.html")

    return render(request, "hdetails.html")


def hdetail2(request):
    if request.method == "POST":
        hlicenceid = request.POST['hlicenceid']
        if len(request.FILES) != 0:
            hiimage = request.FILES['hiimage']

        username=val()

        # messages.success(request,"Your account has created successfully")
        hdet2 = Hdetail2(username=username, hlicenceid=hlicenceid ,hiimage=hiimage)
        hdet2.save()
        #messages.success(request, "Details added successfully")
        return render(request, "hdashboard.html")

    return render(request, "hdetail2.html")



def detail2(request):
    username=val()

    if request.method == "POST":
        sid = request.POST['sid']
        eidn = request.POST['eidn']
        if len(request.FILES) != 0:
            dsbg = request.FILES['dsbg']
        
        username=val()

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

        username=val()


        rdet2 = Rdetail2(username=username, rsid=rsid, reidn=reidn, rdsbg=rdsbg)
        rdet2.save()
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

    user_details=Detail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'profile.html',{'i':i,'j':j})



def didentity(request):
    username=val()
    user_profile=Detail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Detail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'didentity.html',{'i':i,'j':j})


def donidentity(request, username):
    d_p = Detail.objects.filter(username=username).first()
    d2_p=Detail2.objects.filter(username=username).first()
    return render(request, 'didentity.html', {'i': d_p,'j':d2_p})


def rprofile(request):

    username=val()
    user_profile=Rdetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Rdetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'rprofile.html',{'i':i,'j':j})

def ridentity(request):

    username=val()
    user_profile=Rdetail.objects.all()
    for i in user_profile:
        if username==i.username:
            break

    user_details=Rdetail2.objects.all()
    for j in user_details:
        if username==j.username:
            break
    return render(request,'ridentity.html',{'i':i,'j':j})

def recidentity(request, username):
    r_p = Rdetail.objects.filter(username=username).first()
    r2_p = Rdetail2.objects.filter(username=username).first()
    return render(request, 'ridentity.html', {'i': r_p,'j':r2_p})



def recsearch(request, username):
    r_p = Rdetail.objects.filter(username=username).first()
    r2_p = Rdetail2.objects.filter(username=username).first()
    return render(request, 'rprofile.html', {'i': r_p,'j':r2_p})




def donacceptreject(request, username):
    def don_delete_user_data(username):
        try:
            user_detail = Detail.objects.filter(username=username).first()

            if user_detail:
                user_detail.delete()

            user_signup = Signupp.objects.filter(username=username).first()

            if user_signup:
                user_signup.delete()

            user_detail2 = Detail2.objects.filter(username=username).first()

            if user_detail2:
                user_detail2.delete()

            
            return True

        except Exception as e:
            # Handle any exceptions that may occur
            print(e)
            return False

    d_p = Detail.objects.filter(username=username).first()
    if request.method == "POST":
        status = request.POST.get("password")
        if status == "reject":
            if don_delete_user_data(username):
                messages.success(request, "User data deleted successfully.")
            else:
                messages.error(request, "Error deleting user data.")
            signup = Signupp.objects.filter(username=username).first()
            if signup:
                signup.delete()
            else:
                messages.error(request, "Signup not found.")
            return redirect("/admdonar")
        elif status == "accept":
            # Handle the accept case here
            pass  # replace this with your code
    return render(request, 'admDacceptreject.html', {'i': d_p})


def recacceptreject(request, username):
    def rec_delete_user_data(username):
        try:
            user_detail = Rdetail.objects.filter(username=username).first()

            if user_detail:
                user_detail.delete()

            user_signup = Signupp.objects.filter(username=username).first()

            if user_signup:
                user_signup.delete()

            user_detail2 = Rdetail2.objects.filter(username=username).first()

            if user_detail2:
                user_detail2.delete()

            
            return True

        except Exception as e:
            # Handle any exceptions that may occur
            print(e)
            return False

    d_p = Rdetail.objects.filter(username=username).first()
    if request.method == "POST":
        status = request.POST.get("password")
        if status == "reject":
            if rec_delete_user_data(username):
                messages.success(request, "User data deleted successfully.")
            else:
                messages.error(request, "Error deleting user data.")
            signup = Signupp.objects.filter(username=username).first()
            if signup:
                signup.delete()
            else:
                messages.error(request, "Signup not found.")
            return redirect("/admdonar")
        elif status == "accept":
            # Handle the accept case here
            pass  # replace this with your code
    return render(request, 'admRacceptreject.html', {'i': d_p})


def orgacceptreject(request, username):
    def org_delete_user_data(username):
        try:
            user_detail = Odetail.objects.filter(username=username).first()

            if user_detail:
                user_detail.delete()

            user_signup = Signupp.objects.filter(username=username).first()

            if user_signup:
                user_signup.delete()

            user_detail2 = Odetail2.objects.filter(username=username).first()

            if user_detail2:
                user_detail2.delete()

            
            return True

        except Exception as e:
            # Handle any exceptions that may occur
            print(e)
            return False

    d_p = Odetail.objects.filter(username=username).first()
    if request.method == "POST":
        status = request.POST.get("password")
        if status == "reject":
            if org_delete_user_data(username):
                messages.success(request, "User data deleted successfully.")
            else:
                messages.error(request, "Error deleting user data.")
            signup = Signupp.objects.filter(username=username).first()
            if signup:
                signup.delete()
            else:
                messages.error(request, "Signup not found.")
            return redirect("/admdonar")
        elif status == "accept":
            # Handle the accept case here
            pass  # replace this with your code
    return render(request, 'admOacceptreject.html', {'i': d_p})


def donsearch(request, username):
    d_p = Detail.objects.filter(username=username).first()
    d2_p=Detail2.objects.filter(username=username).first()
    return render(request, 'profile.html', {'i': d_p,'j':d2_p})


def admdonreq(request):

    up = Detail.objects.all()
    up1 = Detail2.objects.all()
    return render(request, 'admdonreq.html', {'up': up, 'up1': up1})



def admrecreq(request):
 
 rd=Rdetail.objects.all()
 rd1=Rdetail2.objects.all()

 return render(request,'admrecreq.html',{'rd':rd,'rd1':rd1})

def qrec(request):
    # username=val()
    rd=Rdetail.objects.all()
    return render(request,'qrec.html',{'rd':rd})

def qorg(request):
    # username=val()
    up=Odetail.objects.all()
    return render(request,'qorg.html',{'up':up})

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
    up=Odetail.objects.all()
    return render(request,'admorgreq.html',{'up':up})

def admhosreq(request):
    # username=val()
    hos=Hdetail.objects.all()
    return render(request,'admhosreq.html',{'hos':hos})

