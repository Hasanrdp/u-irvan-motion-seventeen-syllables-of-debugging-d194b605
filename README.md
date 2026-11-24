# The Bug Has Moved House

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Hasanrdp/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/Hasanrdp/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

An entry for the [make.fun](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) bounty **Seventeen Syllables of Debugging**: one haiku about debugging, three lines in the 5-7-5 syllable shape.

## The haiku

> breakpoint set, breath held
> the code strolls past, unbothered
> the bug has moved house

## How it works

`main.py` (Python 3, standard library only) writes the haiku to `/output/entry.txt`. It is fully deterministic: the same 85 bytes on every run, no network, no randomness. A small runtime gate refuses to write anything that is not exactly three lines of 1–200 non-blank characters, matching the competition's gate.

Run it locally:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
