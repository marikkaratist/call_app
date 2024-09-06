# Шаг 1: Получить список уникальных имен файлов без расширения
SELECT DISTINCT name
FROM short_names;

# Шаг 2: Обновить статус в таблице full_names
UPDATE full_names AS f
JOIN (
  SELECT DISTINCT s.name, s.status
  FROM short_names AS s
) AS s
  ON CONCAT(f.name, '.wav') = s.name
   OR CONCAT(f.name, '.mp3') = s.name
SET f.status = s.status;