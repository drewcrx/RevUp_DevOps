# RevUp - DevOps

Página web en Flask adaptada al proyecto **RevUp**, una propuesta para digitalizar la gestión de vehículos, órdenes de trabajo e historial de mantenimiento en talleres mecánicos mediante códigos QR.

Este proyecto conserva el enfoque DevOps del ejercicio original: aplicación Flask, Docker, GitHub Actions, GitHub Container Registry, Docker Stack, VPS y Traefik.

## Datos del proyecto

- **Nombre:** RevUp
- **Autor:** Andrew Carrera
- **Carrera:** Desarrollo de Software
- **Institución:** Instituto Superior Tecnológico de Turismo y Patrimonio Yavirac
- **Propósito:** gestionar vehículos, mantenimientos, órdenes de trabajo, kilometraje e historial consultable por QR.
- **Repositorio sugerido:** `revup-devops`
- **Package / imagen GHCR:** `revup-web`
- **Imagen completa:** `ghcr.io/drewcrx/revup-web:1.0.0`
- **Subdominio configurado en Traefik:** `revup.byronrm.com`
- **Stack:** `revup`
- **Servicio:** `revup-web`

> Nota: si tu usuario de GitHub o subdominio es diferente, cambia `drewcrx` y `revup.byronrm.com` en `.github/workflows/docker.yml`, `stack.yml` y este README.

## Rutas disponibles

```txt
/              Página principal de RevUp
/health        Healthcheck en formato JSON
/api/resumen   Resumen del proyecto en formato JSON
```

## Ejecutar localmente con Docker Compose

```bash
docker compose up -d --build
```

Abrir:

```txt
http://localhost:5000
```

## Detener localmente

```bash
docker compose down
```

## Ejecutar sin Docker

```bash
pip install -r requirements.txt
python app.py
```

Luego abrir:

```txt
http://localhost:5000
```

## Subir a GitHub

```bash
git init
git add .
git commit -m "Proyecto DevOps RevUp"
git branch -M main
git remote add origin https://github.com/drewcrx/revup-devops.git
git push -u origin main
```

## Secrets necesarios en GitHub Actions

En el repositorio, ir a **Settings > Secrets and variables > Actions** y agregar:

```txt
GHCR_TOKEN
VPS_HOST
VPS_USER
VPS_PASSWORD
VPS_PORT
```

### Sobre GHCR

El workflow usa `GITHUB_TOKEN` para publicar la imagen en GitHub Container Registry.

El secret `GHCR_TOKEN` se usa en el VPS para iniciar sesión en GHCR antes de descargar la imagen. Si el package está público, podrías omitir el login del VPS, pero se mantiene para un flujo más completo.

## Comandos útiles en el VPS

```bash
docker service ls
docker service logs revup_revup-web -f
docker pull ghcr.io/drewcrx/revup-web:1.0.0
```

## Despliegue con Docker Stack

```bash
make deploy
make ps
make logs
```

## Cambios realizados respecto al proyecto original

- Se cambió el propósito de la web a una solución para talleres mecánicos.
- Se reemplazó la identidad visual pastel por una estética tecnológica azul/naranja relacionada con RevUp.
- Se adaptaron textos, secciones, servicios, stack, workflow y README.
- Se agregaron rutas `/health` y `/api/resumen` para validación básica.
