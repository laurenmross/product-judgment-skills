#!/usr/bin/env python3
"""Check this repository's intentionally small frontmatter subset and packaging."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'diagnose-product-performance', 'conviction-under-uncertainty',
    'second-order-thinking', 'evaluate-product-investment',
    'resolve-competing-objectives',
}


def validate(root):
    errors = []
    safeguards = {}
    def check(condition, message):
        if not condition:
            errors.append(message)
    folders = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
    check(folders == EXPECTED, 'Skill directory set differs from expected five')
    for name in sorted(EXPECTED):
        path = root / 'skills' / name / 'SKILL.md'
        if not path.is_file():
            errors.append(f'{name}: missing SKILL.md')
            continue
        text = path.read_text()
        match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        if not match:
            errors.append(f'{name}: invalid frontmatter boundaries')
            continue
        fields = {}
        for line in match[1].splitlines():
            key, sep, value = line.partition(': ')
            check(bool(sep) and key not in fields, f'{name}: invalid/duplicate field')
            fields[key] = value
        check(set(fields) == {'name', 'description', 'license'}, f'{name}: unexpected frontmatter fields')
        check(fields.get('name') == name and len(name) <= 64, f'{name}: name mismatch')
        check(fields.get('license') == 'MIT', f'{name}: license mismatch')
        try:
            desc = json.loads(fields.get('description', 'null'))
            check(isinstance(desc, str) and 0 < len(desc) <= 1024, f'{name}: invalid description')
        except ValueError:
            errors.append(f'{name}: description must be a JSON-quoted YAML string')
        for section in ['Procedure', 'Evidence and uncertainty safeguards', 'Output template', 'Example uses']:
            check('## ' + section in text, f'{name}: missing {section}')
        check('[TODO:' not in text, f'{name}: unfinished scaffold')
        check('](references/worked-example.md)' in text and (path.parent / 'references/worked-example.md').is_file(), f'{name}: missing linked worked example')
        check(text.count('```') % 2 == 0, f'{name}: unbalanced code fences')
        block = re.search(r'## Evidence and uncertainty safeguards\n(.*?)\n## ', text, re.S)
        if block:
            safeguards.setdefault(block[1].strip(), []).append(name)
    check(len(safeguards) <= 1, 'Shared safeguards text differs between skills: '
          + '; '.join(', '.join(v) for v in safeguards.values()))
    for name in ['README.md', 'LICENSE', 'evaluations/README.md', 'evaluations/cases.json']:
        check((root / name).is_file(), f'Missing {name}')
    for path in root.rglob('*.md'):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            if '://' not in target and not target.startswith('#'):
                check((path.parent / target.split('#')[0]).exists(), f'{path.relative_to(root)}: broken link {target}')
    try:
        cases = json.loads((root / 'evaluations/cases.json').read_text())
        check({c['skill'] for c in cases} == EXPECTED, 'Evaluation coverage differs from skill set')
        check(len({c['id'] for c in cases}) == len(cases), 'Duplicate evaluation IDs')
        for case in cases:
            check(all(case.get(k) for k in ['id', 'skill', 'prompt', 'must_include', 'critical_failures']), 'Incomplete case')
            check(all(isinstance(case[k], list) for k in ['must_include', 'critical_failures']), 'Invalid criteria lists')
    except (ValueError, KeyError, OSError, TypeError) as exc:
        errors.append(f'Evaluation fixture error: {exc}')
    return errors


if __name__ == '__main__':
    problems = validate(ROOT)
    for problem in problems:
        print('FAIL:', problem)
    if not problems:
        count = len(json.loads((ROOT / 'evaluations/cases.json').read_text()))
        print(f'PASS: 5 skills; frontmatter, shared safeguards, sections, local links, and {count} evaluation fixtures validated.')
    sys.exit(bool(problems))
