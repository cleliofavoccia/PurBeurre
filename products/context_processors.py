"""Context usable in all templates of the project"""
from .forms import SubstituteForm


def get_substitute_form(request):
    """Print a form to post data on SubstituteForm
    of products app"""
    form = SubstituteForm(request.POST or None)
    return {'substitute_form': form}
