import requests


def test_binder_up(binder_url):
    """
    Binder Hub URL is up & returning sensible text
    """
    resp = requests.get(binder_url)
    assert resp.status_code == 200
    assert 'GitHub' in resp.text


def test_hub_up(hub_url):
    """
    JupyterHub url is up and returning sensible result (403)
    """
    resp = requests.get(hub_url)
    # 403 is expected since we are using nullauthenticator
    # FIXME: Have a dedicated health check endpoint for the hub
    assert resp.status_code == 403


def test_hub_user_redirect(hub_url):
    """Requesting a Hub URL for a non-running user"""
    # this should *not* redirect for now,
    resp = requests.get(hub_url + "/user/doesntexist")
    assert resp.status_code == 404

