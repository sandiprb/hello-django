from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 2

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		(None, {'fields': ['pub_date']}),
	]
	inlines = [ChoiceInline]
		

# Register your models here.
admin.site.register(Question, QuestionAdmin)
