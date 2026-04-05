# 🛒 Proyecto de Automatización QA – Urban Grocers API

Este repositorio contiene pruebas automatizadas para la **API de Urban Grocers**, enfocadas en validar la funcionalidad de creación de kits de productos.

---

## 📌 Descripción del proyecto

Urban Grocers es una API que permite gestionar productos y kits dentro de un sistema de compras.

El objetivo de este proyecto fue validar el comportamiento del endpoint de creación de kits, asegurando que los datos ingresados cumplan con las reglas de negocio definidas.

---

## 🎯 Objetivo de testing

- Validar el endpoint de creación de kits  
- Verificar reglas de validación del campo **"name"**  
- Identificar comportamientos esperados y errores del sistema  
- Asegurar la integridad de los datos enviados a la API  

---

## 🔍 Alcance de las pruebas

Se realizaron pruebas automatizadas sobre el endpoint de creación de kits, cubriendo escenarios como:

- Valores válidos  
- Valores inválidos  
- Campos vacíos  
- Longitud mínima y máxima  
- Tipos de datos incorrectos  

---

## 🛠️ Tecnologías y herramientas utilizadas

- 🐍 Python  
- 🧪 PyTest  
- 🔌 Requests (peticiones HTTP)  
- 📄 JSON  

---

## ⚙️ Ejecución de pruebas

1. Asegúrate de tener Python instalado  
2. Instala las dependencias:
   pip install pytest requests
3. Ejecuta las pruebas con: `pytest create_kit_name_kit_test.py

---

## 📊 Resultados
- Validación de múltiples escenarios del campo "name"
- Identificación de comportamientos esperados e inconsistencias
- Cobertura de pruebas sobre reglas clave del endpoint

---

## 🚀 Valor del proyecto
Este proyecto permitió aplicar automatización en pruebas de API, validando reglas de negocio y fortaleciendo la calidad del backend mediante pruebas estructuradas y repetibles.

---

## 📚 Documentación
Las pruebas se basan en la documentación oficial de la API proporcionada (apiDoc).

---

👩‍💻 Autor
Jessica Jiménez
QA Engineer | Software Quality Assurance
