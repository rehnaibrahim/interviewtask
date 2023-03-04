from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# from .models import Department
# from django.http import JsonResponse
# from .models import Course
# from django.views.generic import ListView, CreateView, UpdateView
# from django.urls import reverse_lazy
# from .models import Person

# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user =auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"button.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def form(request):
    return render(request, "form.html")






# def course_selection(request):
#     departments = Department.objects.all()
#     return render(request, 'course_selection.html', {'departments': departments})
#
#
# def courses_by_department(request):
#     department_id = request.GET.get('department_id')
#     courses = Course.objects.filter(department_id=department_id)
#     data = [{'id': course.id, 'name': course.name} for course in courses]
#     return JsonResponse(data, safe=False)
#
#
#
#
# class PersonListView(ListView):
#     model = Person
#     context_object_name = 'people'
#
# class PersonCreateView(CreateView):
#     model = Person
#     fields = ('name', 'birthdate', 'country', 'city')
#     success_url = reverse_lazy('person_changelist')
#
# class PersonUpdateView(UpdateView):
#     model = Person
#     fields = ('name', 'birthdate', 'country', 'city')
#     success_url = reverse_lazy('person_changelist')
#
# def new(request):
#     return render(request, "new.html")




# from .models import Department, Course
#
# def course(request):
#     departments = Department.objects.all()
#     department_id = request.GET.get('department_id')
#     #print(department_id)
#     courses = Course.objects.filter(department_id=department_id)
#     #print(courses)
#     courses = Course.objects.all()
#     #print(courses)
#     context = {'departments': departments, 'courses': courses}
#    # data = [{'id': course.id, 'name': course.name} for course in courses]
#     return render(request, 'course.html', context)

from django.shortcuts import render
from django.http import JsonResponse
from .models import Department, Course

def department_courses(request):
    departments = Department.objects.all()
    return render(request, 'department_courses.html', {'departments': departments})

def load_courses(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id).order_by('name')
    return JsonResponse(list(courses.values('id', 'name')), safe=False)