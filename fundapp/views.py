from datetime import datetime, date

from django.shortcuts import render, HttpResponse, redirect
from .models import userdetails, userdonation, cretecampaign
# Create your views here.
from django.contrib import messages
import hashlib
from time import time
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np


def index(request):
    return render(request, "fundapp/index.html", {})


def Login(request):
    if request.method == "POST":
        username = request.POST["Uname"]
        pwd = request.POST["Pass"]

        if username == 'admin' and pwd == 'admin':
            messages.success(request, "lOGIN Successfully")
            return redirect('homepage')

        else:
            try:
                user = userdetails.objects.get(emailid=username, password=pwd)
                request.session['userid'] = user.id
                request.session['uname'] = user.first_name
                messages.success(request, "lOGIN Successfully")
                return redirect('userhomepage')

            except:
                pass
            # return render(request, "fundapp/userhomepage.html", {})
    return render(request, "fundapp/Login.html", {})


def homepage(request):
    camp = cretecampaign.objects.all()
    print(camp)

    for x in camp:
        cstatus = x.camp_status
        if cstatus == "Active":
            edate = x.end_date
            date_object = datetime.strptime(edate, '%Y-%m-%d').date()
            print(date_object)
            CurrentDate = today = date.today()
            print(CurrentDate)
            if CurrentDate > date_object:
                x.camp_status = "Inactive"
                x.save()

    return render(request, "fundapp/homepage.html", {})


def createcamp(request):
    if request.method == "POST":

        campname = request.POST["cname"]
        ename = request.POST['ename']
        goalfund = request.POST['fgoal']
        locn = request.POST['locn']
        start_date = request.POST['stdate']
        end_date = request.POST['enddate']
        camp_status = "Active"
        camp_totalamt = "0.0"
        newcamp = cretecampaign(campname=campname, eventname=ename, goalfund=goalfund, locn=locn, start_date=start_date,
                                end_date=end_date, camp_status=camp_status, camp_totalamt=camp_totalamt)
        newcamp.save()
        return render(request, "fundapp/homepage.html", {})
    return render(request, "fundapp/createcamp.html", {})


def activecamp(request):
    camp = cretecampaign.objects.all()
    context = {
        'camp': camp

    }
    return render(request, "fundapp/activecamp.html", context)


def viewuser(request):
    viewuser = userdonation.objects.all()
    context = {
        'viewuser': viewuser

    }
    return render(request, "fundapp/viewuser.html", context)


def report(request):
    camp1 = cretecampaign.objects.all()
    xlabel=[]
    ylabel=[]
    for x in camp1:
        cstatus1 = x.campname
        xlabel.append(cstatus1)
    print(xlabel)
    for x in camp1:
        ctotal = x.camp_totalamt
        ylabel.append(ctotal)
    print(ylabel)
    xpoints = xlabel
    ypoints = ylabel


    plt.bar(xpoints, ypoints)
    plt.savefig('D:/finalproject/crowdfund/fundapp/static/images/report.png')
    plt.show()
    return render(request, "fundapp/report.html", {})


def userviewcamp(request):
    camp1 = cretecampaign.objects.all()
    print(camp1)
    context = {

        'camp1': camp1
    }
    return render(request, "fundapp/userviewcamp.html", context)


def userhomepage(request):
    return render(request, "fundapp/userhomepage.html", {})


class blockchain():
    def __init__(self):
        self.blocks = []
        self.__secret = ''
        self.__difficulty = 4
        # guessing the nonce
        i = 0
        secret_string = '/*SECRET*/'
        while True:
            _hash = hashlib.sha256(str(secret_string + str(i)).encode('utf-8')).hexdigest()
            if (_hash[:self.__difficulty] == '0' * self.__difficulty):
                self.__secret = _hash
                break
            i += 1

    def create_block(self, sender: str, information: str):
        block = {
            'index': len(self.blocks),
            'sender': sender,
            'timestamp': time(),
            'info': information
        }
        if (block['index'] == 0):
            block['previous_hash'] = self.__secret  # for genesis block
        else:
            block['previous_hash'] = self.blocks[-1]['hash']
        # guessing the nonce
        i = 0
        while True:
            block['nonce'] = i
            _hash = hashlib.sha256(str(block).encode('utf-8')).hexdigest()
            if (_hash[:self.__difficulty] == '0' * self.__difficulty):
                block['hash'] = _hash
                break
            i += 1
        self.blocks.append(block)

    def validate_blockchain(self):
        valid = True
        n = len(self.blocks) - 1
        i = 0
        while (i < n):
            if (self.blocks[i]['hash'] != self.blocks[i + 1]['previous_hash']):
                valid = False
                break
            i += 1
        if valid:
            print('The blockchain is valid...')
        else:
            print('The blockchain is not valid...')

    def show_blockchain(self):
        for block in self.blocks:
            pprint(block)
            print()
            return block['hash']


def userdonate(request, id=0):
    uid = request.session['userid']
    uname = request.session['uname']
    if id:
        try:
            getuserdata = cretecampaign.objects.get(id=id)
            request.session['campid']=getuserdata.id
            context = {

                'getuserdata': getuserdata
            }
        except:
            pass
    if request.method == "POST":

        uid = uid
        first_name = request.POST['sender']
        cid =  request.POST['cid']
        cname = request.POST['cname']

        amt_donate = request.POST['amt']
        donated_on = request.POST['sentdate']
        b = blockchain()
        b.create_block(first_name, amt_donate)

        hash_code = b.show_blockchain()
        b.validate_blockchain()
        newdonate = userdonation(uid=uid, first_name=first_name, cid=cid, cname=cname, hash_code=hash_code,
                                 amt_donate=amt_donate, donated_on=donated_on)
        newdonate.save()

        updateamt=cretecampaign.objects.get(id=cid)
        print(cid)
        camt=updateamt.camp_totalamt
        ctotalamt = int(float(camt))  + int(float(amt_donate))
        updateamt.camp_totalamt = str(ctotalamt)
        updateamt.save()

        return render(request, "fundapp/userhomepage.html", {})
    return render(request, "fundapp/userdonate.html", context)


def viewuserdonation(request):
    uid = request.session['userid']
    print(uid)
    viewuser = userdonation.objects.all()
    print(viewuser)
    context = {

        'viewuser': viewuser
    }
    return render(request, "fundapp/viewuserdonation.html", context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['Last_name']
        emailid = request.POST['emailid']
        password = request.POST['pwd']
        phonenumber = request.POST['phoneno']
        newuser = userdetails(first_name=first_name, last_name=last_name, emailid=emailid, password=password,
                              phonenumber=phonenumber)
        newuser.save()
        # return HttpResponse("User Registered Successfully")
        return render(request, "fundapp/index.html", {})
    return render(request, "fundapp/register.html", {})
