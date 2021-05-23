select cd.city, cd.country, cd.avg_temp, cd.year
from city_data as cd
join city_list as cl on cl.city = cd.city
where cl.city = 'Dallas' and cl.country = 'United States'