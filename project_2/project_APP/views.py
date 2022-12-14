from django.shortcuts import render
from .forms import employeeForm
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,AuthenticationForm,PasswordChangeForm



def signinView(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        # form = PasswordResetForm(request.POST)
        # form = AuthenticationForm(request.POST)
        form = PasswordChangeForm(request.POST)
        print("form==================",form)
        if form.is_valid():
            form.save()

    else:
        form = PasswordChangeForm()
    return render(request, 'employee.html',{'form':form})

# def employee_view(request):
#     if request.method == "POST":
#         form = employeeForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             favourite_color = form.cleaned_data['favourite_color']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             employee_data = form.cleaned_data['employee_data']
#             headline = form.cleaned_data['headline']
#             day = form.cleaned_data['day']
#             return render(request,"employee.html",{'form':form})
#     else:
#         form = employeeForm()
#     return render(request, 'employee.html',{'form':form})
