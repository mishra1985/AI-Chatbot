from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import DocumentForm

def home(request):
    # Redirect to the upload page (or any other default page you prefer)
    return redirect('upload_document')

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_document')
    else:
        form = DocumentForm()
    return render(request, 'chatbot/upload.html', {'form': form})

def chat_interface(request):
    return render(request, 'chatbot/chat.html')

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from transformers import pipeline


# Switch to GPT-Neo 2.7B for text generation
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

def ask_question(user_query):
    prompt = f"Question: {user_query}\nAnswer:"
    generated = generator(prompt, max_length=150, do_sample=True)
    answer = generated[0]['generated_text']
    return answer

# Example usage
query = "What color is a ripe mango?"
print(ask_question(query))
