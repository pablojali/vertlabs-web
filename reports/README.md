# reports/

Static hosting for Athlete Performance Report PDFs. Drop a PDF in this
folder, commit and push - Cloudflare Pages serves it directly at

    https://vertlabs.run/reports/<same-filename>.pdf

No build step, no code, no page for this: Cloudflare Pages serves this
whole repo as-is (build command empty, output directory `/`), so any
file placed here becomes reachable by its exact filename as soon as the
push deploys. There's no index or listing - if you need to point
someone to a report, share that URL directly (e.g. in an email, a
social post, or a link on an athlete's own page).

Naming convention: `<athlete-slug>-<race-slug>-<year>.pdf`, e.g.
`yngvild-kaspersen-ccc-2026.pdf`. Not enforced by anything - it just
keeps filenames predictable and collision-free across athletes/races.

This folder is exempt from the Engine's "Exportar a Web" publish step
(`PUBLISH_KEEP_ENTRIES` in Vert_engine's `app.py`) - it won't be wiped
or touched when the site's generated content is republished.
