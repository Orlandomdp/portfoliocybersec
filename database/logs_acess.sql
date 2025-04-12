
-- 1. Failed logins
SELECT * FROM logs_acess WHERE acao = 'failed_login';

-- 2. Accesses by a specific user
SELECT * FROM logs_acess WHERE username = 'admin';

-- 3. Access attempts after a certain date
SELECT * FROM logs_acess WHERE data_acess > '2025-04-10 09:00:00';

-- 4. IPs with the most access attempts
SELECT ip_origem, COUNT(*) AS tentativas
FROM logs_acess
GROUP BY ip_origem
ORDER BY tentativas DESC;
