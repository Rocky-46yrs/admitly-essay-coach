"""Negative checks ensure damaged distributions are rejected."""
from pathlib import Path
import shutil
import tempfile
import unittest
from validate_package import validate

class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)/'skill'
        shutil.copytree(Path(__file__).resolve().parents[1], self.root, ignore=shutil.ignore_patterns('__pycache__'))
    def test_valid(self):
        self.assertEqual(validate(self.root), [])
    def test_missing_module(self):
        (self.root/'references/essay-strategy.md').unlink()
        self.assertTrue(validate(self.root))
    def test_broken_link(self):
        with (self.root/'README.md').open('a') as f: f.write('\n[bad](missing.md)\n')
        self.assertTrue(validate(self.root))
    def test_wrong_invocation(self):
        p=self.root/'agents/openai.yaml'
        p.write_text(p.read_text().replace('$admitly-essay-coach','$wrong'))
        self.assertTrue(validate(self.root))
    def test_duplicate_case(self):
        p=self.root/'evals/cases.json'
        p.write_text(p.read_text().replace('"E30"','"E29"'))
        self.assertTrue(validate(self.root))
    def test_symlink(self):
        (self.root/'alias').symlink_to('README.md')
        self.assertTrue(validate(self.root))

    def test_unreachable_runtime_module(self):
        (self.root/'references/orphan.md').write_text('# orphan')
        with (self.root/'README.md').open('a') as f: f.write('\n[orphan](references/orphan.md)\n')
        self.assertTrue(validate(self.root))
    def test_missing_anti(self):
        import json
        p=self.root/'evals/cases.json'
        d=json.loads(p.read_text());d['cases'][-1]['anti']=[]
        p.write_text(json.dumps(d,ensure_ascii=False))
        self.assertTrue(validate(self.root))
    def test_invalid_json(self):
        (self.root/'evals/cases.json').write_text('{')
        self.assertTrue(validate(self.root))
    def test_version_mismatch(self):
        p=self.root/'evals/cases.json'
        p.write_text(p.read_text().replace('0.3.2','9.9.9'))
        self.assertTrue(validate(self.root))

if __name__ == '__main__': unittest.main()
