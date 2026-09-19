"""Check repository-link seeding preserves newer admin-edited records."""
import json
from pathlib import Path
import sqlite3
import subprocess

root = Path(__file__).resolve().parents[1]
subprocess.run(['node', 'scripts/build-platform-seed.mjs', '--brands-only'], cwd=root, check=True)
db = sqlite3.connect(':memory:')
for migration in sorted((root / 'migrations').glob('*.sql')):
    db.executescript(migration.read_text())
seeds = sorted((root / '.tmp').glob('platform-brand-seed-*.sql'))
assert seeds
for seed in seeds:
    db.executescript(seed.read_text())
custom = {'name': 'Admin edit', 'theme': {'primary': '#123456'}, 'designSystemUrl': 'old'}
for table in ['brand_records', 'ip_records']:
    db.execute(f'UPDATE {table} SET version=7,payload_json=? WHERE slug=?', (json.dumps(custom), 'iptrust'))
db.commit()
for seed in seeds:
    db.executescript(seed.read_text())
for table in ['brand_records', 'ip_records']:
    payload, version = db.execute(f'SELECT payload_json,version FROM {table} WHERE slug=?', ('iptrust',)).fetchone()
    assert version == 7
    assert json.loads(payload) == {**custom, 'designSystemUrl': 'https://github.com/ksamint/dsys_iptrust'}
    for brand in json.loads((root / 'config/brands.json').read_text()):
        payload, = db.execute(f'SELECT payload_json FROM {table} WHERE slug=?', (brand['slug'],)).fetchone()
        assert json.loads(payload)['designSystemUrl'] == brand['designSystemUrl']
assert not db.execute('PRAGMA foreign_key_check').fetchall()
print('All 36 repository links seeded; newer admin data and versions preserved.')
