from django.shortcuts import render, get_object_or_404, redirect
from .models import Match
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# 1. Read - Display all matches
@login_required
def match_list(request):
    matches = Match.objects.all()  # Retrieve all matches
    return render(request, 'matches/match_list.html', {'matches': matches})

# 2. Create - Add a new match
@login_required
def add_match(request):
    if request.method == 'POST':
        team1 = request.POST['team1']
        team2 = request.POST['team2']
        venue = request.POST['venue']
        match_time = request.POST['match_time']
        watch = request.POST['watch']
        Match.objects.create(team1=team1, team2=team2, venue=venue, match_time=match_time, watch=watch)
        return redirect('match_list')
    return render(request, 'matches/add_match.html')

# 3. Update - Edit an existing match
@login_required
def edit_match(request, id):
    match = get_object_or_404(Match, id=id)
    if request.method == 'POST':
        match.team1 = request.POST['team1']
        match.team2 = request.POST['team2']
        match.venue = request.POST['venue']
        match.match_time = request.POST['match_time']
        match.watch = request.POST['watch']
        match.save()  # Save the updated match
        return redirect('match_list')
    return render(request, 'matches/edit_match.html', {'match': match})

# 4. Delete - Remove a match
@login_required
def delete_match(request, id):
    match = get_object_or_404(Match, id=id)
    if request.method == 'POST':
        match.delete()  # Delete the match
        return redirect('match_list')
    return render(request, 'matches/delete_match.html', {'match': match})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('match_list')  # Redirect to a main page after signup
    else:
        form = SignUpForm()
    return render(request, 'matches/sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username exists
        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            # Authenticate if user exists
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('match_list')  # Redirect to the main page after login
            else:
                # Incorrect password
                messages.error(request, "Wrong password. Please try again.")
        else:
            # User doesn't exist
            messages.error(request, "User does not exist. Please sign up first.")

    else:
        form = AuthenticationForm()

    return render(request, 'matches/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
