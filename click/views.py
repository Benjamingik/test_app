from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

import user
from click.admin import ExerciseAdmin
from click.forms import VariantForm, ExerciseFormSet

from click.models import Exercise, Subject, Variant, Result, UserAnswer


def index_view(request):
    return render(request, 'pages/home_page.html')


def subject_list_view(request):
    user = request.user
    if user.is_authenticated:
        subject_list = Subject.objects.all()
        if user.is_staff:
            subject_list = subject_list.filter(teacher__user=user)
        context = {
            'subject_list': subject_list
        }
        return render(request, 'pages/subject_page.html', context)
    return redirect('accaunt:login')


def subject_view(request, pk):
    variant_list = Variant.objects.filter(subject_id=pk)
    # print(variant_list)
    subject = Subject.objects.get(id=pk)
    context = {
        'subject': subject,
        'variant_list': variant_list
    }
    return render(request, 'pages/variant_page.html', context)


# def variant_view(request, pk):
#     context = {
#         'variant': Variant.objects.get(id=pk),
#         'exercise_list': Exercise.objects.filter(variant_id=pk)
#     }
#     return render(request, 'pages/exercise_page.html', context)


@login_required
def variant_view(request, pk):
    exercise_list = Exercise.objects.filter(variant_id=pk)
    variant = Variant.objects.get(id=pk)
    if request.method == 'GET':
        template = 'pages/exercise_page.html'
        if request.user.is_stuff:
            template = 'pages/variant_edit.html'
        context = {
            'variant': variant,
            'exercise_list': exercise_list
        }
        return render(request, 'pages/exercise_page.html', context)
    if request.method == 'POST':
        data = request.POST
        result = Result.objects.create(user=request.user, variant=variant)
        for exercise in exercise_list:
            user_answer = UserAnswer(result=result, exercise=exercise)
            if data.get(str(exercise.id)) is not None:
                user_answer.user_answer = data.get(str(exercise.id))
                if exercise.answer == data.get(exercise.id):
                    user_answer.is_True = True
            user_answer.save()
        # return HttpResponseRedirect(reverse_lazy('click:result_list'))
        return redirect('click:result', pk=result.id)


def result_list_view(request):
    context = {
        'result_list': request.user.results.all()
    }
    return render(request, 'pages/result_list_page.html', context=context)


def result_view(request, pk):
    result = Result.objects.get(id=pk, user=request.user)
    object_list = []
    ua = UserAnswer.objects.filter(result=result, is_True=True)
    # variant = result.variant
    for exercise in result.variant.exercises.all():
        object_list.append({
            'exercise': exercise,
            'user_answer': exercise.user_answers.get(result=result).user_answer,
            'is_true': exercise.user_answers.get(result=result).is_True
        })
    context = {
        'object_list': object_list,
        'ball': len(ua),
        'count': len(result.variant.exercises.all())
    }
    return render(request, 'pages/result_page.html', context=context)


def logout_view(request):
    logout_view(request)
    return redirect('home')


class VariantCreateView(View):
    def get(self, request):
        context = {
            'variant_form': VariantForm(),
            'formset': ExerciseFormSet(instance=Variant())
            }

        return render(request, 'pages/variant_create.html', context=context)

    def post(self, request):
        variant_form = VariantForm(request.POST)
        formset = ExerciseFormSet(request.POST, instance=Variant())

        if variant_form.is_valid() and formset.is_valid():
            variant = variant_form.save()
            formset.instance = variant
            formset.save()
            return redirect('home')
