

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def view_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')
    unread_count = notifications.filter(is_read=False).count()
    return render(request, 'notifications.html', {'notifications': notifications, 'unread_count': unread_count})

def clubs(request):
    return render(request,'clubs.html')

def form(request):
    return render(request,'form.html')

def study(request):
    return render(request,'study.html')

def First(request):
    return render(request,'First.html')

def jobs(request):
    return render(request,'jobs.html')

def Events(request):
    return render(request,'event_registration_page.html')



from django.shortcuts import render, redirect
from .models import Message
from .forms import ChatMessageForm
from django.contrib.auth.decorators import login_required

@login_required  # Ensure only logged-in users can access the chat
def chat_box(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.user = request.user  # Associate the message with the logged-in user
            chat_message.save()
            return redirect('chat_box')  # Redirect to the same page after saving
    else:
        form = MessageForm()

    # Fetch all chat messages
    chat_messages = Message.objects.all().order_by('timestamp')

    # Pass the form and messages to the template
    context = {
        'form': form,
        'chat_messages': chat_messages,
    }

    return render(request, 'chat_box.html', context)


@login_required
def chat_box(request):
    if request.method == 'POST':
        message_text = request.POST.get('message')
        Message.objects.create(user=request.user, message=message_text)
    
    # Fetch all top-level messages (messages without a parent)
    chat_messages = Message.objects.filter(parent__isnull=True)
    return render(request, 'chat_box.html', {'chat_messages': chat_messages})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def reply_to_message(request, message_id):
    if request.method == 'POST':
        # Get the parent message or return a 404 error if it doesn't exist
        parent_message = get_object_or_404(Message, id=message_id)
        reply_text = request.POST.get('reply')

        # Create the reply
        Message.objects.create(
            user=request.user,
            message=reply_text,
            parent=parent_message
        )
    
    return redirect('chat_box')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def auth_view(request):
    # Initialize forms
    signup_form = UserCreationForm()
    login_form = AuthenticationForm()

    # Handle Signup Form Submission
    if request.method == 'POST' and 'signup' in request.POST:
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            print(f"User created: {user.username}")

            # Write signup data to a text 

            messages.success(request, "Signup successful! Please log in.")
            return redirect('auth')
        else:
            print(signup_form.errors)
            messages.error(request, 'Sign up failed.')

    # Handle Login Form Submission
    elif request.method == 'POST' and 'login' in request.POST:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            print(f"Username: {username}, Password: {password}")
            user = authenticate(username=username, password=password)
            print(f"User: {user}")
            if user is not None:
                login(request, user)
                print(f"User logged in: {request.user.is_authenticated}")
                print("Redirecting to dashboard...")
                return redirect('notifications')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            print(login_form.errors)

    # Render the page for GET requests or invalid form submissions
    return render(request, 'auth.html', {
        'signup_form': signup_form,
        'login_form': login_form,
    })

@login_required
def dashboard(request):
    '''if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the same page after saving
    else:
        form = PersonForm()

    # Fetch all persons to display in the list
    persons = Person.objects.all()'''
    context = {
        #'form': form,
        #'persons': persons,
        'user': request.user,  # Ensure this is properly formatted
    }

    return render(request, 'notifications.html', context)




'''from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def send_email_to_user(request):
    if request.method == 'POST':
        # Get the email from the custom form
        user_email = request.POST.get('email')  # 'email' is the name of the input field
        
        # Validate the email (optional)
        if user_email:
            # Define email content
            subject = 'Thank You for Registering'
            message = 'Hello,\n\nThank you for reaching out! We will get back to you soon.\n\nBest regards,\nFull Stack Fighters'
            from_email = 'pallavibandikari@gmail.com'  # Sender's email
            recipient_list = ['rr200191@rguktrkv.ac.in','bandikari115@gamil.com','kprathap088@gmail.com']  # User's email
            
            # Send the email
            send_mail(
                subject=subject,
                message=message,
                from_email=from_email,
                recipient_list=recipient_list,
                fail_silently=False,
            )
            
            # Return a success message
            return HttpResponse('Email sent successfully!')
        else:
            return HttpResponse('Invalid email address.')
    
    # Render the custom form template for GET requests
    return render(request, 'form.html')'''



