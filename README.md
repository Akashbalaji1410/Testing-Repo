# Scanner validation fixture

Extract this archive into the existing test repository and commit the files at
the repository root. Preserve .github/workflows/fixture.yml. The fixture is
intended for static inspection and does not require npm install, a Docker
build, or running the GitHub Actions workflow.

| Tool | Input | Expected evidence |
| --- | --- | --- |
| Gitleaks | fixture.py | Generic API key rule may flag the random synthetic string. |
| Trivy | package-lock.json | An advisory for lodash 4.17.20 with an available npm vulnerability database. |
| Bandit | fixture.py | B101 for assert. The weak hash may also be flagged. |
| Grype | package-lock.json | An advisory for lodash 4.17.20 with an available vulnerability database. |
| Hadolint | Dockerfile | DL3007 for the latest base-image tag. |
| Actionlint | .github/workflows/fixture.yml | A diagnostic for the misspelled hosted-runner label. The workflow job is disabled. |
| Syft | package-lock.json | Inventory evidence for lodash 4.17.20. |
| SonarQube Cloud | fixture.py | Python S4790 Security Hotspot for weak hashing if the scanner analyzes this file and the rule is active. |

In the Vercel preview, select this repository and choose Select all available.
Check each scanner's completion status before interpreting the results.

For SonarQube Cloud, analyze this repository's default branch in its own Sonar
project. Set SONAR_CLOUD_REPOSITORY and SONAR_CLOUD_PROJECT_KEY in Vercel
Preview to identify this repository and its own project. Keep the token in
Vercel. Read quality gate shows the recorded gate status. Look under Security
Hotspots in SonarQube Cloud for the weak-hash example. Gate status depends on
the project's quality gate, security profile, and new-code settings.
