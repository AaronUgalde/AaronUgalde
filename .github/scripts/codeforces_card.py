"""Draw my Codeforces rating history and solved problems as light/dark SVG cards."""
import collections
import datetime
import json
import sys
import urllib.request

HANDLE = "LicAaron"
OUT = sys.argv[1] if len(sys.argv) > 1 else "assets"

THEMES = {
    "dark": dict(bg="#0d1117", fg="#e6edf3", muted="#8b949e", faint="#21262d", stop="#0d1117"),
    "light": dict(bg="#ffffff", fg="#1f2328", muted="#59636e", faint="#eaeef2", stop="#ffffff"),
}
# Codeforces rank bands: (lower bound, name, color)
BANDS = [
    (0, "newbie", "#808080"),
    (1200, "pupil", "#3fa34d"),
    (1400, "specialist", "#03a89e"),
    (1600, "expert", "#3b6cf6"),
    (1900, "candidate master", "#aa00aa"),
    (2100, "master", "#ff8c00"),
]


def api(method):
    with urllib.request.urlopen(f"https://codeforces.com/api/{method}", timeout=30) as resp:
        data = json.load(resp)
    if data["status"] != "OK":
        raise RuntimeError(data.get("comment"))
    return data["result"]


def band(rating):
    return [b for b in BANDS if rating >= b[0]][-1]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


def render(c, info, history, solved):
    W, H = 900, 260
    rating, top = info.get("rating", 0), info.get("maxRating", 0)
    _, rank, color = band(rating)
    year = datetime.date.today().year
    this_year = sum(1 for t, _ in solved.values() if datetime.datetime.fromtimestamp(t, datetime.timezone.utc).year == year)

    # Rating chart, drawn as a transit line: one station per rated contest.
    cx0, cx1, cy0, cy1 = 400, 860, 40, 200
    ratings = [h["newRating"] for h in history] or [rating]
    lo = min(ratings + [1100]) // 100 * 100 - 100
    hi = max(ratings + [1500]) // 100 * 100 + 100

    def y(r):
        return cy1 - (r - lo) / (hi - lo) * (cy1 - cy0)

    def x(i):
        return cx0 + (i / max(len(ratings) - 1, 1)) * (cx1 - cx0)

    parts = []
    for lower, _, col in BANDS:
        upper = next((b[0] for b in BANDS if b[0] > lower), 10_000)
        a, b = max(lower, lo), min(upper, hi)
        if a < b:
            parts.append(f'<rect x="{cx0 - 12}" y="{y(b):.1f}" width="{cx1 - cx0 + 24}" height="{y(a) - y(b):.1f}" fill="{col}" fill-opacity=".10"/>')
    for r in range(lo + 100, hi, 200):
        parts.append(f'<text x="{cx0 - 20}" y="{y(r) + 4:.1f}" text-anchor="end" class="tick">{r}</text>')
    for i in range(1, len(ratings)):
        seg = band(ratings[i])[2]
        parts.append(f'<line x1="{x(i - 1):.1f}" y1="{y(ratings[i - 1]):.1f}" x2="{x(i):.1f}" y2="{y(ratings[i]):.1f}" stroke="{seg}" stroke-width="6" stroke-linecap="round"/>')
    for i, r in enumerate(ratings):
        rc = band(r)[2]
        last = i == len(ratings) - 1
        if last:
            parts.append(f'<circle cx="{x(i):.1f}" cy="{y(r):.1f}" r="9" fill="{c["stop"]}" stroke="{c["fg"]}" stroke-width="4"/>'
                         f'<circle cx="{x(i):.1f}" cy="{y(r):.1f}" r="3.5" fill="{c["fg"]}"/>')
        else:
            parts.append(f'<circle cx="{x(i):.1f}" cy="{y(r):.1f}" r="5" fill="{c["stop"]}" stroke="{rc}" stroke-width="3"/>')
    chart = "".join(parts)
    first = history[0]["ratingUpdateTimeSeconds"] if history else None
    since = datetime.datetime.fromtimestamp(first, datetime.timezone.utc).strftime("%b %Y") if first else ""

    # Solved problems by difficulty.
    by_diff = collections.Counter(r for _, r in solved.values() if r)
    diffs = list(range(800, 2000, 100))
    peak = max([by_diff[d] for d in diffs] + [1])
    bars = []
    for i, d in enumerate(diffs):
        h = by_diff[d] / peak * 50
        bx = 40 + i * 25
        bars.append(f'<rect x="{bx}" y="{222 - h:.1f}" width="18" height="{max(h, 1.5):.1f}" rx="2" fill="{band(d)[2]}"/>')
    bars.append('<text x="40" y="240" class="tick">800</text><text x="186" y="240" text-anchor="middle" class="tick">by difficulty</text><text x="333" y="240" text-anchor="end" class="tick">1900</text>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Codeforces {esc(info["handle"])}: rating {rating} ({rank}), max {top}, {len(solved)} problems solved over {len(history)} rated contests.">
  <style>
    .k {{ font: 400 12px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: {c["muted"]}; }}
    .h {{ font: 700 24px -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; fill: {c["fg"]}; }}
    .r {{ font: 600 15px -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; fill: {color}; }}
    .n {{ font: 700 22px -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; fill: {c["fg"]}; }}
    .tick {{ font: 400 11px ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; fill: {c["muted"]}; }}
  </style>
  <rect width="{W}" height="{H}" rx="12" fill="{c["bg"]}"/>
  <text x="40" y="34" class="k">codeforces</text>
  <text x="40" y="62" class="h">{esc(info["handle"])}</text>
  <text x="40" y="86" class="r">{rank} · {rating}<tspan class="k" dx="8">max {top}</tspan></text>
  <text x="40" y="128" class="n">{len(solved)}</text><text x="40" y="146" class="k">solved</text>
  <text x="150" y="128" class="n">{this_year}</text><text x="150" y="146" class="k">in {year}</text>
  <text x="260" y="128" class="n">{len(history)}</text><text x="260" y="146" class="k">contests</text>
  {"".join(bars)}
  {chart}
  <text x="{cx0}" y="232" class="tick">{since}</text>
  <text x="{cx1}" y="232" text-anchor="end" class="tick">rating per contest</text>
</svg>
'''


def main():
    info = api(f"user.info?handles={HANDLE}")[0]
    history = api(f"user.rating?handle={HANDLE}")
    solved = {}
    for s in api(f"user.status?handle={HANDLE}"):
        if s.get("verdict") == "OK":
            p = s["problem"]
            solved.setdefault((p.get("contestId"), p["index"]), (s["creationTimeSeconds"], p.get("rating")))
    for name, theme in THEMES.items():
        with open(f"{OUT}/codeforces-{name}.svg", "w", encoding="utf-8") as f:
            f.write(render(theme, info, history, solved))


if __name__ == "__main__":
    main()
