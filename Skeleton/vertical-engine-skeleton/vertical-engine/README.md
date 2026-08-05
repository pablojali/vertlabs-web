# vertical-engine (repo PRIVADO)

Esqueleto funcional del Engine + Builder de Vertical Trail Labs.
Corré `python publish.py` y genera el sitio completo en `output/`.

## Estructura

```
vertical-engine/
  engine/metrics/       -> vpi.py, dmi.py, er.py (stubs, portar desde el Streamlit)
  builder/templates/     -> Jinja2: base.html, race.html, athlete.html, index.html
  builder/generators/    -> un módulo por tipo de página, cada uno lee su JSON
  data/races/, data/athletes/  -> JSON de ejemplo (esto lo va a producir el Engine)
  assets/                -> CSS/JS que se copian tal cual a output/assets/
  output/                -> sitio generado (gitignored, no se commitea acá)
  publish.py             -> orquestador de un solo comando
  .github/workflows/publish.yml -> automatiza build + push al repo público
```

## Cómo probarlo ahora

```bash
pip install -r requirements.txt
python publish.py
# abrí output/index.html en el navegador
```

## Próximos pasos de código (en orden)

1. Portar `calculate_vpi/dmi/er` desde el Streamlit `app.py` a `engine/metrics/`.
2. Escribir un script en `engine/` que tome un GPX + checkpoints y emita
   `data/races/<slug>.json` y `data/athletes/<slug>.json` (reemplaza los
   JSON de ejemplo que hoy edito a mano).
3. Generar los charts (Plotly + kaleido) como PNG dentro de
   `assets/images/races/<slug>/` y `assets/images/athletes/<slug>/`.
4. Agregar `rankings_generator.py` (VPI/DMI/ER top N) siguiendo el mismo
   patrón que `race_generator.py`.

---

# Configuración de infraestructura (hacer una sola vez)

## 1. Crear los dos repos en GitHub

- `vertical-engine` → **privado**. Este código.
- `vertlabs-site` → **público**. Solo va a contener lo que salga de `output/`.
  Podés arrancar el repo vacío, con un solo `index.html` placeholder.

## 2. Conectar Cloudflare Pages al repo público

1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** →
   **Connect to Git** → elegís `vertlabs-site`.
2. Build settings:
   - Framework preset: **None**
   - Build command: *(vacío, no hay build — ya es HTML estático)*
   - Build output directory: `/`
3. Deploy. Cloudflare te da un subdominio `*.pages.dev` para probar antes
   de conectar el dominio real.

## 3. Conectar el dominio vertlabs.run

1. En el proyecto de Pages → **Custom domains** → **Set up a custom domain**
   → escribís `vertlabs.run`.
2. Como el dominio ya está en tu cuenta de Cloudflare (DNS-only), Cloudflare
   agrega el registro CNAME automáticamente y emite el certificado SSL.
   No hay que tocar nada en Namecheap.
3. Esperá la propagación (minutos, no horas) y listo.

## 4. Automatizar el publish con GitHub Actions

1. Generá un **deploy key** con permiso de escritura para `vertlabs-site`:
   ```bash
   ssh-keygen -t ed25519 -f vertlabs_deploy_key -N ""
   ```
2. En `vertlabs-site` → Settings → Deploy keys → agregás la pública
   (`vertlabs_deploy_key.pub`) con **Allow write access**.
3. En `vertical-engine` → Settings → Secrets and variables → Actions →
   agregás la privada (`vertlabs_deploy_key`) como secret
   `VERTLABS_SITE_DEPLOY_KEY`.
4. Editás `.github/workflows/publish.yml`: reemplazá `TU_USUARIO` por tu
   usuario/organización real de GitHub.
5. Cada push a `main` en `vertical-engine` (o disparo manual desde la
   pestaña Actions) corre `publish.py` y pushea `output/` al repo público.
   Cloudflare Pages detecta el push en `vertlabs-site` y despliega solo.

## 5. Resultado del flujo completo

```
vos editás data/ o el Engine
        ↓
   git push (vertical-engine)
        ↓
  GitHub Actions: publish.py
        ↓
  push a vertlabs-site
        ↓
  Cloudflare Pages detecta el push
        ↓
  sitio en vivo en vertlabs.run
```

Sin builds manuales, sin subir nada a mano por FTP, sin depender de
acordarte de correr un script desde tu máquina.
