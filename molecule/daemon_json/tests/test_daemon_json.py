import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


# Test that the daemon.json was installed and looks good
def test_daemon_json(host):
    # Only a CentOS box is being tested for this one
    host.run("yum -y install jq")
    assert host.run_test('[ $(jq \'.["log-driver"] == "json-file"\' /etc/docker/daemon.json) = "true" ]').exit_status == 0
