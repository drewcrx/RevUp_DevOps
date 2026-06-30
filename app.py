from flask import Flask, jsonify

app = Flask(__name__)

PROJECT_INFO = {
    "project": "RevUp",
    "owner": "Andrew Carrera",
    "institution": "Instituto Superior Tecnológico de Turismo y Patrimonio Yavirac",
    "program": "Desarrollo de Software",
    "purpose": "Sistema web y móvil para la gestión digital de vehículos, órdenes de trabajo e historial de mantenimiento en talleres mecánicos mediante códigos QR.",
    "status": "DevOps practice deployment with Flask, Docker, GHCR and Traefik",
}


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RevUp | Gestión Inteligente para Talleres</title>
        <style>
            :root {
                --azul: #1b4585;
                --azul-oscuro: #071426;
                --azul-profundo: #0b1f3a;
                --celeste: #4db7ff;
                --naranja: #ff8a1f;
                --gris: #d9e4f2;
                --blanco: #ffffff;
                --texto: #eaf3ff;
                --muted: #a8bdd6;
                --card: rgba(255, 255, 255, 0.08);
                --borde: rgba(255, 255, 255, 0.16);
            }

            * {
                box-sizing: border-box;
                scroll-behavior: smooth;
            }

            body {
                margin: 0;
                min-height: 100vh;
                font-family: "Segoe UI", Arial, sans-serif;
                color: var(--texto);
                background:
                    radial-gradient(circle at 12% 18%, rgba(77, 183, 255, 0.30) 0, transparent 26%),
                    radial-gradient(circle at 80% 8%, rgba(255, 138, 31, 0.22) 0, transparent 26%),
                    linear-gradient(135deg, var(--azul-oscuro), var(--azul-profundo) 48%, #050a13);
                overflow-x: hidden;
            }

            a {
                color: inherit;
            }

            header {
                width: min(1180px, 92%);
                margin: 0 auto;
                padding: 28px 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 20px;
            }

            .logo {
                display: flex;
                align-items: center;
                gap: 12px;
                font-size: 28px;
                font-weight: 900;
                letter-spacing: 0.5px;
            }

            .logo-mark {
                width: 48px;
                height: 48px;
                border-radius: 16px;
                display: grid;
                place-items: center;
                background: linear-gradient(135deg, var(--azul), var(--celeste));
                box-shadow: 0 18px 40px rgba(77, 183, 255, 0.24);
            }

            nav {
                display: flex;
                gap: 12px;
                flex-wrap: wrap;
                justify-content: center;
            }

            nav a {
                text-decoration: none;
                color: var(--gris);
                font-weight: 700;
                padding: 10px 14px;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.10);
            }

            .hero {
                width: min(1180px, 92%);
                margin: 38px auto 24px;
                display: grid;
                grid-template-columns: 1.08fr 0.92fr;
                gap: 32px;
                align-items: center;
            }

            .panel {
                background: var(--card);
                border: 1px solid var(--borde);
                border-radius: 32px;
                padding: 42px;
                box-shadow: 0 30px 80px rgba(0, 0, 0, 0.32);
                backdrop-filter: blur(18px);
            }

            .tag {
                width: fit-content;
                display: inline-flex;
                gap: 8px;
                align-items: center;
                color: #071426;
                background: linear-gradient(135deg, var(--celeste), #b8e7ff);
                border-radius: 999px;
                padding: 10px 16px;
                font-weight: 900;
                margin-bottom: 22px;
            }

            h1 {
                font-size: clamp(42px, 6vw, 76px);
                line-height: 0.95;
                margin: 0 0 22px;
                letter-spacing: -2px;
            }

            h1 span {
                color: var(--celeste);
            }

            .subtitle {
                font-size: 20px;
                line-height: 1.65;
                color: var(--gris);
                margin: 0 0 30px;
            }

            .buttons {
                display: flex;
                gap: 14px;
                flex-wrap: wrap;
            }

            .btn {
                display: inline-block;
                text-decoration: none;
                color: #061121;
                background: linear-gradient(135deg, var(--naranja), #ffd08a);
                border-radius: 16px;
                padding: 14px 20px;
                font-weight: 900;
                box-shadow: 0 16px 34px rgba(255, 138, 31, 0.26);
            }

            .btn.secondary {
                color: var(--texto);
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid var(--borde);
                box-shadow: none;
            }

            .dashboard {
                display: grid;
                gap: 16px;
            }

            .mock-card {
                background: rgba(255, 255, 255, 0.10);
                border: 1px solid var(--borde);
                border-radius: 24px;
                padding: 22px;
            }

            .mock-card h3 {
                margin: 0 0 8px;
                color: var(--blanco);
                font-size: 22px;
            }

            .mock-card p {
                margin: 0;
                color: var(--muted);
                line-height: 1.55;
            }

            .qr-box {
                display: grid;
                grid-template-columns: 92px 1fr;
                gap: 18px;
                align-items: center;
            }

            .qr {
                width: 92px;
                height: 92px;
                border-radius: 18px;
                background:
                    linear-gradient(90deg, #fff 10px, transparent 10px) 0 0 / 24px 24px,
                    linear-gradient(#fff 10px, transparent 10px) 0 0 / 24px 24px,
                    var(--azul);
                border: 8px solid white;
                box-shadow: 0 18px 35px rgba(0, 0, 0, 0.28);
            }

            .status {
                display: flex;
                gap: 10px;
                flex-wrap: wrap;
                margin-top: 14px;
            }

            .status span {
                background: rgba(77, 183, 255, 0.12);
                border: 1px solid rgba(77, 183, 255, 0.24);
                color: #cdeeff;
                border-radius: 999px;
                padding: 8px 12px;
                font-size: 14px;
                font-weight: 800;
            }

            .section {
                width: min(1180px, 92%);
                margin: 24px auto;
            }

            .section-title {
                margin-bottom: 18px;
            }

            .section-title h2 {
                margin: 0 0 8px;
                font-size: clamp(30px, 4vw, 44px);
            }

            .section-title p {
                margin: 0;
                color: var(--muted);
                line-height: 1.6;
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
            }

            .feature {
                background: var(--card);
                border: 1px solid var(--borde);
                border-radius: 26px;
                padding: 24px;
                min-height: 178px;
            }

            .icon {
                font-size: 38px;
                margin-bottom: 12px;
            }

            .feature h3 {
                margin: 0 0 10px;
                color: var(--blanco);
                font-size: 21px;
            }

            .feature p {
                margin: 0;
                color: var(--muted);
                line-height: 1.58;
            }

            .split {
                display: grid;
                grid-template-columns: 0.95fr 1.05fr;
                gap: 18px;
                align-items: stretch;
            }

            .list {
                display: grid;
                gap: 12px;
                margin-top: 18px;
            }

            .list div {
                display: flex;
                gap: 12px;
                align-items: flex-start;
                background: rgba(255, 255, 255, 0.07);
                border: 1px solid rgba(255, 255, 255, 0.10);
                border-radius: 18px;
                padding: 14px;
                color: var(--gris);
            }

            .stack {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 18px;
            }

            .stack span {
                border-radius: 999px;
                border: 1px solid rgba(255, 255, 255, 0.15);
                background: rgba(255, 255, 255, 0.08);
                padding: 10px 14px;
                font-weight: 800;
                color: var(--gris);
            }

            .owner {
                border-left: 5px solid var(--naranja);
            }

            footer {
                width: min(1180px, 92%);
                margin: 34px auto 0;
                padding: 28px 0 36px;
                color: var(--muted);
                text-align: center;
                font-weight: 700;
            }

            @media (max-width: 900px) {
                header,
                .hero,
                .split {
                    grid-template-columns: 1fr;
                }

                header {
                    flex-direction: column;
                    text-align: center;
                }

                .grid {
                    grid-template-columns: 1fr;
                }

                .panel {
                    padding: 28px;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <div class="logo">
                <div class="logo-mark">⚙️</div>
                <div>RevUp</div>
            </div>
            <nav>
                <a href="#funciones">Funciones</a>
                <a href="#proposito">Propósito</a>
                <a href="#devops">DevOps</a>
                <a href="#autor">Autor</a>
            </nav>
        </header>

        <main class="hero">
            <section class="panel">
                <div class="tag">🚗 Proyecto de gestión automotriz</div>
                <h1>Digitaliza el historial de cada <span>vehículo</span>.</h1>
                <p class="subtitle">
                    RevUp es una propuesta para talleres mecánicos que permite registrar vehículos,
                    órdenes de trabajo, mantenimientos y kilometraje. Cada vehículo puede consultarse
                    mediante un código QR para acceder rápido a su historial dentro del taller.
                </p>
                <div class="buttons">
                    <a class="btn" href="#funciones">Ver funcionalidades</a>
                    <a class="btn secondary" href="/health">Probar healthcheck</a>
                </div>
            </section>

            <section class="dashboard" aria-label="Vista demostrativa de RevUp">
                <article class="mock-card qr-box">
                    <div class="qr" aria-hidden="true"></div>
                    <div>
                        <h3>QR del vehículo</h3>
                        <p>Escaneo rápido para consultar placa, cliente, kilometraje, último trabajo y mantenimientos.</p>
                        <div class="status">
                            <span>Placa: PBD-4321</span>
                            <span>Estado: En taller</span>
                        </div>
                    </div>
                </article>
                <article class="mock-card">
                    <h3>Orden de trabajo activa</h3>
                    <p>Cambio de aceite, revisión de frenos y actualización de kilometraje asignada a un mecánico.</p>
                    <div class="status">
                        <span>Prioridad media</span>
                        <span>Mecánico asignado</span>
                    </div>
                </article>
                <article class="mock-card">
                    <h3>Historial centralizado</h3>
                    <p>La información deja de depender de hojas físicas y se organiza en un flujo digital más seguro.</p>
                </article>
            </section>
        </main>

        <section class="section" id="funciones">
            <div class="section-title">
                <h2>Funciones principales</h2>
                <p>El enfoque de la página cambió de una tienda artesanal a una solución tecnológica para talleres.</p>
            </div>
            <div class="grid">
                <article class="feature">
                    <div class="icon">🧾</div>
                    <h3>Órdenes de trabajo</h3>
                    <p>Registro, asignación y seguimiento de trabajos realizados dentro del taller mecánico.</p>
                </article>
                <article class="feature">
                    <div class="icon">🔧</div>
                    <h3>Mantenimientos</h3>
                    <p>Control de servicios, repuestos, fechas y observaciones para cada vehículo atendido.</p>
                </article>
                <article class="feature">
                    <div class="icon">📲</div>
                    <h3>Consulta por QR</h3>
                    <p>Acceso rápido al historial del vehículo escaneando un código único desde el taller.</p>
                </article>
                <article class="feature">
                    <div class="icon">📈</div>
                    <h3>Reportes</h3>
                    <p>Visualización de trabajos, mantenimientos y actividad operativa para apoyar decisiones.</p>
                </article>
                <article class="feature">
                    <div class="icon">🛞</div>
                    <h3>Vehículos y clientes</h3>
                    <p>Administración interna de datos del cliente, vehículo, placa y kilometraje actualizado.</p>
                </article>
                <article class="feature">
                    <div class="icon">🔐</div>
                    <h3>Roles del taller</h3>
                    <p>Flujo pensado para administrador y mecánico, manteniendo el alcance real del proyecto.</p>
                </article>
            </div>
        </section>

        <section class="section split" id="proposito">
            <article class="panel owner">
                <div class="section-title">
                    <h2>Propósito</h2>
                    <p>
                        RevUp busca reducir la pérdida de información, agilizar la consulta de mantenimientos
                        y reemplazar procesos manuales por una experiencia digital clara para el taller.
                    </p>
                </div>
                <div class="list">
                    <div>✅ Registrar información importante del vehículo en un solo lugar.</div>
                    <div>✅ Consultar el último mantenimiento sin buscar hojas físicas.</div>
                    <div>✅ Actualizar kilometraje y estado de la orden de trabajo.</div>
                    <div>✅ Mejorar la organización del taller con una solución escalable.</div>
                </div>
            </article>

            <article class="panel" id="devops">
                <div class="section-title">
                    <h2>Enfoque DevOps</h2>
                    <p>
                        Esta versión conserva la práctica de despliegue: aplicación Flask empaquetada en Docker,
                        publicación de imagen en GHCR y despliegue en VPS usando Docker Stack y Traefik.
                    </p>
                </div>
                <div class="stack">
                    <span>Flask</span>
                    <span>Docker</span>
                    <span>Docker Compose</span>
                    <span>GitHub Actions</span>
                    <span>GHCR</span>
                    <span>Traefik</span>
                    <span>VPS</span>
                </div>
            </article>
        </section>

        <section class="section" id="autor">
            <article class="panel">
                <div class="section-title">
                    <h2>Datos del proyecto</h2>
                    <p>
                        Desarrollado por <strong>Andrew Carrera</strong>, estudiante de Desarrollo de Software
                        del Instituto Superior Tecnológico de Turismo y Patrimonio Yavirac. Este despliegue sirve
                        como adaptación DevOps del proyecto RevUp.
                    </p>
                </div>
                <div class="stack">
                    <span>Autor: Andrew Carrera</span>
                    <span>Proyecto: RevUp</span>
                    <span>Carrera: Desarrollo de Software</span>
                    <span>Institución: Yavirac</span>
                </div>
            </article>
        </section>

        <footer>
            © 2026 RevUp · Página de práctica DevOps para gestión de talleres mecánicos
        </footer>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({"status": "ok", "project": "revup", "owner": "Andrew Carrera"})


@app.route("/api/resumen")
def resumen():
    return jsonify(PROJECT_INFO)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
