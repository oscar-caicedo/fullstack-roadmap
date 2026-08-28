# 🟢 Etapa 8 — Backend con Node.js y Express

### 🎯 Objetivo
Entender el funcionamiento del lado del servidor, el protocolo HTTP y cómo construir APIs RESTful escalables con Node.js y Express.

---

## 📚 Conceptos Clave
- [ ] Fundamentos del entorno de ejecución Node.js y NPM / package.json.
- [ ] Protocolo HTTP: Métodos (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), Códigos de estado (`200`, `201`, `400`, `401`, `404`, `500`), Headers y Payload.
- [ ] Express: Configuración de servidor, enrutamiento modular (`Router`).
- [ ] Middlewares: `express.json()`, CORS, loggers (Morgan), middlewares personalizados y manejo global de errores.
- [ ] Arquitectura en capas: Routes → Controllers → Services.
- [ ] Validación de datos en endpoints (ej. Zod o Joi).
- [ ] Variables de entorno con `dotenv`.

---

## 🏆 Proyecto de Etapa: REST API de la Tienda
Endpoints para:
- [ ] `GET /api/products`, `GET /api/products/:id`
- [ ] `POST /api/products`, `PUT /api/products/:id`, `DELETE /api/products/:id`
- [ ] `POST /api/orders` (creación de pedidos) y `GET /api/orders`
- [ ] `POST /api/users` (registro de clientes)
