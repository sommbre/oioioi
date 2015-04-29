from django.db import models
from django.utils.translation import ugettext_lazy as _
from oioioi.base.utils.deps import check_django_app_dependencies
from oioioi.contests.models import Submission, Contest


check_django_app_dependencies(__name__, ['oioioi.disqualification'],
                              strict=True)


class SubmissionsSimilarityGroup(models.Model):
    contest = models.ForeignKey(Contest, verbose_name=_("contest"))
    comment = models.TextField(blank=True, verbose_name=_("admin comment"))

    class Meta(object):
        verbose_name = _("submissions similarity")
        verbose_name_plural = _("submissions similarities")


class SubmissionsSimilarityEntry(models.Model):
    submission = models.ForeignKey(Submission,
        verbose_name=_("submission"), related_name='similarities')
    group = models.ForeignKey(SubmissionsSimilarityGroup,
        verbose_name=_("group"), related_name='submissions')
    guilty = models.BooleanField(default=True, verbose_name=_("guilty"))

    class Meta(object):
        verbose_name = _("submissions similarity entry")
        verbose_name_plural = _("submissions similarity entries")
        unique_together = (('submission', 'group'),)