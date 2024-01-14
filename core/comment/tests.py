import pytest

from core.fixtures.user import user
from core.fixtures.post import post
from core.comment.models import Comment


@pytest.mark.django_db
def test_comment(user, post):
    comment = Comment.objects.create(
        post=post, author=user, body='Test comment Body'
        )
    assert comment.post == post
    assert comment.author == user
    assert comment.body == 'Test comment Body'