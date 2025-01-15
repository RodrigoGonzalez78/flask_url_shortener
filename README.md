# Acortador de Url

## **Documentación de la API**
---

### **1. Eliminar un Short URL**
Elimina un short URL existente.

- **URL**: `/shorten/<short_code>`
- **Método**: `DELETE`
- **Descripción**: Borra el short URL asociado al `short_code`.
- **Parámetros de URL**:
  - `short_code` (string): El código único del short URL.
- **Respuestas**:
  - **204 No Content**: El short URL fue eliminado exitosamente.
  - **404 Not Found**: No se encontró un short URL con el código proporcionado.

#### **Ejemplo de petición**
```bash
DELETE /shorten/abc123
```

#### **Ejemplo de respuesta exitosa**
```
204 No Content
```

#### **Ejemplo de error**
```json
{
  "error": "Short URL not found"
}
```

---

### **2. Obtener estadísticas de un Short URL**
Obtiene estadísticas detalladas de un short URL.

- **URL**: `/shorten/<short_code>/stats`
- **Método**: `GET`
- **Descripción**: Devuelve información y estadísticas del short URL asociado al `short_code`.
- **Parámetros de URL**:
  - `short_code` (string): El código único del short URL.
- **Respuestas**:
  - **200 OK**: Devuelve las estadísticas del short URL.
  - **404 Not Found**: No se encontró un short URL con el código proporcionado.

#### **Cuerpo de la respuesta exitosa**
```json
{
  "id": "1",
  "url": "https://www.example.com/some/long/url",
  "shortCode": "abc123",
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:00:00Z",
  "accessCount": 10
}
```

#### **Ejemplo de petición**
```bash
GET /shorten/abc123/stats
```

#### **Ejemplo de respuesta exitosa**
```json
{
  "id": "1",
  "url": "https://www.example.com/some/long/url",
  "shortCode": "abc123",
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:00:00Z",
  "accessCount": 10
}
```

#### **Ejemplo de error**
```json
{
  "error": "Short URL not found"
}
```
