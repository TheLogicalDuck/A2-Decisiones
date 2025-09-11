# A2-Decisiones - "Preguntas bien pasadas de rosca"
App en flet para tomar decisiones con temática de panes, dónde le usuario elige si le gusta o no el pan.

MAPA DE DECISIÓNES
Inicio: ¿Te gusta el pan? 😏
│
├── Sí
│   └── ¿Prefieres una concha que un bolillo? 🥐
│       ├── Sí
│       │   └── ¿Te gusta el... el bolillo? 👀
│       │       ├── Sí
│       │       │   └── ¿Te gusta la torta de ate? 🤑
│       │       │       ├── Sí → ¿Te gusta el cuernito relleno de jamón? 🥪
│       │       │       │   ├── Sí → Esperanza: ¿Sí o no?
│       │       │       │   │   ├── Sí → ✅ Final Bueno
│       │       │       │   │   └── No → ✅ Final Bueno
│       │       │       │   └── No → 😑 Final Medio
│       │       │       └── No → 🥛 ¿Te gusta tomarte tu pan con leche?
│       │       │           ├── Sí → 🍯 ¿Te gusta el bolillo con mermelada?
│       │       │           │   ├── Sí → ✅ Final Bueno
│       │       │           │   └── No → 😑 Final Medio
│       │       │           └── No → 😑 Final Medio
│       │       └── No → 😑 Final Medio
│       └── No
│           └── ¿Te gusta el pan de queso? 🧀
│               ├── Sí/No → 😑 Final Medio
├── No
│   └── ¿Entonces no te gusta nada nadita? 🥺
│       ├── Sí/No → 😡 Final Malo

*Requisitos de uso:*
Python 3.9 o superior
La última versión disponible de Flet

*¿Cómo ejecutarlo?:*
-Una vez instalado python y flet, abre powershell como administrador e ingresa: "cd (ruta donde clonaste el repositorio)"
Ejemplo: C:\Users\ProgIV-28\Documents\GitHub\A2-Decisiones\first-flet-app\src
-Ahora ejecuta el comando "flet run"
-Eso es todo 🔥

(aca van a ir las capturas)