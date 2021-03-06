"""
Tests for main views module.
"""

import pytest

from django.core.urlresolvers import reverse


USERNAME = 'test'
PASSWORD = 'pass'


def test_views_anon(client):
    for view, kwargs, status_code in [
        ('home', dict(), 200),
        ('about', dict(), 200),
        ('legal', dict(), 200),
        ('robots', dict(), 200),
        # stuff that requires being logged-in redirects to the login view:
        ('status', dict(), 302),
        ('overview', dict(), 302),
        ('domain_overview', dict(), 302),
        ('host_view', dict(pk=1), 302),
        ('domain_view', dict(pk=1), 302),
        ('generate_secret_view', dict(pk=1), 302),
        ('generate_ns_secret_view', dict(pk=1), 302),
        ('delete_host', dict(pk=1), 302),
        ('delete_domain', dict(pk=1), 302),
    ]:
        print view, kwargs, status_code
        response = client.get(reverse(view, kwargs=kwargs))
        assert response.status_code == status_code


def test_views_logged_in(client):
    client.login(username=USERNAME, password=PASSWORD)
    for view, kwargs, status_code in [
        ('home', dict(), 200),
        ('about', dict(), 200),
        ('legal', dict(), 200),
        ('robots', dict(), 200),
        ('status', dict(), 200),
        ('overview', dict(), 200),
        ('domain_overview', dict(), 200),
        ('host_view', dict(pk=1), 200),
        ('domain_view', dict(pk=1), 200),
        ('generate_secret_view', dict(pk=1), 200),
        ('generate_ns_secret_view', dict(pk=1), 200),
        ('delete_host', dict(pk=1), 200),
        ('delete_domain', dict(pk=1), 200),
    ]:
        print view, kwargs, status_code
        response = client.get(reverse(view, kwargs=kwargs))
        assert response.status_code == status_code
