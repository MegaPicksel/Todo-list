from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm
from .models import ToDoList
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ToDoListSerializer


def login_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')
    else:
        form = LoginForm()
        return render(request, 'todo/login.html', {'form': form})


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_redirect')
        else:
            form = RegistrationForm()

    return render(request, 'todo/register.html', {'form': form})


def registration_redirect(request):
    return render(request, 'todo/check_email.html')


def home(request):
    return render(request, 'todo/home.html')


def logout(request):
    return redirect('login')


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


class ToDoDetail(APIView):
    def get(self, request, pk):
        task = get_object_or_404(ToDoList, pk=pk)
        serializer = ToDoListSerializer(task)
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = get_object_or_404(ToDoList, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









