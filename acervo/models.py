from django.db import models
from django.utils.translation import gettext_lazy as _


class Autor(models.Model):
    nome = models.CharField(_("nome"), max_length=200)
    email = models.EmailField(_("email"), blank=True)
    data_nascimento = models.DateField(
        _("data de nascimento"),
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("nome", "id")
        verbose_name = _("livro")
        verbose_name_plural = _("livros")

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(_("título"), max_length=255)
    data_lancamento = models.DateField(
        _("data de lançamento"),
        null=True,
        blank=True,
    )
    resumo = models.TextField(_("resumo"), blank=True)
    editora = models.CharField(_("editora"), max_length=100)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name="livros",
        verbose_name=_("autor"),
    )

    class Meta:
        ordering = ("titulo", "data_lancamento", "id")
        verbose_name = _("livro")
        verbose_name_plural = _("livros")

    def __str__(self):
        return self.titulo
