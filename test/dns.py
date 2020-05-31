import testinfra 

def test_named_is_installed(host):
    named = host.package("bind")
    assert named.is_installed
    assert named.version.startswith("9.11")

def test_named_running_and_enabled(host):
    named = host.service("named")
    assert named.is_running
    assert named.is_enabled

def test_os_release(host):
    assert host.file("/etc/os-release").contains("CentOS")

def test_sshd_inactive(host):
    assert host.service("sshd").is_running is True
