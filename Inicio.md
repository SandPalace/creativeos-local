---
cssclasses: tablero
---

> [!portada|inicio] Mi agencia
> Esta bóveda **es** la agencia. El CMO y su equipo trabajan en **Claude Desktop** (modo Code); tú
> contestas, decides y firmas aquí. Todo son archivos locales: nada sale de tu computadora.

> [!tip] Empieza aquí
> 1. Deja copias de tus documentos (precios, brochure, logo…) en la carpeta **documentos**.
> 2. Abre esta carpeta en **Claude Desktop → Code** y escribe: *"Hola, soy el dueño de <tu negocio>."*
> El CMO revisa qué hay en la bóveda y te entrevista para llenar lo que falta. Mira cómo se llena
> aquí mismo.

> [!firma] La aprobación es tuya
> **Arrastra la tarjeta a _aprobada_ y escribe tu nombre en `aprobado_por`** (o abre la pieza y cambia `estado` a `aprobada`). Ningún agente puede hacerlo: es tu firma. Si falta el nombre, la tarjeta dice ⚠ *falta firma*.

## Flujo del periodo

![[Tablero.base#Flujo]]

> [!tip]- ¿Dice "unknown view type: kanban"?
> Tu Obsidian es anterior a 1.14. Ajustes → General → **Buscar actualizaciones**, y **reinicia**
> Obsidian (la actualización no se aplica hasta reiniciar). Mientras tanto, la misma información
> en tarjetas:
>
> ![[Tablero.base#Piezas]]

## Creativos

![[Tablero.base#Creativos]]

## Calendario

![[Tablero.base#Calendario]]

> [!tip]- ¿No ves el calendario?
> Usa el plugin **Calendar Bases**, que viene dentro de la bóveda. Ajustes → Plugins de la comunidad →
> **Activar plugins de la comunidad** y enciende *Calendar Bases*. Mientras tanto, la lista:
>
> ![[Tablero.base#Lista]]

## El equipo

> [!grid]
>> [!agente|cmo] CMO
>> Corre todo el pipeline. A ti sólo te pide datos y firmas.
>
>> [!agente|investigador] Investigador
>> Mercado, competidores y tendencias, siempre con fuente.
>
>> [!agente|creativo] Creativo
>> Copy y prompts de imagen/video, sólo para piezas aprobadas.
>
>> [!agente|analista] Analista
>> Números por costo por resultado y el reporte HTML.
>
>> [!agente|motion-editor] Motion editor
>> El video terminado de una pieza firmada. Llegó del estudio AI Studios.

## Estados

> [!grid]
>> [!estado|bloqueada] bloqueada
>> Falta un dato tuyo; la pregunta está en la tarjeta. Contéstala en el chat.
>
>> [!estado|propuesta] propuesta
>> Lista para que la revises y la firmes.
>
>> [!estado|aprobada] aprobada
>> Tú la aprobaste y firmaste.
>
>> [!estado|publicada] publicada
>> Ya salió.

## Atajos

> [!grid]
>> [!atajo|flujo] [[Flujo]]
>> El kanban a pantalla completa: aquí apruebas.
>
>> [!atajo|calendario] [[Calendario]]
>> El mes en cuadrícula: arrastra una pieza para cambiar su fecha.
>
>> [!atajo|equipo] [[Equipo]]
>> Los agentes y skills, leídos de `.claude/`.
>
>> [!atajo|estrategia] [[Estrategia de contenido]]
>> Cuánto publicar, graba una vez y publica muchas, qué pautar.
>
>> [!atajo|presentacion] [[Presentación]]
>> Las diapositivas del taller: comando *Start presentation*.
>
>> [!atajo|cliente] [[ejercicios/copy-con-trampa|Copy con trampa]]
>> El ejercicio de verificar hechos.
>
>> [!atajo|conectores] [[Conectores para después|Conectores]]
>> Para cuando la agencia crezca.
