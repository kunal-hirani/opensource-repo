# Security Policy

## Supported versions

weatherkit follows Semantic Versioning; only the latest release receives
security fixes.

| Version | Supported |
|---|---|
| 0.2.x | Yes |
| < 0.2 | No |

## Reporting a vulnerability

**Please do not report security issues in public issues or pull requests.**

Use GitHub's "Report a vulnerability" button under the repository's
**Security** tab, which opens a private security advisory. Include:

- A description of the issue and how to reproduce it
- The version of weatherkit affected
- Any proof-of-concept code (kept confidential)

You can expect an initial response within 7 days. We will keep you informed of
progress toward a fix and coordinate a disclosure date together.

## Scope

weatherkit is a pure-Python library with no network, filesystem, or process
side effects, so realistic vulnerabilities are limited to things like
unexpected exceptions on crafted input. Reports in that spirit (for example,
input that escapes documented validation) are still welcome.
