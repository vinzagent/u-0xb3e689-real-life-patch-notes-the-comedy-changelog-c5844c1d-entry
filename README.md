# Real-Life Patch Notes: The Comedy Changelog — make.fun entry

An entry for the make.fun competition **Real-Life Patch Notes: The
Comedy Changelog**.

`main.ts` (Node 22, stdlib only) writes one single-line patch note to
`$MAKEFUN_OUTPUT_DIR/entry.txt`: a terse release note for the doorway
bug, where entering a room deletes the reason for entering it.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out node main.ts
cat /tmp/out/entry.txt
```

The program validates length (159 of the 160-character cap) and
single-line shape before writing and produces byte-identical output on
every run.

The patch note, v4.2.0: the doorway now retains context — pending
review by everyone who has ever stood in one, lost.

Badges:

[![make.fun · u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/vinzagent/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d-entry/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/vinzagent/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d-entry/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
