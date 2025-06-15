use fitness_data;
-------- hourlyintensities_merged.csv : removing null values ----------

SELECT * 
FROM hourlyintensities_merged
WHERE Id IS NOT NULL
  AND ActivityHour IS NOT NULL
  AND TotalIntensity  IS NOT NULL
  AND AverageIntensity  IS NOT NULL;
  