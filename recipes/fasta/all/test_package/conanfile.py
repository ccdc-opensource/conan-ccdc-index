from conans import ConanFile


class TestPackage(ConanFile):
    
    def test(self):
        self.run("fasta36", run_environment=True)