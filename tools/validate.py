#!/usr/bin/env python3
"""validate.py [--check-media]: controleert releases/index.json (structuur, dubbele ID's, READY volledig, sha256 vs download)."""
import json, sys, hashlib, urllib.request
REQ = ["content_id","character","title","summary","status","media_url","sha256","technical_qa_pass","rights_checked","ai_generated","platforms","approved_via_claude","created_at"]
d = json.load(open(sys.argv[0].rsplit("/tools/",1)[0] + "/releases/index.json")) if "/tools/" in sys.argv[0] else json.load(open("releases/index.json"))
errs = []
if d.get("schema_version") != 1 or not isinstance(d.get("releases"), list): errs.append("schema")
ids = [r.get("content_id") for r in d.get("releases", [])]
if len(ids) != len(set(ids)): errs.append("dubbele content_id")
for r in d.get("releases", []):
    m = [k for k in REQ if k not in r]
    if m: errs.append(f"{r.get('content_id')}: mist {m}")
    if r.get("status") not in ("READY","HOLD"): errs.append(f"{r.get('content_id')}: status")
    if r.get("status") == "READY":
        if not (r.get("technical_qa_pass") and r.get("rights_checked") and r.get("ai_generated") is True and r.get("approved_via_claude") is True): errs.append(f"{r['content_id']}: READY onvolledig")
        if "--check-media" in sys.argv:
            b = urllib.request.urlopen(r["media_url"], timeout=60).read()
            if hashlib.sha256(b).hexdigest() != r["sha256"]: errs.append(f"{r['content_id']}: sha256 klopt niet")
print("FOUT: " + "; ".join(errs) if errs else f"OK ({len(ids)} releases)")
sys.exit(1 if errs else 0)
