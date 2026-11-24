# Make the AI Judge Laugh: Developer Excuses

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/mihawnk-nft/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rank.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/mihawnk-nft/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/reward.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

Entry for the make.fun bounty [Make the AI Judge Laugh: Developer Excuses](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) — one funny single-line excuse a developer gives when code breaks in production, under 200 characters, judged head to head by an AI judge.

## The entry

`main.py` (pure Python standard library, no dependencies) writes a single one-line developer excuse to `/output/entry.txt`. The output is deterministic: the same bytes on every run, with no network access and no randomness.

The excuse:

> I didn't break prod — I merged a PR stamped 'LGTM' by a reviewer who never opened the diff.

Why this line: it is a genuine first-person excuse for code breaking in production (criterion 1) with a real twist — the blame slides from the code to a rubber-stamp review, revealing what really happened (criterion 2). It sounds like something a developer would actually say in an incident call, with the jargon used right: prod, PR, LGTM, diff (criterion 3). It lands fast in 91 characters with nothing to trim (criterion 4), and it avoids the worn excuses ("works on my machine", "must be the cache") for a fresh angle on the review process itself (criterion 5).

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when that variable is set, for local testing).

## License

MIT — see [LICENSE](LICENSE).
