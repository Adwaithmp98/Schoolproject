from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

from .forms import FormEntryForm
from .models import Department, Course, FormEntry
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import JsonResponse
from .models import Department, Course

from django.shortcuts import render, redirect


def demo(request):
    return render(request, "index.html")
def Home(request):
    return render(request, "index.html")



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'hello.html')
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)

            user.save();
            print("user created")
            return render(request, 'login.html')
        else:
            messages.info(request, "passworf wrong")
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')


def index(request):
    departments = Department.objects.all()
    return render(request, 'mcq.html', {'departments': departments})




def get_courses(request, department_id):
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)

def index(request):
    departments = Department.objects.all()
    return render(request, 'template.html', {'departments': departments})


def save_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        purpose = request.POST['purpose']
        materials = request.POST.getlist('materials')

        entry = FormEntry(name=name, dob=dob, age=age, gender=gender, phone=phone,
                          email=email, address=address, department=department,
                          purpose=purpose, materials=materials)
        entry.save()

        return redirect('home')
    if request.method == 'POST':
        form = FormEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the appropriate URL name for your home page
    else:
        form = FormEntryForm()

    return render(request, 'template.html', {'form': form})