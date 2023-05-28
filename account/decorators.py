from functools import wraps
from django.urls import reverse
from django.http import HttpResponseRedirect


def has_group(group: str, redirect_to="index"):
  def inner_render(fn):
    @wraps(fn)  # Ensure the wrapped function keeps the same name as the view
    def wrapped(request, *args, **kwargs):
      if request.user.is_authenticated:
        if request.user.groups.filter(name=group).exists():
          return fn(request, *args, **kwargs)
        else:
          return HttpResponseRedirect(reverse(redirect_to))
      else:
        return HttpResponseRedirect(reverse(redirect_to))
    return wrapped
  return inner_render