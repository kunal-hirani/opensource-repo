# Negative test: deliberately broken link

This file exists for **Test 11** (negative test) only. Do not merge a branch
containing it.

The link below points at a domain that can never resolve, so the lychee step
in the `docs / checks` job must fail and the pull request must be blocked
once branch protection requires status checks.

See: [the thing](https://example.invalid/nope)

After capturing the red check and the blocked merge button, delete this
branch. Nothing in `main` may ever contain this file.
