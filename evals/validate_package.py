"""Dependency-free checks for this package's constrained metadata format, not model behavior."""
from pathlib import Path
import json
import re
import sys

REQUIRED = ['SKILL.md', 'README.md', 'CHANGELOG.md', 'LICENSE', 'SOURCES.md', 'agents/openai.yaml',
    'evals/cases.json', 'evals/README.md', 'evals/RESULTS.md', 'MERGE_NOTES.md',
    'references/interpretation-proposals.md', 'assets/handoff.md']
REQUIRED += ['references/'+n+'.md' for n in ('application-routing','interview-zh','essay-strategy',
    'undergraduate','research-applications','ps-sop-guide','program-fit','scoring','style-guide','revision-protocol')]
REQUIRED += ['assets/'+n+'.md' for n in ('diagnosis','paragraph-revision','fact-ledger','program-brief','draft','strategy-outline')]

def validate(root):
    root = Path(root).resolve()
    errors = []
    for name in REQUIRED:
        p = root/name
        if not p.is_file() or not p.read_text(encoding='utf-8').strip():
            errors.append('Missing/empty: '+name)
    if errors:
        return errors
    skill = (root/'SKILL.md').read_text()
    header = re.match(r'^---\n(.*?)\n---\n', skill, re.S)
    if not header or not re.search(r'^name: admitly-essay-coach$', header[1], re.M) or not re.search(r'^description: .{20,1024}$', header[1], re.M) or 'version: "0.3.2"' not in header[1]:
        errors.append('Invalid entrypoint metadata')
    ui = (root/'agents/openai.yaml').read_text()
    desc = re.search(r'short_description: "([^"]+)"', ui)
    if not desc or not 25 <= len(desc[1]) <= 64 or '$admitly-essay-coach' not in ui or 'allow_implicit_invocation: true' not in ui:
        errors.append('Invalid UI metadata')
    for p in root.rglob('*'):
        if p.is_symlink():
            errors.append('Symlink not portable: '+str(p.relative_to(root)))
        if p.is_file() and p.suffix == '.md':
            for dest in re.findall(r'\]\(([^)]+)\)', p.read_text()):
                if '://' in dest or dest.startswith('#'):
                    continue
                target = (p.parent/dest.split('#')[0]).resolve()
                if not target.is_relative_to(root) or not target.exists():
                    errors.append(f'Broken/outside link: {p.name} -> {dest}')
    # Only runtime entrypoint reachability counts; a link from a changelog is not routing.
    seen = set()
    pending = [root/'SKILL.md']
    while pending:
        page = pending.pop().resolve()
        if page in seen or not page.is_file() or not page.is_relative_to(root):
            continue
        seen.add(page)
        for dest in re.findall(r'\]\(([^)]+)\)', page.read_text()):
            if '://' not in dest and not dest.startswith('#'):
                target = (page.parent/dest.split('#')[0]).resolve()
                if target.suffix == '.md' and target.is_relative_to(root):
                    pending.append(target)
    for folder in ['references','assets']:
        for p in (root/folder).glob('*.md'):
            if p.resolve() not in seen:
                errors.append('Unreachable runtime module: '+str(p.relative_to(root)))
    try:
        data = json.loads((root/'evals/cases.json').read_text())
        cases = data['cases']
        if data['version'] != '0.3.2' or data['synthetic'] is not True:
            errors.append('Invalid eval metadata')
        if [c['id'] for c in cases] != [f'E{i:02}' for i in range(1,49)]:
            errors.append('Expected E01–E48 exactly once in order')
        for c in cases:
            if int(c['id'][1:]) >= 37 and (not isinstance(c.get('anti'),list) or len(c['anti']) < 1 or not all(isinstance(x,str) and x.strip() for x in c['anti'])):
                errors.append('Invalid anti criteria '+c['id'])
            if not isinstance(c.get('prompt'), str) or not c['prompt'].strip() or not isinstance(c.get('must'), list) or not c['must'] or not all(isinstance(x,str) and x.strip() for x in c['must']):
                errors.append('Invalid eval '+c['id'])
    except (ValueError, KeyError, TypeError) as e:
        errors.append('Malformed eval data: '+str(e))
    return errors

if __name__ == '__main__':
    errors = validate(Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1])
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(REQUIRED)} required files; metadata; UI; relative links; 48 synthetic cases; no symlinks')
