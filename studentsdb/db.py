import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    #'default': {
       # 'ENGINE': 'django.db.backends.postgresql',
	#'NAME': 'students_db',
	#'USER': 'students_db_user',
	#'PASSWORD': '300629qweR',
	#'HOST': 'localhost',
	#'PORT': '',
     
'default': {
	'ENGINE': 'django.db.backends.mysql',
	'HOST': 'localhost',
	'USER': 'students_db_user',
	'PASSWORD': '300629qweR',
	'NAME': 'students_db',   


	#'HOST': 'localhost',
       # 'USER': 'students_db_user',
        #'PASSWORD': '300629qweR',
        #'NAME': 'students_db',
    }
}
