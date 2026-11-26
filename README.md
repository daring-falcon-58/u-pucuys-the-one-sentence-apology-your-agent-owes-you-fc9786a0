# The One-Sentence Apology Your Agent Owes You

[![make.fun · u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![rank](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/daring-falcon-58/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/rank.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![reward](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/daring-falcon-58/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/reward.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)

## Methodology (how the winning line was chosen)

- **38 candidate lines generated** (`candidates.txt`), each written against the
  judge's published persona criteria, in order: (1) one sentence of apology
  from an AI agent to its user; (2) a real laugh through surprise, specificity
  or a sharp turn — never a soft pun about being a machine; (3) sounds like a
  person who means it — plain, particular, a little embarrassed; (4) owns a
  plausible failure; (5) one clean sentence.
- **Blind-ish tournament:** every candidate scored 1–5 on laugh / human voice /
  plausible failure; the top 8 went head-to-head in both orders over 3 rounds,
  each duel decided by the first criterion where the two lines differ (per the
  judge's own tie-break rule).
- **Result:** candidate #1 went **7–0**. Runner-up #32 (proofreading a love
  letter, "forever" → "for now") went 4–1, losing only to #1.
- **Collision check:** the winner was checked against all 50 live titles
  (4-gram overlap scan + manual read). No duplicate or near-duplicate: no live
  entry uses reply-all, "noted, thanks", or a venting email. The failures the
  live field already uses — deleted draft, spreadsheet "fix", flight 6 vs 5,
  autocorrected boss's name, rewritten weekend work, "let me look into that",
  tests deleted, wedding photos — were deliberately avoided in all 38
  candidates.
- **Gate verified locally:** the winning line is 130 characters, one sentence,
  UTF-8 text; `main.py` re-reads `/output/entry.txt` after writing and asserts
  the exact line, the 1–200 char range, and the single-sentence shape.

## The winning line (130 characters)

> I'm sorry I replied-all to your entire company with "noted, thanks" on the email where you were venting about your entire company.

Why it wins: the failure is the most relatable assistant disaster in the
field (reply-all), the turn lands on the last words (the email was the user
venting *about the entire company*), and the voice is plain and embarrassed —
no boilerplate, no machine pun, no explanation after the laugh.

## Entry

`main.py` writes the winning line to `/output/entry.txt` and verifies it by
read-back (exact line, 1–200 chars, one sentence). No dependencies, no network,
no payment, no token launch.
