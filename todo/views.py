from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from .models import ToDoList
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ToDoListSerializer
from .tasks import mail


# login Form
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})


# Registration form
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            form.save()
            """
            Calls the celery task
            Passes registration_email task variable in to function call
            in order to pass users email to Celery function.
            
            """
            registration_email = request.POST.get('email')
            mail.delay(registration_email)
            return redirect('registration_redirect')
        else:
            form = RegistrationForm()

    return render(request, 'todo/register.html', {'form': form})


# Registration redirect
def registration_redirect(request):
    return render(request, 'todo/check_email.html')


# Home page
def home(request):
    return render(request, 'todo/home.html')


# Logout
def logout(request):
    form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})


# Add items to "todo-list"
# Going through a rest API to interact with the PostgreSQL database
class ToDoView(APIView):
    def get(self, request):
        tasks = ToDoList.objects.all()
        serializer = ToDoListSerializer(tasks, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View the details of the task, allows user to delete a task once done.
class ToDoDetail(APIView):
    def get(self, request, pk):
        task = get_object_or_404(ToDoList, pk=pk)
        serializer = ToDoListSerializer(task)
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = get_object_or_404(ToDoList, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)