import datetime

def get_unique_tag()->str:
    return datetime.datetime.now().strftime("%b_%d_%Y_%H_%M_%S")