def index(request):
    return render(request, 'lobsternachos/orders/index.html')

def show(request):
    return render(request, 'lobsternachos/orders/show.html')

def edit(request):
    return render(request, 'lobsternachos/orders/edit.html')

def destroy(request):
    return render(request, 'lobsternachos/orders/destroy.html')
