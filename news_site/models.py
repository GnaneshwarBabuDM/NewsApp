from django.db import models

# Create your models here.
class UserAuthenticationDetails(models.Model):
    # user_id = models.AutoField('User ID', db_column='USER_ID', primary_key=True)
    user_name = models.CharField('User Name', db_column='USER_NAME', max_length=35)
    password = models.CharField('Password', db_column='PASSWORD', max_length=35)
    created_on = models.DateTimeField('Created On', db_column='CREATED_DATE')
	
    # This is to used to give name to the database 
    class Meta:
        #managed = True
        db_table = 'REF_USER_AUTHENTICATION_DETAILS'

		
class UserSearchData(models.Model):
    user = models.ForeignKey(UserAuthenticationDetails, on_delete=models.CASCADE)
    search_data = models.CharField('Search Data', db_column='SEARCH_DATA', max_length=35)

    class Meta:
        #managed = True
        db_table = 'REF_USER_SEARCH_DATA'