from check_linux import site_vulnerable


def test_site(site):
    assert site_vulnerable(site), f'Site {site} is vulnerable'