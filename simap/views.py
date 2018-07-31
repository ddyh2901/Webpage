from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import psutil
import uuid
import socket
from simap.models import Log, ARP_command, ARP_result
from django.utils import timezone
import time
import threading
from django.core import serializers
import os
import urllib.request
from urllib.parse import urlparse
import netifaces
# Create your views here.

def index(request):
    return render(request, 'simap/index.html')

def info(request):
    return render(request, 'simap/info.html')

def info2(request):
    return render(request, 'simap/info2.html')

def wan_IP(request):
    return render(request, 'simap/wan_IP.html')

def wan_ping(request):
    return render(request, 'simap/wan_ping.html')

def wan_port(request):
    return render(request, 'simap/wan_port.html')

def lan_IP(request):
    return render(request, 'simap/lan_IP.html')

def lan_ping(request):
    return render(request, 'simap/lan_ping.html')

def lan_port(request):
    return render(request, 'simap/lan_port.html')

def wifi_24(request):
    return render(request, 'simap/wifi_24.html')

def wifi_5(request):
    return render(request, 'simap/wifi_5.html')

def nat_set(request):
    return render(request, 'simap/nat_set.html')

def nat_lookup(request):
    return render(request, 'simap/nat_lookup.html')

def log(request):
    Log.objects.filter(check=True).update(check=False)
    log_lists = Log.objects.order_by('-time')
    context = {'log_lists': log_lists}
    return render(request, 'simap/log.html', context)

def Log_five(request):
    log_lists = list(Log.objects.order_by('-id')[:5].values())
    return JsonResponse(log_lists,safe=False)

def table_delete(request):
    Log.objects.all().delete()

def cpu_ram(request):
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent(interval=1)
    if(ram>75):
        q = Log(time=timezone.now(), cpu=cpu, ram=ram, check=True)
        q.save()
        q.id
    if (cpu > 75):
        q = Log(time=timezone.now(), cpu=cpu, ram=ram, check=True)
        q.save()
        q.id
    context = {'cpu': cpu, 'ram': ram, 'time': timezone.now(), 'check': True}
    return JsonResponse(context)

def life(request):
    context = {'text': 1}
    return JsonResponse(context)

def cpu(request):
    cpu = psutil.cpu_percent(interval=1)
    #hostname = socket.gethostname()
    #mac_addresses = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    #                           for ele in range(0, 8 * 6, 8)][::-1]))
    #lan = socket.gethostbyname(socket.gethostname())
    #wan = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    #sock = request.build_absolute_uri('/')
    #o = urlparse(sock)
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.bind(('0.0.0.0', 0))
    context = {'cpu': cpu}
    return JsonResponse(context)

def ram(request):
    ram = psutil.virtual_memory().percent
    context = {'ram': ram}
    return JsonResponse(context)

def mac_host(request):
    mac_addresses = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
               for ele in range(0, 8 * 6, 8)][::-1]))
    hostname = socket.gethostname()
    group1 = {'mac_addresses': mac_addresses, 'hostname': hostname}
    return JsonResponse(group1)

def ip_netmask_gateway(request):
    #lan = socket.gethostbyname(socket.gethostname())
    ip_info = netifaces.ifaddresses('{12D26DFF-6CB4-46A6-BB6E-0C41A7961D43}')
    a = ip_info[netifaces.AF_INET][0]['addr']
    b = ip_info[netifaces.AF_INET][0]['netmask']
    c = netifaces.gateways()['default'][netifaces.AF_INET][0]
    context = {'lan': a, 'netmask': b, 'gateway': c}
    return JsonResponse(context)

def ip_address(request):
    ip_address = 0
    if request.method == 'POST':
        ip_address = request.POST.get('a', None)
    #os.system('ifconfig eth0 inet %s netmask 255.255.255.0' % ip_address)
    return 0


def thread1(request):

    a = ARP_command(function_num=1, jason="Hello")
    a.save()
    a.id

    for i in range(1, 11):
        time.sleep(1)
        b = ARP_result.objects.filter(key=a.id)
        if b:
            break

    data = ARP_result.objects.all()[0]
    data.inst
    result = {'hello':  data.inst}
    return JsonResponse(result)
