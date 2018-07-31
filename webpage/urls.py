"""webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

import socket
import uuid
import urllib.request
import requests
from simap.models import Log, ARP_command, ARP_result
import threading
import time
from simap.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simap/', include('simap.urls')),

    path('system/ram', ram, name='ram'),
    path('system/cpu', cpu, name='cpu'),
    path('life', life, name='life'),
    path('Log_five', Log_five, name='Log_five'),
    path('log/table', table_delete, name='table_delete'),
    path('system/mac-hostname', mac_host, name='mac-hostname'),
    path('wan_IP/IP_address', ip_address, name='ip_address'),
    path('system/ip-netmask-gateway', ip_netmask_gateway, name='ip-netmask-gateway'),
    path('ip_address', ip_address, name='ip_address'),
    path('thread1', thread1, name='thread1'),
]

hostname = socket.gethostname()
mac_addresses = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1]))
wan = urllib.request.urlopen('https://ident.me').read().decode('utf8')
port = 8000
data = {'hostname': hostname, 'mac_addresses': mac_addresses, 'wan_ip': wan, 'port': port}
res = requests.post('http://203.252.34.237:8080/simMe', data=data)

class DBcheck(threading.Thread):
    def run(self):
        b = None
        while 1:
            key = ARP_command.objects.first()
            if key is None:
                continue
            elif b == key.id:
                pass
            else:
                if key.function_num == 1:
                    q = ARP_result(inst="Yes Hello", key=key.id)
                    q.save()
                    q.id
                key.delete()

            b = key.id
            time.sleep(1)
send = DBcheck(name='dbchecking')
send.start()