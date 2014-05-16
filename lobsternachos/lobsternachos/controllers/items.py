def index(request):
    return render(request, 'lobsternachos/items/index.html')

def show(request):
    return render(request, 'lobsternachos/items/show.html')

def new(request):
    return render(request, 'lobsternachos/items/new.html')

def edit(request):
    return render(request, 'lobsternachos/items/edit.html')

def destroy(request):
    return render(request, 'lobsternachos/items/destroy.html')
