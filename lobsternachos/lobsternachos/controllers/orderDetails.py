def index(request):
    return render(request, 'lobsternachos/orderDetails/index.html')

def show(request):
    return render(request, 'lobsternachos/orderDetails/show.html')

def edit(request):
    return render(request, 'lobsternachos/orderDetails/edit.html')

def destroy(request):
    return render(request, 'lobsternachos/orderDetails/destroy.html')
