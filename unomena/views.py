from django.shortcuts import redirect


def register_redirect(request):
    return redirect('register')