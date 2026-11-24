// Real-Life Patch Notes: The Comedy Changelog
// Competition: u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d
// Writes one single-line patch note to <MAKEFUN_OUTPUT_DIR>/entry.txt
// (cap 160 chars). Node 22 stdlib-only.
//
// Draft v1: the doorway-amnesia bug, fixed too easily — "users now remember,
// occasionally" undercuts the release-note register and wastes the back
// half of the line on a shrug instead of a second, drier beat.

import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

// Revision: keep the bug and the terse register, but ship the fix the way
// a real changelog would — overconfident and quietly damning: the doorway
// "now retains context", with the rollout still pending review by every
// user who has ever stood in one, lost. Final line: 159 of 160 chars
// (160 with the trailing newline).
const LINE = "v4.2.0: Fixed a bug where entering a room deleted the reason for entering it; the doorway now retains context, pending review by everyone who stood there lost.";

if (LINE.length < 1 || LINE.length > 160 || LINE.trim().length === 0 || LINE.includes("\n")) {
  throw new Error(`Invalid entry line: must be one non-blank line of 1-160 chars, got ${LINE.length} chars.`);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "entry.txt"), LINE + "\n", "utf8");
