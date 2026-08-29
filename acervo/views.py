from django.shortcuts import get_object_or_404, render

from acervo.models import Autor, Livro


def autor_list(request):
    autores = Autor.objects.all()
    context = {"autores": autores}
    return render(request, "acervo/autor_list.html", context)


def autor_detail(request, pk):
    autor = get_object_or_404(Autor, id=pk)
    context = {"autor": autor}
    return render(request, "acervo/autor_detail.html", context)


def livro_list(request):
    livros = Livro.objects.all()
    context = {"livros": livros}
    return render(request, "acervo/livro_list.html", context)


def livro_detail(request, pk):
    livro = get_object_or_404(Livro, id=pk)
    context = {"livro": livro}
    return render(request, "acervo/livro_detail.html", context)
