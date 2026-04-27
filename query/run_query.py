"""
run_query.py
Populates the pet-store data (same as pytest steps 1-7) then reads
query.txt from the repository root and writes response.txt.
"""

import json
import os
import sys
import requests

# ---------------------------------------------------------------------------
# Service URLs
# ---------------------------------------------------------------------------
STORE1 = "http://localhost:5001"
STORE2 = "http://localhost:5002"
ORDER  = "http://localhost:5003"

# ---------------------------------------------------------------------------
# Pet type payloads (identical to assn4_tests.py)
# ---------------------------------------------------------------------------
PET_TYPE1 = {"type": "Golden Retriever"}
PET_TYPE2 = {"type": "Australian Shepherd"}
PET_TYPE3 = {"type": "Abyssinian"}
PET_TYPE4 = {"type": "bulldog"}

PET1_TYPE1 = {"name": "Lander",  "birthdate": "14-05-2020"}
PET2_TYPE1 = {"name": "Lanky"}
PET3_TYPE1 = {"name": "Shelly",  "birthdate": "07-07-2019"}
PET4_TYPE2 = {"name": "Felicity","birthdate": "27-11-2011"}
PET5_TYPE3 = {"name": "Muscles"}
PET6_TYPE3 = {"name": "Junior"}
PET7_TYPE4 = {"name": "Lazy",    "birthdate": "07-08-2018"}
PET8_TYPE4 = {"name": "Lemon",   "birthdate": "27-03-2020"}


# ---------------------------------------------------------------------------
# Step 2: populate data (pytest steps 1-7)
# ---------------------------------------------------------------------------
def populate_data():
    ids = {}

    # POST pet types to store 1
    r = requests.post(f"{STORE1}/pet-types", json=PET_TYPE1)
    ids['id_1'] = r.json()['id']
    r = requests.post(f"{STORE1}/pet-types", json=PET_TYPE2)
    ids['id_2'] = r.json()['id']
    r = requests.post(f"{STORE1}/pet-types", json=PET_TYPE3)
    ids['id_3'] = r.json()['id']

    # POST pet types to store 2
    r = requests.post(f"{STORE2}/pet-types", json=PET_TYPE1)
    ids['id_4'] = r.json()['id']
    r = requests.post(f"{STORE2}/pet-types", json=PET_TYPE2)
    ids['id_5'] = r.json()['id']
    r = requests.post(f"{STORE2}/pet-types", json=PET_TYPE4)
    ids['id_6'] = r.json()['id']

    # POST pets to store 1
    requests.post(f"{STORE1}/pet-types/{ids['id_1']}/pets", json=PET1_TYPE1)
    requests.post(f"{STORE1}/pet-types/{ids['id_1']}/pets", json=PET2_TYPE1)
    requests.post(f"{STORE1}/pet-types/{ids['id_3']}/pets", json=PET5_TYPE3)
    requests.post(f"{STORE1}/pet-types/{ids['id_3']}/pets", json=PET6_TYPE3)

    # POST pets to store 2
    requests.post(f"{STORE2}/pet-types/{ids['id_4']}/pets", json=PET3_TYPE1)
    requests.post(f"{STORE2}/pet-types/{ids['id_5']}/pets", json=PET4_TYPE2)
    requests.post(f"{STORE2}/pet-types/{ids['id_6']}/pets", json=PET7_TYPE4)
    requests.post(f"{STORE2}/pet-types/{ids['id_6']}/pets", json=PET8_TYPE4)

    print(f"[populate] IDs: {ids}", flush=True)
    return ids


# ---------------------------------------------------------------------------
# Parse query.txt
# ---------------------------------------------------------------------------
def parse_query_file(filepath):
    """
    Returns a list of entries.
    Each entry is either:
      ('query',    store_num_str, query_string)
      ('purchase', json_str)
    """
    with open(filepath, 'r') as f:
        content = f.read()

    entries = []
    # Split on ';' — each entry ends with one
    parts = [p.strip() for p in content.split(';') if p.strip()]

    for part in parts:
        # Collapse internal newlines/spaces
        part = ' '.join(part.split())

        if part.startswith('query:'):
            rest = part[len('query:'):].strip()
            # Format: "<store_num>,<field>=<value>"
            comma_idx = rest.index(',')
            store_num    = rest[:comma_idx].strip()
            query_string = rest[comma_idx + 1:].strip()
            entries.append(('query', store_num, query_string))

        elif part.startswith('purchase:'):
            rest = part[len('purchase:'):].strip()
            entries.append(('purchase', rest))

    return entries


# ---------------------------------------------------------------------------
# Execute a single entry
# ---------------------------------------------------------------------------
def execute_entry(entry):
    if entry[0] == 'query':
        _, store_num, query_string = entry
        port = 5000 + int(store_num)
        url  = f"http://localhost:{port}/pet-types?{query_string}"
        resp = requests.get(url)

        status = resp.status_code
        if status == 200:
            payload = json.dumps(resp.json(), indent=2)
        else:
            payload = "NONE"

    elif entry[0] == 'purchase':
        _, json_str = entry
        payload_data = json.loads(json_str)
        resp = requests.post(
            f"{ORDER}/purchases",
            json=payload_data,
            headers={"Content-Type": "application/json"}
        )
        status = resp.status_code
        if status == 201:
            payload = json.dumps(resp.json(), indent=2)
        else:
            payload = "NONE"

    else:
        status  = 400
        payload = "NONE"

    return status, payload


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("[query_job] Populating data ...", flush=True)
    populate_data()

    query_file = 'query.txt'
    if not os.path.exists(query_file):
        print(f"[query_job] ERROR: {query_file} not found", flush=True)
        sys.exit(1)

    print(f"[query_job] Parsing {query_file} ...", flush=True)
    entries = parse_query_file(query_file)
    print(f"[query_job] Found {len(entries)} entries", flush=True)

    output_lines = []
    for entry in entries:
        status, payload = execute_entry(entry)
        print(f"[query_job] {entry[0]} → {status}", flush=True)
        output_lines.append(f"{status}\n{payload}\n;")

    with open('response.txt', 'w') as f:
        f.write('\n'.join(output_lines) + '\n')

    print("[query_job] response.txt written successfully", flush=True)


if __name__ == '__main__':
    main()
