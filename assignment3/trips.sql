SELECT 
    trip_data.request_date AS "Day", 
    ROUND(SUM(trip_data.is_canceled) * 1.0 / COUNT(trip_data.request_date), 2) AS "Cancellation Rate"
FROM 
    (
        SELECT 
            CASE WHEN status != 'completed' THEN 1 ELSE 0 END AS is_canceled, 
            request_at AS request_date
        FROM 
            Trips
        WHERE 
            client_id IN (SELECT users_id FROM Users WHERE banned = 'No') 
            AND driver_id IN (SELECT users_id FROM Users WHERE banned = 'No')
    ) AS trip_data
GROUP BY 
    trip_data.request_date
HAVING 
    trip_data.request_date BETWEEN '2013-10-01' AND '2013-10-03';
