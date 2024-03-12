
from .models.campaign import Campaign
from .models.quiz import Question


from django.shortcuts import render

def no_active_campaign(request):
    return render(request, 'no_active_campaign.html')




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.db.models import Q
from django.http import JsonResponse
from django.utils.safestring import mark_safe
import json


def no_active_campaign(request):
    """View to display when no active campaign is available."""
    return render(request, 'no_active_campaign.html')

@login_required
def start_quiz(request):
    """View to start the quiz for an active campaign."""
    current_time = now()
    try:
        # Get the active campaign that is currently running
        campaign = Campaign.objects.filter(
            Q(is_active=True) & 
            Q(start_date__lte=current_time) & 
            Q(end_date__gte=current_time)
        ).get()
    except Campaign.DoesNotExist:
        # Redirect to a view indicating no active campaign
        return redirect('no_active_campaign')
    
    # Check if there are questions associated with the active campaign
    if not campaign.questions.exists():
        # Redirect to a view indicating no questions available for the campaign
        return redirect('no_questions_available')

    # Serialize questions and choices for the frontend
    questions_json = serialize_questions(campaign.questions.all())

    context = {
        'campaign': campaign,
        'questions_json': mark_safe(json.dumps(questions_json)),  # Safe for JSON in the template
    }
    return render(request, 'quiz_play.html', context)

def serialize_questions(questions):
    """Utility function to serialize questions and their choices into a JSON-friendly format."""
    questions_json = []
    for question in questions:
        choices = list(question.choices.values('id', 'text')) if question.type == 'MCQ' else None
        questions_json.append({
            'id': question.id,
            'text': question.text,
            'type': question.type,
            'choices': choices,
            'duration': question.duration,  # Assuming you have a duration field
        })
    return questions_json

# Additional views...
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


@login_required
@csrf_exempt  # Be cautious with CSRF exemption. Handling the CSRF token in AJAX is preferable.
def submit_quiz(request):
    if request.method == 'POST':
        answers_data = request.body.decode('utf-8')  # Getting raw body data
        try:
            submitted_answers = json.loads(answers_data).get('answers')  # Assuming 'answers' is wrapped in a key
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Bad request: Unable to parse JSON.'}, status=400)

        score = 0
        correct_answers = {}

        for question_id, user_answer in submitted_answers.items():
            try:
                question = Question.objects.get(pk=question_id)

                # For MCQs
                if question.type == 'MCQ':
                    correct_choice = question.choices.filter(is_correct=True).first()
                    if correct_choice and str(correct_choice.id) == user_answer:
                        score += 1  # Correct answer
                    correct_answers[question_id] = correct_choice.id if correct_choice else 'No correct answer'
                
                # For text response questions
                elif question.type == 'TXT':
                    if question.correct_text_answer.lower() == user_answer.lower():  # Assuming case-insensitive matching
                        score += 1  # Correct answer
                    correct_answers[question_id] = question.correct_text_answer  # Providing the correct answer for reference

            except ObjectDoesNotExist:
                correct_answers[question_id] = 'Question does not exist'

        total_questions = len(submitted_answers)
        result = {
            'score': score,
            'total': total_questions,
            'correct_answers': correct_answers,
        }
        return JsonResponse(result)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=405)



