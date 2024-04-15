class Django:

    ALLOWED_HOSTS = ['*']

    DEBUG = False 
    DEBUG = True #Comment if testing in Cloud


    DEPLOY = True
    DEPLOY = False #Comment if running in cloud for prod

    DEBUG_DB = 'postgres'
