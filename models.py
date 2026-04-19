from django.shortcuts import get_object_or_404, render
from .models import Question, Choice, Submission

def submit_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        # Step 1: Get the choice the user selected from the POST data
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form if no choice was selected
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Step 2: Create the Submission record (The "First Process")
        Submission.objects.create(
            user_name=request.user.username, # Or a name from a form
            selected_choice=selected_choice
        )
        
        # Step 3: Increment the vote count (Optional)
        selected_choice.votes += 1
        selected_choice.save()
        
        return render(request, 'polls/results.html', {'question': question})
