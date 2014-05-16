def index(request):
    return render(request, 'lobsternachos/devices/index.html')

def show(request):
    return render(request, 'lobsternachos/devices/show.html')

def new(request):
    return render(request, 'lobsternachos/devices/new.html')

def edit(request):
    return render(request, 'lobsternachos/devices/edit.html')

def destroy(request):
    return render(request, 'lobsternachos/devices/destroy.html')
