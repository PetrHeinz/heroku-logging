from django.shortcuts import redirect, render
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def user_register(request):
    if request.method == "GET":
        return render(request, "user/register.html")
    elif request.method == "POST":
        User.objects.create_user(
            request.POST["username"], request.POST["email"], request.POST["password"]
        )
        return redirect("home")


def user_login(request):
    if request.method == "GET":
        return render(request, "user/login.html")
    elif request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "user/auth_fail.html")


def user_logout(request):
    logout(request)
    return redirect("home")


def note_list(request):
    notes = Note.objects.all()
    return render(request, "note/list.html", {"notes": notes})


def note_show(request, id):
    note = Note.objects.get(pk=id)
    return render(request, "note/show.html", {"note": note})


@login_required
def note_create(request):
    if request.method == "GET":
        return render(request, "note/create.html")
    elif request.method == "POST":
        note = Note(title=request.POST["title"], content=request.POST["content"])
        note.save()
        return redirect("home")


@login_required
def note_update(request, id):
    if request.method == "GET":
        note = Note.objects.get(pk=id)
        return render(request, "note/update.html", {"note": note})
    elif request.method == "POST":
        note = Note.objects.update_or_create(
            pk=id,
            defaults={
                "title": request.POST["title"],
                "content": request.POST["content"],
            },
        )
        return redirect("home")


@login_required
def note_delete(request, id):
    note = Note.objects.get(pk=id)
    note.delete()
    return redirect("home")
