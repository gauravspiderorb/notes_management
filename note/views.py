from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ModelNote
from .forms import FormNote


class ViewNoteList(ListView):
    model = ModelNote
    template_name = 'note/note_list.html'	# Default: <app_label>/<model_name>_list.html
    context_object_name = 'notes'  # Default: object_list
    paginate_by = 5
    queryset = ModelNote.objects.all()  # Default: Model.objects.all()


class ViewNoteCreate(CreateView):
    form_class = FormNote
    model = ModelNote
    success_url = reverse_lazy('home')
    template_name = 'note/note_template.html'


class ViewNoteDelete(DeleteView):
    model = ModelNote
    success_url = reverse_lazy('home')
    template_name = 'note/note_confirm_delete.html'


class ViewNoteUpdate(UpdateView):
    model = ModelNote
    form_class = FormNote
    success_url = reverse_lazy('home')
    template_name = 'note/note_update.html'


class ViewNoteDetail(DetailView):
    model = ModelNote
    template_name = 'note/note_detail.html'


class ViewNoteTemplate(ListView):
    model = ModelNote
    template_name = 'core/note_list.html'  # Default: <app_label>/<model_name>_list.html
    # context_object_name = 'notes'  # Default: object_list
    paginate_by = 2
    queryset = ModelNote.objects.all()  # Default: Model.objects.all()





