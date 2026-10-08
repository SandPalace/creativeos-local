# Kit · Mi agencia de marketing agéntica

Todo local y gratis: **Obsidian** para ver y aprobar, **Claude Code** para que los agentes
trabajen. Los dos abren la misma carpeta.

```bash
git clone https://github.com/kikirrins/creativeos-local.git ~/mi-agencia
```

Sin git: descomprime `mi-agencia.zip` en `~/mi-agencia`.

**En Obsidian:** *Open folder as vault* → `~/mi-agencia` → abre `Inicio.md`.

**En la terminal:**

```bash
cd ~/mi-agencia && claude
```

0. **Acepta el diálogo de confianza** ("Do you trust the files in this folder?"). Sin eso, Claude
   Code ignora los `allow` de `.claude/settings.json` y te pedirá permiso para todo.
1. `/agents` → deben aparecer **estratega, investigador, creativo, analista**.
2. Pregunta *"¿qué skills tienes?"* → deben aparecer las 8.
3. Opcional, navegador: `cp .mcp.example.json .mcp.json` y reinicia `claude` (Playwright, gratis,
   necesita Node 20+).
4. Opcional, base de datos: `sqlite3 datos/agencia.db < datos/esquema.sql`.

Primer pedido:

> *"Arranquemos con Café Norte, un cliente nuevo."*

Mientras los agentes trabajan, mira cómo se llena `Tablero.base` en Obsidian. Para aprobar una
pieza, cambia su propiedad `estado` a `aprobada`.

Lee `CLAUDE.md` primero: ahí está quién aprueba qué. Los conectores para cuando crezcas están en
`Conectores para después.md`.

`datos/ejemplo-exporte.csv` trae métricas **ficticias** para practicar `metricas-sqlite`. Ojo:
P03 tiene el CTR más alto y es la pieza más cara por resultado.
