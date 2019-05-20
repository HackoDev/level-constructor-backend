from django.core.exceptions import ValidationError

__all__ = [
    'Game',
    'Location',
    'Transition'
]

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Game(models.Model):
    title = models.CharField(_('title'), max_length=256)
    description = models.TextField(_('title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')


class Location(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE,
                             related_name='locations')
    name = models.CharField(_('name'), max_length=512)
    description = models.TextField(_('description'), max_length=512)
    is_start = models.BooleanField(_('is start'))
    is_finish = models.BooleanField(_('is finish'))
    meta = JSONField(_('meta'), default=dict, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Location')


class Transition(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True,
                             related_name='transitions',
                             verbose_name=_('Game'))
    source = models.ForeignKey(Location, on_delete=models.CASCADE,
                               related_name='source_transitions',
                               verbose_name=_('source location'))
    target = models.ForeignKey(Location, on_delete=models.CASCADE,
                               related_name='target_transitions',
                               verbose_name=_('target location'))
    condition = JSONField(_('condition'), blank=True, default=dict)
    state = JSONField(_('state'), blank=True, default=dict)
    position = models.PositiveIntegerField(_('position'))
    weight = models.PositiveIntegerField(_('weight'))
    is_visible = models.BooleanField(_('is visible'))
    meta = JSONField(_('meta'), default=dict, blank=True)

    def __str__(self):
        return '{} -> {}'.format(self.source, self.target)

    class Meta:
        verbose_name = _('Transition')
        verbose_name_plural = _('Transitions')

    def clean(self):
        if self.source.game != self.target.game:
            raise ValidationError({
                'source': _('Should have same game relation'),
                'target': _('Should have same game relation')
            })
        if self.source == self.target:
            raise ValidationError({
                'source': _('Cannot use same `source` and `target`'),
                'target': _('Cannot use same `source` and `target`')
            })

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.game_id = self.target.game_id
        super().save(*args, **kwargs)
