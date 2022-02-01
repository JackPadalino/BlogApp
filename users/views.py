from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.views.generic import ListView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome! Your account has been created and you are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your profile has been updated!')
            return redirect('profile')
    else:       
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)     
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)

class UserDeleteView(SuccessMessageMixin,LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('register')
    success_message = "Your profile was successfully deleted."

    # this test_func function checks to make that the current logged in user has the same ID as the profile we are trying to delete
    def test_func(self):
        user = self.get_object()
        if self.request.user.id == user.id:
            return True
        else:
            return False
