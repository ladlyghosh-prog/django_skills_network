from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice, Submission

def submit(request, course_id):
    # Logic to process the submitted exam
    course = get_object_or_404(Course, pk=course_id)
    try:
        # Assuming multiple questions are submitted
        for question in course.question_set.all():
            selected_choice_id = request.POST[f'choice_{question.id}']
            selected_choice = question.choice_set.get(pk=selected_choice_id)
            # Create a submission record
            Submission.objects.create(
                user=request.user,
                choice=selected_choice
            )
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'onlinecourse/course_detail.html', {
            'course': course,
            'error_message': "You didn't select all answers.",
        })
    
    # After saving, redirect to the results page
    return HttpResponseRedirect(reverse('onlinecourse:show_exam_result', args=(course.id,)))

def show_exam_result(request, course_id):
    # Logic to calculate and show the results
    course = get_object_or_404(Course, pk=course_id)
    # Get all submissions for the current user and course
    submissions = Submission.objects.filter(user=request.user, choice__question__course=course)
    
    total_score = 0
    for submission in submissions:
        if submission.choice.is_correct:
            total_score += 1

    return render(request, 'onlinecourse/exam_result.html', {
        'course': course,
        'score': total_score,
        'submissions': submissions
    })
