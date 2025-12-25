from django.db import models

# Create your models here.


class userdetails(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30)
    emailid = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    phonenumber = models.CharField(max_length=30, null=False)

    def __str__(self):
        return "%s %s %s %s %s %s" % (
            self.id, self.first_name, self.last_name, self.emailid, self.password, self.phonenumber)

class cretecampaign(models.Model):
    id=models.AutoField(primary_key=True)
    campname=models.CharField(max_length=50,null=False)
    eventname=models.CharField(max_length=50,null=False)
    goalfund=models.CharField(max_length=10,null=False)
    locn=models.CharField(max_length=50,null=False)
    start_date=models.CharField(max_length=100,null=False)
    end_date=models.CharField(max_length=100,null=False)
    camp_status=models.CharField(max_length=50,null=False)
    camp_totalamt=models.CharField(max_length=50,null=False)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" %(self.id,self.campname,self.eventname,self.goalfund,self.locn,self.start_date, self.end_date, self.camp_status, self.camp_totalamt)


class userdonation(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=30)
    cid = models.CharField(max_length=30, null=False)
    cname = models.CharField(max_length=30, null=False)
    hash_code = models.CharField(max_length=30, null=False)
    amt_donate = models.CharField(max_length=30, null=False)
    donated_on= models.CharField(max_length=30, null=False)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (
            self.id, self.uid, self.first_name, self.cid, self.cname, self.hash_code, self.amt_donate, self.donated_on)
