from django.shortcuts import get_object_or_404, render

from acervo.models import Autor


def autor_list(request):
    autores = Autor.objects.all()
    context = {"autores": autores}
    return render(request, "acervo/autor_list.html", context)


def autor_detail(request, pk):
    autor = get_object_or_404(Autor, id=pk)
    context = {"autor": autor}
    return render(request, "acervo/autor_detail.html", context)
