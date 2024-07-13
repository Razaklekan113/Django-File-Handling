from django.shortcuts import render, get_object_or_404, redirect
from .forms import FileForm
from .models import File

# Create your views here.
def upload_form(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {"form": form}
            return render(request, 'file/index.html', context)
    context = {"form": FileForm()}
    return render(request, 'file/index.html', context)

def list_files(request):
    files = File.objects.all()
    context = {"files": files}
    return render(request, 'file/list.html', context) 

def delete_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.delete()
    return redirect('list_files') 