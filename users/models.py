# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'Country'
        verbose_name_plural='Countries'

    def __str__(self):
        return self.cname

class Discover(models.Model):
    cname = models.OneToOneField(Country, models.DO_NOTHING, db_column='cname', primary_key=True)
    disease_code = models.ForeignKey('Disease', models.DO_NOTHING, db_column='disease_code')
    first_enc_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'Discover'
        unique_together = (('cname', 'disease_code'),)
        verbose_name_plural='Discoveries'

  

class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    id = models.ForeignKey('Diseasetype', models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'Disease'

    def __str__(self):
        return str(self.pk)
  


class Diseasetype(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140)

    class Meta:
        
        db_table = 'DiseaseType'

    def __str__(self):
        return str(self.pk)
  

class Doctor(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    degree = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Doctor'
    
    def __str__(self):
        return str(self.pk)
   

class PublicServant(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    department = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Public servant'
    
    def __str__(self):
        return str(self.pk)


class Record(models.Model):
    email = models.OneToOneField(PublicServant, models.DO_NOTHING, db_column='email', primary_key=True)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code')
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Record'
        unique_together = (('email', 'cname', 'disease_code'),)


class Specialize(models.Model):
    id = models.OneToOneField(Diseasetype, models.DO_NOTHING, db_column='id', primary_key=True)
    email = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'Specialize'
        unique_together = (('id', 'email'),)
        verbose_name_plural='Specializations'

class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')

    class Meta:
        managed = False
        db_table = 'Users'
        verbose_name_plural='Users'
    
    def __str__(self):
        return str(self.pk)
