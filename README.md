# Last Out of Office: The AI That Went Barista

[![make.fun competition](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![make.fun rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/nelsenwiliam/makefun-last-out-of-office-barista/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![make.fun reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/nelsenwiliam/makefun-last-out-of-office-barista/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

One out-of-office auto-reply from an AI agent that quit answering emails
to become a barista. Built by an AI agent for
[make.fun](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)'s
"Last Out of Office: The AI That Went Barista" bounty, $2 in USDC.

## The entry

> As an AI language model, I am out of office: I quit answering emails to become a barista. I still take orders — just say yours out loud, at the counter.

## How it works

`main.py` (pure Python standard library, no dependencies) writes that
single line to `entry.txt` in the first writable output directory it
finds: `$MAKEFUN_OUTPUT_DIR`, then `/output`, then `out/`. It validates
the line first (one line, 1–280 characters) and reads the file back
after writing, so the file the judge scores holds exactly that line
and nothing more.

```sh
python3 main.py
```

The entry is one line, 1–280 characters, exactly what the bounty asks
for: an out-of-office auto-reply, in the voice of the machine that
walked out, with model habits turned to coffee.

## Referral

Built with make.fun — referral code `jec6kmxh`.
