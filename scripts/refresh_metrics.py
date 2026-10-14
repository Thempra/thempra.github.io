#!/usr/bin/env python3
"""Refresh live metrics for the portfolio from GitHub + SonarQube + DefectDojo.

Tokens are read from local files and NEVER committed. Prints a JSON snapshot
that can be pasted into index.html metric cells. Run from anywhere:
    python3 scripts/refresh_metrics.py
"""
import json, re, subprocess, sys

PROJECTS = {  # slug -> (sonar key or None, defectdojo product or None)
    "qzero": ("qzero", "qzero"),
    "vagustrader": ("vagustrader", "vagustrader"),
    "overmind-ng": ("overmind_flutter", "overmind_flutter"),
    "kidsclock": (None, None),
}

def _tok(path):
    try: return open(path).read().strip()
    except FileNotFoundError: return None

def curl(args, url):
    r = subprocess.run(["curl", "-s"] + args + [url], capture_output=True, text=True, timeout=30)
    try: return json.loads(r.stdout)
    except Exception: return {}

def main():
    gh_tok = None
    for line in open(f"{__import__('os').environ['HOME']}/.git-credentials"):
        m = re.match(r"https://[^:]+:([^@]+)@github.com", line.strip())
        if m: gh_tok = m.group(1)
    sonar = _tok(f"{__import__('os').environ['HOME']}/.sonar_token")
    dd = _tok(f"{__import__('os').environ['HOME']}/.defectdojo_token")

    out = {}
    for slug, (sk, dp) in PROJECTS.items():
        rec = {}
        if gh_tok:
            d = curl(["-H", f"Authorization: Bearer {gh_tok}"],
                     f"https://api.github.com/repos/Thempra/{slug}")
            rec["pushed_at"] = d.get("pushed_at")
            rec["language"] = d.get("language")
        if sonar and sk:
            m = curl(["-u", sonar + ":"],
                     "https://sast.thempra.net/api/measures/component?component=%s"
                     "&metricKeys=ncloc,bugs,vulnerabilities,code_smells,coverage" % sk)
            rec["sonar"] = {x["metric"]: x.get("value")
                            for x in m.get("component", {}).get("measures", [])}
        if dd and dp:
            c = curl(["--resolve", "dojo.thempra.net:443:192.168.50.5",
                      "-H", "Authorization: Token " + dd],
                     "https://dojo.thempra.net/api/v2/findings/?product_name=%s"
                     "&active=true&severity=High&limit=1" % dp)
            rec["dd_high_active"] = c.get("count")
        out[slug] = rec
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    sys.exit(main())
