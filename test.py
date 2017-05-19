import os
if __name__ == '__main__':
    print "++++++++++++++++++++++++++++++++"
    # print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    print STATICFILES_DIRS
