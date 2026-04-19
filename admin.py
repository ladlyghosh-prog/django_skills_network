from django.contrib import admin
# These are the 7 imported classes (3 models + 4 admin/inline types)
from .models import Question, Choice, Submission, Lesson 

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Register the implementations
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Submission)
