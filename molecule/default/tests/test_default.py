import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_promtail_is_installed(host):
    assert host.exists('promtail')


def test_promtail_running_and_enabled(host):
    service = host.service('promtail')
    assert service.is_running
    assert service.is_enabled


def test_promtail_is_listen(host):
    assert host.socket('tcp://0.0.0.0:9080').is_listening


def test_loki_is_installed(host):
    assert host.exists('loki')


def test_loki_running_and_enabled(host):
    service = host.service('loki')
    assert service.is_running
    assert service.is_enabled


def test_loki_is_listen(host):
    assert host.socket('tcp://0.0.0.0:3100').is_listening
