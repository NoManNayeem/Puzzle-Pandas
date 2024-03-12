from django.contrib import admin
from campaign.models.campaign import Campaign
from campaign.models.quiz import  Question, Choice

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_active', 'winner', 'runner_up', 'third_place')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'
    fields = ('title', 'description', 'start_date', 'end_date', 'is_active', 'prize_description', 'winner', 'runner_up', 'third_place')


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
    fields = ('text', 'is_correct')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'type', 'campaign')
    list_filter = ('type', 'campaign')
    search_fields = ('text',)
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('question', 'is_correct')
    search_fields = ('text', 'question__text')
