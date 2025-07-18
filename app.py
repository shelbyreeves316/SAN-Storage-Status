import json
import re
import subprocess
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, text=True)
    except FileNotFoundError:
        return ''
    except subprocess.CalledProcessError as e:
        return e.output

def get_smart_status(device):
    output = run_cmd(['smartctl', '-H', device])
    status = 'unknown'
    alert = None
    for line in output.splitlines():
        if 'SMART overall-health self-assessment test result' in line:
            status = line.split(':')[-1].strip()
            if status.lower() != 'passed':
                alert = status
    return {'status': status, 'alert': alert}

def get_btrfs_usage(path):
    output = run_cmd(['btrfs', 'filesystem', 'usage', '-h', path])
    # use first line as summary
    for line in output.splitlines():
        if 'Overall:' in line or 'Device size:' in line:
            return line.strip()
    return ''

def parse_btrfs():
    output = run_cmd(['btrfs', 'filesystem', 'show', '--raw'])
    volumes = []
    current = None
    for line in output.splitlines():
        m = re.match(r"Label:\s+'?([^']*)'?.*uuid:\s+([0-9a-fA-F-]+)", line)
        if m:
            if current:
                volumes.append(current)
            current = {'label': m.group(1), 'uuid': m.group(2), 'drives': []}
            continue
        m = re.match(r"\s*devid\s+(\d+)\s+size\s+(\S+)\s+used\s+(\S+)\s+path\s+(\S+)", line)
        if m and current is not None:
            devid, size, used, path = m.groups()
            drive = {
                'devid': devid,
                'size': size,
                'used': used,
                'path': path,
                'smart': get_smart_status(path)
            }
            current['drives'].append(drive)
    if current:
        volumes.append(current)
    # add usage info
    for vol in volumes:
        if vol['drives']:
            vol['usage'] = get_btrfs_usage(vol['drives'][0]['path'])
    return volumes

@app.route('/api/status')
def api_status():
    volumes = parse_btrfs()
    if not volumes:
        return jsonify(error='No BTRFS volumes found or btrfs command missing'), 200
    return jsonify(volumes=volumes)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
