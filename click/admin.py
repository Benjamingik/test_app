from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from click.models import Exercise, Subject, Variant, Result, Topic, Teacher


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Variant)
class VariantAdmin(TranslationAdmin):
    list_display = ['title']
    list_filter = ['subject']
    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


# class AnswerAdmin(admin.TabularInline):
#     model = Answer
#     extra = 4

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_filter = ['variant']
    group_fieldsets = True

    def get_object(self, request, *args, **kwargs):
        request_admin_obj = super(ExerciseAdmin, self).get_object(*args, **kwargs)
        return request_admin_obj

    # def render_change_form(self, request, context, *args, **kwargs):
    #     context['adminform'].form.fields['teacher'].queryset = Teacher.objects.filter(user=request.user)
    #     context['adminform'].form.fields['subject'].queryset = Subject.objects.filter(teacher__user=request.user)
    #     return super(VariantAdmin, self).render_change_form(request, context, *args, **kwargs)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_filter = ['subject']
