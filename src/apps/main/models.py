from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from model_utils.choices import Choices
from solo.models import SingletonModel

__all__ = [
    'Config',
    'Game',
    'Location',
    'Transition'
]

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Config(SingletonModel):
    bool_expression_rules = models.TextField(_('bool expression rules'))
    state_expression_rules = models.TextField(_('state expression rules'))

    class Meta:
        verbose_name = _('config')


class Game(models.Model):
    title = models.CharField(_('title'), max_length=256)
    description = models.TextField(_('title'))
    initial_state = JSONField(_('initial state (rules)'), default=dict,
                              blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')


class Location(models.Model):
    TYPE_CHOICES = Choices(
        (0, 'DEFAULT', _('Default')),
        (1, 'START', _('Is Start')),
        (2, 'Finish', _('Is Finish')),
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE,
                             related_name='locations')
    name = models.CharField(_('name'), max_length=512)
    description = models.TextField(_('description'), max_length=512)
    type = models.SmallIntegerField(_('type'), choices=TYPE_CHOICES,
                                    default=TYPE_CHOICES.DEFAULT)
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

    # human readable rules
    condition = models.CharField(
        _('condition (readable)'), blank=True, max_length=1024
    )
    state = JSONField(
        _('statement (readable)'), blank=True, default=dict
    )

    # json structured rules
    condition_rules = JSONField(
        _('condition (rules)'), blank=True, default=dict
    )
    state_rules = JSONField(
        _('state (rules)'), blank=True, default=dict
    )

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


def set_is_start_value(instance, **kwargs):
    if instance.type == Location.TYPE_CHOICES.START:
        instance.game.locations\
            .exclude(id=instance.id)\
            .filter(type=Location.TYPE_CHOICES.START)\
            .update(type=Location.TYPE_CHOICES.DEFAULT)


post_save.connect(set_is_start_value, sender=Location)
