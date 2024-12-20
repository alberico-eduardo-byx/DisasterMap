FROM python:3.11-slim as backend-builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# --- Frontend ---

FROM NODE:22.12.0 as frontend-builder

WORKDIR /app

COPY frontend/package*.json .

RUN npm install --legacy-peer-deps

COPY frontend .

RUN npm run build

# --- Deploy ---

FROM nginx:1.27.3 as deploy

COPY --from=frontend-builder /app/build /usr/share/nginx/html

COPY --from=backend-builder /app /backend

COPY nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]