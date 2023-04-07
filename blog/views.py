from django.shortcuts import render
from django.views import generic
from .models import Post, PolicyPost
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def Policy(request):
    template_name = 'policy.html'
    return  render(request,template_name, {})
def Contact(request):
    submitted = False
    template_name = 'success.html'
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = ContactForm(name=name,email=email,message=message,
                       subject = subject
                       )
        data.save()
        submitted = True
        return render(request,template_name,{})
    else:
        template_name = 'contact.html'
        
        return render(request,template_name,{})