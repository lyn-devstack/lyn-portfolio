"""Genera el CV en HTML (es/en) para imprimirlo a PDF con Edge/Chrome.

Uso:
  python scripts/make_cv.py <carpeta_salida>                       -> versión pública (sin email ni teléfono)
  python scripts/make_cv.py <carpeta_salida> --email X --phone Y   -> versión para postular (no subir al repo)
"""
import argparse, html, os

ap = argparse.ArgumentParser()
ap.add_argument('out')
ap.add_argument('--email')
ap.add_argument('--phone')
args = ap.parse_args()
out = args.out
private = bool(args.email or args.phone)
L = {
'es': dict(
 role='Desarrolladora web full-stack | Vue.js · TypeScript · PHP · .NET',
 loc='España · Remoto', auth='Permiso de trabajo: España y EE. UU.',
 h_profile='Perfil profesional', h_exp='Experiencia profesional', h_proj='Proyectos', h_edu='Formación', h_skills='Habilidades técnicas', h_more='Idiomas y certificaciones',
 profile='Desarrolladora web full-stack con doble titulación (DAW y DAM) y experiencia en el ciclo de vida completo de aplicaciones web. Frontend moderno con Vue.js y TypeScript, y backend con PHP y .NET. Perfil proactivo y resolutivo, con capacidad para optimizar código, resolver problemas técnicos complejos y trabajar con metodologías ágiles (Scrum, Kanban). Actualmente cursando el Grado en Ingeniería en Tecnologías de la Información (UNED).',
 jobs=[
  ('Web Developer', 'Avantio · Híbrido', 'Mar 2025 – Actualidad', 'Mantenimiento técnico, evolución y despliegue del software de gestión de reservas y de los sitios web de la compañía.', [
   ('Desarrollo a medida:', 'widgets y componentes interactivos desde cero con JavaScript moderno, SCSS y PHP para ampliar las funcionalidades del núcleo del producto.'),
   ('Arquitectura y lógica:', 'reestructuración de sitios web complejos y flujos de reserva con arquitectura basada en componentes y lógica de negocio dinámica (plantillas PHP).'),
   ('Integraciones:', 'implementación y configuración de brokers de ventas, pasarelas de pago y larga estancia en coordinación con el equipo de Sistemas.'),
   ('Tooling:', 'entornos de desarrollo local con Node.js y Gulp para garantizar la compatibilidad entre versiones del producto.'),
   ('Calidad de código:', 'flujo ágil con Jira, Pull Requests en GitHub y code reviews cruzadas.')]),
  ('Full Stack Developer (prácticas)', 'Kiteris Solutions · Remoto', 'Sep 2022 – Ene 2023', 'Plataforma de gestión de recursos empresariales con arquitectura de microservicios.', [
   ('Backend:', 'creación y mantenimiento de microservicios con .NET y C#.'),
   ('Migración frontend:', 'de interfaces tradicionales a una SPA modular con Vue.js, Pinia y TypeScript.'),
   ('Funcionalidades:', 'login y autenticación, filtros avanzados, consumo de APIs con Swagger y exportación de informes PDF.'),
   ('Impacto:', 'mejora estimada del 25% en la experiencia de usuario y del 15% en la legibilidad del código aplicando principios SOLID.')])],
 projects=[
  ('matchaTest', 'Vue 3 · TypeScript · IndexedDB', 'Simulador de exámenes tipo test local-first: motor de reglas de puntuación, lector de guías docentes en PDF y repaso con sistema Leitner.'),
  ('Booky Bloom', 'Kotlin · Firebase · MVVM', 'App Android de lectura con comunidad de reseñas y roles de administrador y cliente. Proyecto final de DAM.'),
  ('Infinite', 'PHP (MVC) · MySQL · AJAX', 'Gestión de citas, stock y usuarios para centros de estética, con disparadores para el control de inventario.')],
 edu=[
  ('Grado en Ingeniería en Tecnologías de la Información', 'UNED', '2026 – Actualidad'),
  ('CFGS Desarrollo de Aplicaciones Multiplataforma (DAM)', 'Ilerna · Nota media 9,14', '2024 – 2025'),
  ('CFGS Desarrollo de Aplicaciones Web (DAW)', 'Ilerna', '2020 – 2023'),
  ('Justicia Criminal (1 año cursado)', 'ASA College, Nueva York, EE. UU.', '2016 – 2017')],
 skills=[
  ('Frontend:', 'JavaScript, TypeScript, Vue.js, Pinia, HTML5, CSS3, SCSS, Tailwind CSS'),
  ('Backend:', 'PHP, C#, .NET Core, microservicios, APIs REST, Swagger'),
  ('Bases de datos:', 'SQL, MySQL, SQL Server, Firebase'),
  ('Herramientas:', 'Git, GitHub, Jira, Node.js, Gulp, WordPress'),
  ('Metodologías:', 'Scrum, Kanban, code review, principios SOLID')],
 more='Español (nativo) · Inglés (intermedio-avanzado) · Principios SOLID y Código Limpio (Udemy) · Ciberseguridad (Cisco)',
 contact='Contacto por LinkedIn'),
'en': dict(
 role='Full-Stack Web Developer | Vue.js · TypeScript · PHP · .NET',
 loc='Spain · Remote', auth='Work authorization: Spain (EU) and United States',
 h_profile='Professional Summary', h_exp='Professional Experience', h_proj='Projects', h_edu='Education', h_skills='Technical Skills', h_more='Languages & Certifications',
 profile="Full-stack web developer with two higher technical degrees (Web and Multiplatform Application Development) and experience across the full lifecycle of web applications. Modern frontend with Vue.js and TypeScript, backend with PHP and .NET. Proactive problem-solver focused on code quality, used to working in agile teams (Scrum, Kanban). Currently pursuing a Bachelor's degree in Information Technology Engineering (UNED).",
 jobs=[
  ('Web Developer', 'Avantio · Hybrid', 'Mar 2025 – Present', "Technical maintenance, evolution and deployment of the company's booking management software and websites.", [
   ('Custom development:', 'built interactive widgets and components from scratch with modern JavaScript, SCSS and PHP to extend the core product.'),
   ('Architecture & logic:', 'restructured complex websites and booking flows using a component-based architecture and dynamic business logic (PHP templates).'),
   ('Integrations:', 'implemented and configured sales, payment gateway and long-stay brokers in coordination with the Systems team.'),
   ('Tooling:', 'managed local development environments with Node.js and Gulp to keep compatibility across product versions.'),
   ('Code quality:', 'agile workflow with Jira, Pull Requests on GitHub and cross code reviews.')]),
  ('Full Stack Developer (Internship)', 'Kiteris Solutions · Remote', 'Sep 2022 – Jan 2023', "Enterprise resource management platform built on microservices.", [
   ('Backend:', 'built and maintained microservices with .NET and C#.'),
   ('Frontend migration:', 'moved legacy interfaces to a modular SPA with Vue.js, Pinia and TypeScript.'),
   ('Key features:', 'login/authentication, advanced data filters, Swagger-documented API integration and PDF report export.'),
   ('Impact:', 'estimated 25% improvement in user experience and 15% in code readability by applying SOLID principles.')])],
 projects=[
  ('matchaTest', 'Vue 3 · TypeScript · IndexedDB', 'Local-first multiple-choice exam simulator: configurable scoring engine, PDF syllabus parser and Leitner-based review deck.'),
  ('Booky Bloom', 'Kotlin · Firebase · MVVM', 'Android reading app with a review community and admin/client roles. Final project of the DAM degree.'),
  ('Infinite', 'PHP (MVC) · MySQL · AJAX', 'Appointment, stock and user management for beauty centers, with database triggers for inventory control.')],
 edu=[
  ("Bachelor's Degree in Information Technology Engineering", 'UNED', '2026 – Present'),
  ('Higher Technical Degree in Multiplatform App Development (DAM)', 'Ilerna · GPA 9.14/10', '2024 – 2025'),
  ('Higher Technical Degree in Web App Development (DAW)', 'Ilerna', '2020 – 2023'),
  ('Criminal Justice (1 year completed)', 'ASA College, New York, USA', '2016 – 2017')],
 skills=[
  ('Frontend:', 'JavaScript, TypeScript, Vue.js, Pinia, HTML5, CSS3, SCSS, Tailwind CSS'),
  ('Backend:', 'PHP, C#, .NET Core, microservices, REST APIs, Swagger'),
  ('Databases:', 'SQL, MySQL, SQL Server, Firebase'),
  ('Tools:', 'Git, GitHub, Jira, Node.js, Gulp, WordPress'),
  ('Methodologies:', 'Scrum, Kanban, code review, SOLID principles')],
 more='Spanish (native) · English (upper-intermediate) · SOLID Principles & Clean Code (Udemy) · Cybersecurity (Cisco)',
 contact='Contact via LinkedIn'),
}

CSS = '''
@page { size: A4; margin: 10mm 14mm; }
* { box-sizing: border-box; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 9.2pt; color: #222; margin: 0; line-height: 1.32; font-variant-ligatures: none; }
h1 { font-size: 22pt; margin: 0; color: #a08850; font-weight: 700; letter-spacing: .5px; }
.role { font-size: 11.5pt; color: #0b3560; font-weight: 600; margin: 2px 0 5px; }
.contact { font-size: 8.6pt; color: #555; }
.contact a { color: #0b3560; text-decoration: none; }
h2 { background: #0b3560; color: #d8c48f; font-size: 9.8pt; text-transform: uppercase; letter-spacing: .5px; padding: 4px 9px; margin: 8px 0 5px; }
p { margin: 2px 0 3px; }
.row { display: flex; justify-content: space-between; gap: 10px; }
.date { color: #a08850; font-weight: 700; white-space: nowrap; }
.sub { font-style: italic; color: #555; }
ul { margin: 2px 0 0; padding-left: 16px; }
li { margin-bottom: 1.5px; }
.item { margin-bottom: 5px; }
.tech { color: #0b3560; font-size: 8.4pt; }
'''

e = html.escape
for lang, d in L.items():
    jobs = ''.join(
        f'<div class="item"><div class="row"><b>{e(r)}</b><span class="date">{e(p)}</span></div>'
        f'<div class="sub">{e(c)}</div><p>{e(s)}</p><ul>'
        + ''.join(f'<li><b>{e(a)}</b> {e(b)}</li>' for a, b in bl) + '</ul></div>'
        for r, c, p, s, bl in d['jobs'])
    projects = ''.join(f'<li><b>{e(n)}</b> <span class="tech">{e(t)}</span> — {e(x)}</li>' for n, t, x in d['projects'])
    skills = ''.join(f'<p><b>{e(a)}</b> {e(b)}</p>' for a, b in d['skills'])
    contact_line = ' &nbsp;|&nbsp; '.join(e(x) for x in [args.email, args.phone] if x)
    if contact_line:
        contact_line += ' &nbsp;|&nbsp; '
    edu = ''.join(f'<div class="row"><span><b>{e(t)}</b>, {e(w)}</span><span class="date">{e(y)}</span></div>' for t, w, y in d['edu'])
    doc = f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>CV Leslie Carolyn</title>
<style>{CSS}</style></head><body>
<h1>LESLIE CAROLYN</h1>
<div class="role">{e(d['role'])}</div>
<div class="contact">{contact_line}{e(d['loc'])} &nbsp;|&nbsp; {e(d['auth'])}<br>
<a href="https://lyn-devstack.github.io/lyn-portfolio/">lyn-devstack.github.io/lyn-portfolio</a> &nbsp;|&nbsp;
<a href="https://www.linkedin.com/in/carolyn-lyn-dev">linkedin.com/in/carolyn-lyn-dev</a> &nbsp;|&nbsp;
<a href="https://github.com/lyn-devstack">github.com/lyn-devstack</a>{'' if private else ' &nbsp;·&nbsp; ' + e(d['contact'])}</div>
<h2>{e(d['h_profile'])}</h2><p>{e(d['profile'])}</p>
<h2>{e(d['h_exp'])}</h2>{jobs}
<h2>{e(d['h_proj'])}</h2><ul>{projects}</ul>
<h2>{e(d['h_edu'])}</h2>{edu}
<h2>{e(d['h_skills'])}</h2>{skills}
<h2>{e(d['h_more'])}</h2><p>{e(d['more'])}</p>
</body></html>'''
    with open(os.path.join(out, f"cv_{lang}{'_postular' if private else ''}.html"), 'w', encoding='utf-8') as f:
        f.write(doc)
