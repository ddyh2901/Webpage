from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import psutil
import uuid
import socket
from simap.models import Log
from django.utils import timezone

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
    log_lists = Log.objects.order_by('time')
    context = {'log_lists': log_lists}
    return render(request, 'simap/log.html', context)

def usage(request):
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent(interval=1)
    if(ram>75):
        q = Log(time=timezone.now(), cpu=cpu, ram=ram)
        q.save()
        q.id
    if (cpu > 75):
        q = Log(time=timezone.now(), cpu=cpu, ram=ram)
        q.save()
        q.id
    context = {'cpu': cpu, 'ram': ram}
    return JsonResponse(context)

def mac_host(request):
    mac_addresses = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
               for ele in range(0, 8 * 6, 8)][::-1]))
    hostname = socket.gethostname()
    group1 = {'mac_addresses': mac_addresses, 'hostname': hostname}
    return JsonResponse(group1)

def ip_address(request):
    group1=[]
    return JsonResponse(group1)