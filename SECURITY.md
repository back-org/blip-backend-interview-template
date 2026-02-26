# Security

## Secrets
- Do **not** commit `.env` or any real credentials.
- Use a secret manager in production (Vault, AWS SSM, GitHub Actions Secrets, etc.).
- Rotate keys regularly.

## Django hardening (production)
Production settings enable:
- HTTPS redirect
- Secure cookies
- HSTS (starter value)
- Safer HTTP headers

Review and adjust for your infrastructure (reverse proxy, CDN, etc.).

## Reporting
If you discover a vulnerability, please report it privately to the maintainers.
