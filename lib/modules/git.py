import subprocess


class GitControl(object):
    def __init__(self, repo_config):
        self._repoDir = repo_config.dir if (dir in repo_config) else False
        self._remoteUrl = repo_config.url
        self._remoteName = repo_config.remote

    def add(self, add_string):
        cmd = ['git', 'add', add_string]
        p = subprocess.Popen(cmd, cwd=self._repoDir)
        p.wait()

    def clone(self):
        cmd = ['git', 'clone', self._remoteUrl]
        if self._repoDir:
            cmd.append(self._repoDir)
        p = subprocess.Popen(cmd, cwd='~')
        p.wait()

    def status(self):
        cmd = ['git', 'status']
        p = subprocess.Popen(cmd, cwd=self._repoDir)
        p.wait()
