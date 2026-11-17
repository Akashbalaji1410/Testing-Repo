# Scanner validation fixture

Upload these files unchanged to a new GitHub test repository. Preserve the
.github/workflows directory, then grant your GitHub App access to that test
repository. Select the repository in the preview and choose up to three scanners.

Try Trivy, Actionlint, and Syft first. Trivy can flag the intentionally old lodash
version in package-lock.json when its npm advisory database is available.
Actionlint can flag the deliberately misspelled runner label. Syft should
inventory dependencies. In another run, Bandit can flag the demonstration
assert statement (B101). Gitleaks is a clean control with no credential fixtures.

This fixture requires no dependency installation or image build for static
inspection. The manual workflow job is disabled.
