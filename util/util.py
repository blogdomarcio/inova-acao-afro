from datetime import datetime, date


def generate_nome(self, filename):
    data = datetime.now()
    url = "%s+'_'+%s" % (data, filename)
    return url