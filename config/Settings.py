import os
class Settings:
    secretKey="a12nc)238OmPq#cxOlm*a"

    #Dev
    # host='localhost'
    # database='furniture'
    # user='root'
    # password='root'

    #Production
    host=os.environ['HOST']
    database=os.environ['DATABASE']
    user=os.environ['USER']
    password=os.environ['PASSWORD']