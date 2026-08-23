# 🔐 Etapa 10 — Autenticación, Autorización y Seguridad (JWT)

### 🎯 Objetivo
Implementar un sistema de autenticación seguro, protección de contraseñas, tokens JWT y control de acceso basado en roles (RBAC).

---

## 📚 Conceptos Clave
- [ ] Hashing seguro de contraseñas con `bcrypt` (salt + hash).
- [ ] JSON Web Tokens (JWT): Estructura (Header, Payload, Signature), creación y verificación.
- [ ] Middlewares de autenticación en Express (validar header `Authorization: Bearer <token>`).
- [ ] Control de roles y permisos (ej. `USER`, `ADMIN`).
- [ ] Rutas protegidas en el Frontend (guardias de navegación en React).
- [ ] Seguridad básica: CORS, Rate Limiting, Sanitización contra XSS e inyección SQL.

---

## 🏆 Proyecto de Etapa: Sistema Auth para la Tienda
- [ ] Registro (`/api/auth/register`) y Login (`/api/auth/login`).
- [ ] Perfil de Usuario regular: ver compras, modificar datos.
- [ ] Panel de Administrador: CRUD protegido de productos, ver estadísticas y ventas totales.
