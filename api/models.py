
from django.db import models
from django.core.validators import RegexValidator
#from .utils import generate_qr
ST_CHOICES=(
    (True, 'Active'),
    (False, 'Inactive')
)

class AssetType(models.Model):
    asset_type_id = models.AutoField(primary_key=True)
    asset_type_name = models.CharField(unique=True, max_length=50, blank=False, null=False)
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')

    class Meta:
        managed = True
        db_table = 'asset_type'

    def __str__(self):
        return self.asset_type_name


class Assets(models.Model):
    asset_id = models.AutoField(unique=True, primary_key =True)
    user_id = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    asset_type = models.ForeignKey('AssetType', models.DO_NOTHING, blank=False, null=False)
    asset_name = models.CharField(max_length=100, blank=False, null=False)
    asset_model = models.CharField(max_length=100, blank=True, null=True)
    asset_inst_date = models.DateField(blank=False, null=False)
    asset_remove_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=14, decimal_places=4, blank=False, null=False)
    warranty_period = models.DateField(blank=True, null=True)
    service_interval = models.IntegerField(blank=True, null=True)
    last_service = models.DateTimeField(blank=True, null=True)
    media_attachments = models.FileField(blank=False, null=False, default='')
    invoice_attachments = models.FileField(blank=False, null=False, default='')
    barcode = models.BigIntegerField(blank=True, null=True)
    distributor_id = models.ForeignKey('Distributor', models.DO_NOTHING, blank=True, null=True)
    supplier_id = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')

    class Meta:
        managed = True
        db_table = 'assets'

    # def save(self, *args, **kwargs):
    #     print("something")
    #     self.barcode = generate_qr()
    #     super(Assets,self).save(*args, **kwargs)

    def __str__(self):
         return self.asset_name

class Distributor(models.Model):
    distributor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(unique=True, max_length=50, blank=False, null=False)
    mobile =  models.CharField(unique=True, max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')])
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    attachments = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')

    class Meta:
        managed = True
        db_table = 'distributor'

    def __str__(self):
        return str(self.name)


class PaymentType(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    payment_type_name = models.CharField(max_length=100, blank=False, null=False)
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')

    class Meta:
        managed = True
        db_table = 'payment_type'

    def __str__(self):
        return self.payment_type_name


class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_type = models.ForeignKey('PaymentType', models.DO_NOTHING, blank=True, null=True)
    cost = models.FloatField(blank=False, null=False)
    billno = models.BigIntegerField(blank=False, null=False)
    invoiceid = models.BigIntegerField(blank=True, null=True)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING, blank=True, null=True)
    attachments = models.FileField(blank=False, null=False, default='')
    asset_id = models.ForeignKey('Assets', models.DO_NOTHING, blank=True, null=True)
    vendor_id = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')

    class Meta:
        managed = True
        db_table = 'payments'
    
    def __str__(self):
        return str(self.payment_type)

class Priorities(models.Model):
    priority_id = models.AutoField(primary_key=True)
    priority_name = models.CharField(max_length=100, blank=False, null=False)
    hours = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')

    class Meta:
        managed = True
        db_table = 'priorities'

    def __str__(self):
        return self.priority_name    


class Rolemapping(models.Model):
    rolemapping_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    role_id = models.ForeignKey('Roles', models.DO_NOTHING, blank=True, null=True)
    status = models.BooleanField(choices=ST_CHOICES,default=True)    
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')
    
    class Meta:
        managed = True
        db_table = 'rolemapping'


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=30, blank=False, null=False)
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')

    class Meta:
        managed = True
        db_table = 'roles'

    def __str__(self):
        return self.role_name


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=50, blank=False, null=False)
    mobile =  models.CharField(unique=True, max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')])
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    distributor_id = models.ForeignKey(Distributor, models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')

    class Meta:
        managed = True
        db_table = 'supplier'

    def __str__(self):
        return str(self.name)


class TicketStatus(models.Model):
    ticket_status_id = models.AutoField(primary_key=True)
    ticket_status_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')

    class Meta:
        managed = True
        db_table = 'ticket_status'

    def __str__(self):
        return self.ticket_status_name


class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Users', models.DO_NOTHING, blank=False, null=False)
    asset_id = models.ForeignKey('Assets', models.DO_NOTHING, blank=False, null=False)
    location = models.CharField(max_length=250, blank=True, null=True)
    priority = models.ForeignKey('Priorities', models.DO_NOTHING, blank=False, null=False)
    description = models.CharField(max_length=250, blank=True, null=True)
    ticket_status = models.ForeignKey(TicketStatus, models.DO_NOTHING, db_column='ticket_status', blank=True, null=True)
    attachments = models.FileField(blank=False, null=False, default='')
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')
   
    class Meta:
        managed = True
        db_table = 'tickets'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey('Roles', models.DO_NOTHING, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True, max_length=50, blank=False, null=False)
    mobile =  models.CharField(unique=True, max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')])
    password = models.CharField(max_length=30, blank=False, null=False)
    cnfpassword = models.CharField(max_length=30, blank=False, null=False)
    status = models.BooleanField(choices=ST_CHOICES,default=True)
    created_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    created_by = models.ForeignKey('self', models.DO_NOTHING, db_column='created_by', blank=True, null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey('self', models.DO_NOTHING, db_column='updated_by', blank=True, null=True, related_name='%(class)s_updated')

    class Meta:
        managed = True
        db_table = 'users'

    def __str__(self):
        return str(self.name)

