'''
# Question 1.
❯ docker run -it --entrypoint=bash python:3.12.8                                                                                     ─╯
root@19376041c5bb:/# pip --version
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
'''


'''
# Question 2.
db:5432

2.1 Understanding “hostname” in a Compose network
When two services are defined in the same docker-compose.yml (here, db and pgadmin), Docker automatically creates a network for them. Each service name becomes a DNS entry on that network. So, from inside the pgadmin container, the Postgres database’s hostname is whichever key you gave it under services:—in this case, db (or the container’s name, postgres, but best practice is to use the service name db).

2.2 Understanding the port mapping
Under db: ports: ["5433:5432"]
The right side (5432) is the port inside the container where Postgres is listening.
The left side (5433) is the port on your host machine that’s forwarded to internal port 5432.
But pgAdmin itself runs inside its own container, not on your host machine, so it does not need to connect to the host’s port 5433. Instead, it connects to the database’s internal port (5432) over the Docker network.

2.3 Putting it together
Hostname: db
Port: 5432
That means, when you open pgAdmin’s “Add New Server” dialog inside the browser at http://localhost:8080, the “Host name/address” field should be db and the “Port” field should be 5432.
'''


'''
Question 3.

select
    case
        when trip_distance <= 1 then 'Up to 1 mile'
        when trip_distance > 1 and trip_distance <= 3 then '1~3 miles'
        when trip_distance > 3 and trip_distance <= 7 then '3~7 miles'
        when trip_distance > 7 and trip_distance <= 10 then '7~10 miles'
        else '10+ miles'
    end as segment,
    to_char(count(1), '999,999') as num_trips
from
    green_taxi
where
    lpep_pickup_datetime >= '2019-10-01'
    and lpep_pickup_datetime < '2019-11-01'
    and lpep_dropoff_datetime >= '2019-10-01'
    and lpep_dropoff_datetime < '2019-11-01'
group by
    segment
'''


'''
Question 4.

select
lpep_pickup_datetime,
trip_distance
from green_taxi
order by trip_distance desc

"2019-10-31 23:23:41"	515.89
'''


'''
Question 5.
g
SELECT
	--g."lpep_pickup_datetime",
	count(*) PU_zone_counts,
	g."PULocationID",
 	tz."Zone"
FROM green_taxi AS g
LEFT JOIN taxi_zones AS tz
  ON g."PULocationID" = tz."LocationID"
WHERE 1=1
--AND DATE(g."lpep_pickup_datetime") = '2019-10-18'
AND lpep_pickup_datetime::date = '2019-10-18'

GROUP BY "PULocationID", tz."Zone"

ORDER BY PU_zone_counts DESC;

"pu_zone_counts"	"PULocationID"	"Zone"
1236	74	"East Harlem North"
1101	75	"East Harlem South"
931	41	"Central Harlem"
821	82	"Elmhurst"
East Harlem North, East Harlem South, Morningside Heights

'''

'''
Question 6.

with pickup_tips as (
SELECT
--*
g."tip_amount",
g."PULocationID",
tz."Zone",
g."DOLocationID"

FROM green_taxi AS g
LEFT JOIN taxi_zones AS tz
  ON g."PULocationID" = tz."LocationID"
WHERE 1=1
AND tz."Zone" = 'East Harlem North'
ORDER BY g."tip_amount" desc)

select 
pt.*,
tz."Zone"
from pickup_tips as pt
LEFT JOIN taxi_zones AS tz
  ON pt."DOLocationID" = tz."LocationID"
 ORDER BY pt."tip_amount" desc
 
"tip_amount"	"PULocationID"	"Zone"	"DOLocationID"	"Zone-2"
87.3	74	"East Harlem North"	132	"JFK Airport"
'''

'''
Question 7.

Downloading the provider plugins and setting up backend,
Generating proposed changes and auto-executing the plan
Remove all resources managed by terraform`


terraform init, terraform apply -auto-approve, terraform destroy

'''



