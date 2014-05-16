def index(request):
    return render(request, 'lobsternachos/categories/index.html')

def show(request):
    return render(request, 'lobsternachos/categories/show.html')

def new(request):
    return render(request, 'lobsternachos/categories/new.html')

def edit(request):
    return render(request, 'lobsternachos/categories/edit.html')

def destroy(request):
    return render(request, 'lobsternachos/categories/destroy.html')
